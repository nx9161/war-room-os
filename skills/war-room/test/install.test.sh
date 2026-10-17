#!/usr/bin/env bash
# Hermetic test for skills/war-room/install.sh.
# Builds a fake template (master skill + 2 seat skills), fake HOME, fake CLIs.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INSTALL="$SCRIPT_DIR/install.sh"

pass=0; fail=0
ok()  { pass=$((pass+1)); echo "ok   - $1"; }
bad() { fail=$((fail+1)); echo "FAIL - $1"; }

# 1. Frontmatter sanity.
name="$(sed -n 's/^name: *//p' "$SCRIPT_DIR/SKILL.md" | head -1 | tr -d ' "')"
desc="$(sed -n 's/^description: *//p' "$SCRIPT_DIR/SKILL.md" | head -1)"
[[ "$name" == "war-room" ]] && ok "frontmatter name matches folder" || bad "frontmatter name ($name)"
[[ -n "$desc" ]] && ok "description present" || bad "description missing"
(( ${#desc} <= 200 )) && ok "description <= 200 chars (${#desc})" || bad "description too long (${#desc})"
grep -q '^license: MIT' "$SCRIPT_DIR/SKILL.md" && ok "license MIT" || bad "license field"
[[ -f "$SCRIPT_DIR/references/roster.md" && -f "$SCRIPT_DIR/references/phases.md" && -f "$SCRIPT_DIR/references/activation.md" ]] \
  && ok "references present" || bad "references missing"

# 2. Fake template + environment.
FAKE_TEMPLATE="$(mktemp -d)"
mkdir -p "$FAKE_TEMPLATE/skills/war-room" "$FAKE_TEMPLATE/office/skills"
cp -r "$SCRIPT_DIR"/. "$FAKE_TEMPLATE/skills/war-room"/
for seat in product-owner appsec-lead; do
  mkdir -p "$FAKE_TEMPLATE/office/skills/$seat"
  printf -- '---\nname: %s\ndescription: Test seat.\n---\n\n# %s\n' "$seat" "$seat" \
    > "$FAKE_TEMPLATE/office/skills/$seat/SKILL.md"
done
# Point the installer at the fake template by shadowing SCRIPT_DIR resolution:
# the installer derives the template from its own location, so copy it there.
cp "$INSTALL" "$FAKE_TEMPLATE/skills/war-room/install.sh"
FAKE_INSTALL="$FAKE_TEMPLATE/skills/war-room/install.sh"

FAKE_HOME="$(mktemp -d)"; FAKE_BIN="$(mktemp -d)"
export HOME="$FAKE_HOME" PATH="$FAKE_BIN:$PATH"
trap 'rm -rf "$FAKE_HOME" "$FAKE_BIN" "$FAKE_TEMPLATE"' EXIT
for cli in claude codex; do printf '#!/bin/sh\nexit 0\n' > "$FAKE_BIN/$cli"; chmod +x "$FAKE_BIN/$cli"; done

# 3. --list detects fake harnesses and counts seat skills.
list_out="$(bash "$FAKE_INSTALL" --list --seats)"
echo "$list_out" | grep -q "claude-code" && ok "detect claude-code" || bad "detect claude-code"
echo "$list_out" | grep -q "codex" && ok "detect codex" || bad "detect codex"
echo "$list_out" | grep -q "Seat skills available: 2" && ok "seat count = 2" || bad "seat count"

# 4. Master-only install.
bash "$FAKE_INSTALL" --all >/dev/null
for d in "$FAKE_HOME/.claude/skills/war-room" "$FAKE_HOME/.agents/skills/war-room"; do
  [[ -f "$d/SKILL.md" && -f "$d/references/phases.md" ]] && ok "master install ($d)" || bad "master install ($d)"
  [[ ! -e "$d/install.sh" && ! -e "$d/test" ]] && ok "installer/test excluded ($d)" || bad "installer leaked ($d)"
done
[[ ! -d "$FAKE_HOME/.claude/skills/product-owner" ]] && ok "no seats without --seats" || bad "seats installed unexpectedly"

# 5. --seats installs every seat skill.
bash "$FAKE_INSTALL" --all --seats >/dev/null
[[ -f "$FAKE_HOME/.claude/skills/product-owner/SKILL.md" ]] && ok "seat install (claude-code)" || bad "seat install (claude-code)"
[[ -f "$FAKE_HOME/.agents/skills/appsec-lead/SKILL.md" ]] && ok "seat install (codex)" || bad "seat install (codex)"
seat_name="$(sed -n 's/^name: *//p' "$FAKE_HOME/.claude/skills/product-owner/SKILL.md" | head -1 | tr -d ' "')"
[[ "$seat_name" == "product-owner" ]] && ok "seat frontmatter intact" || bad "seat frontmatter"

# 6. Idempotent.
before="$(find "$FAKE_HOME" -type f | sort | sha256sum)"
bash "$FAKE_INSTALL" --all --seats >/dev/null
after="$(find "$FAKE_HOME" -type f | sort | sha256sum)"
[[ "$before" == "$after" ]] && ok "idempotent re-install" || bad "re-install changed tree"

# 7. --project installs repo-local.
PROJ="$(mktemp -d)"; cd "$PROJ"
bash "$FAKE_INSTALL" --project --claude-code >/dev/null
[[ -f "$PROJ/.claude/skills/war-room/SKILL.md" ]] && ok "project install" || bad "project install"
cd - >/dev/null; rm -rf "$PROJ"

# 8. Unknown flag rejected.
bash "$FAKE_INSTALL" --nope >/dev/null 2>&1 && bad "unknown flag should fail" || ok "unknown flag rejected"

echo
echo "passed: $pass, failed: $fail"
[[ $fail -eq 0 ]]
