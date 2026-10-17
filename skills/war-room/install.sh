#!/usr/bin/env bash
# Install the War Room Protocol as agent skills.
#
# Installs the `war-room` master skill (the Chief's operating manual),
# and optionally all 43 seat skills, into your AI agent harness.
#
# Usage:
#   ./install.sh                  # master skill -> every detected harness
#   ./install.sh --seats          # ...plus all 43 seat skills
#   ./install.sh --project        # repo-local skill dirs instead of global
#   ./install.sh --claude-code --codex   # pick harnesses explicitly
#   ./install.sh --list           # show detected harnesses, install nothing
#
# Run from a clone of https://github.com/nx9161/war-room-os — or from
# anywhere: without a local template it clones the public repo to a
# temp dir automatically.
set -euo pipefail

SKILL_NAME="war-room"
TEMPLATE_URL="https://github.com/nx9161/war-room-os"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOME_DIR="${HOME:-$HOME}"

PROJECT_MODE=0
INSTALL_SEATS=0
LIST_ONLY=0
declare -a WANT=()

usage() { sed -n '2,16p' "$0" | sed 's/^# \?//'; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)    PROJECT_MODE=1 ;;
    --seats)      INSTALL_SEATS=1 ;;
    --list)       LIST_ONLY=1 ;;
    --claude-code) WANT+=(claude-code) ;;
    --codex)      WANT+=(codex) ;;
    --cursor)     WANT+=(cursor) ;;
    --copilot)    WANT+=(copilot) ;;
    --gemini)     WANT+=(gemini) ;;
    --opencode)   WANT+=(opencode) ;;
    --all)        WANT=(claude-code codex cursor copilot gemini opencode) ;;
    -h|--help)    usage; exit 0 ;;
    *) echo "Unknown flag: $1" >&2; usage >&2; exit 1 ;;
  esac
  shift
done

# Locate the template: prefer the repo this script lives in, else clone.
TEMPLATE_DIR=""
if [[ -d "$SCRIPT_DIR/../../office/skills" ]]; then
  TEMPLATE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
else
  TEMPLATE_DIR="$(mktemp -d)/war-room-os"
  echo "No local template found — cloning $TEMPLATE_URL ..."
  git clone -q --depth 1 "$TEMPLATE_URL" "$TEMPLATE_DIR"
fi
SKILL_SRC="$TEMPLATE_DIR/skills/$SKILL_NAME"
SEATS_SRC="$TEMPLATE_DIR/office/skills"

skill_dir() {
  case "$1" in
    claude-code) [[ $PROJECT_MODE -eq 1 ]] && echo ".claude/skills/$2"  || echo "$HOME_DIR/.claude/skills/$2" ;;
    codex)      [[ $PROJECT_MODE -eq 1 ]] && echo ".agents/skills/$2"   || echo "$HOME_DIR/.agents/skills/$2" ;;
    cursor)     [[ $PROJECT_MODE -eq 1 ]] && echo ".cursor/skills/$2"   || echo "$HOME_DIR/.cursor/skills/$2" ;;
    copilot)    [[ $PROJECT_MODE -eq 1 ]] && echo ".github/skills/$2"   || echo "$HOME_DIR/.copilot/skills/$2" ;;
    gemini)     [[ $PROJECT_MODE -eq 1 ]] && echo ".gemini/skills/$2"   || echo "$HOME_DIR/.gemini/skills/$2" ;;
    opencode)   [[ $PROJECT_MODE -eq 1 ]] && echo ".opencode/skills/$2" || echo "$HOME_DIR/.config/opencode/skills/$2" ;;
  esac
}

detect() {
  command -v claude >/dev/null 2>&1 && echo "claude-code"
  { command -v codex >/dev/null 2>&1 || [[ -d "$HOME_DIR/.codex" ]]; } && echo "codex"
  { command -v cursor >/dev/null 2>&1 || [[ -d "$HOME_DIR/.cursor" ]]; } && echo "cursor"
  { command -v copilot >/dev/null 2>&1 || [[ -d "$HOME_DIR/.copilot" ]]; } && echo "copilot"
  { command -v gemini >/dev/null 2>&1 || [[ -d "$HOME_DIR/.gemini" ]]; } && echo "gemini"
  { command -v opencode >/dev/null 2>&1 || [[ -d "$HOME_DIR/.config/opencode" ]]; } && echo "opencode"
  return 0
}

install_skill_dir() {
  # install_skill_dir <src> <harness> <skill-name>
  local src="$1" harness="$2" name="$3"
  local dest
  dest="$(skill_dir "$harness" "$name")"
  mkdir -p "$dest"
  rm -rf "${dest:?}"
  mkdir -p "$dest"
  cp -r "$src"/. "$dest"/
  # install.sh and test/ don't belong in an installed skill
  rm -f "$dest/install.sh"
  rm -rf "$dest/test"
  echo "installed: $harness/$name -> $dest"
}

if [[ ${#WANT[@]} -eq 0 ]]; then
  # shellcheck disable=SC2207
  WANT=($(detect))
fi

if [[ $LIST_ONLY -eq 1 ]]; then
  if [[ ${#WANT[@]} -eq 0 ]]; then echo "No supported harnesses detected.";
  else
    echo "Detected harnesses:"
    for h in "${WANT[@]}"; do echo "  - $h -> $(skill_dir "$h" "$SKILL_NAME")"; done
    if [[ $INSTALL_SEATS -eq 1 ]]; then
      echo "Seat skills available: $(find "$SEATS_SRC" -maxdepth 1 -mindepth 1 -type d | wc -l)"
    fi
  fi
  exit 0
fi

if [[ ${#WANT[@]} -eq 0 ]]; then
  echo "No supported harnesses detected. Pass one explicitly, e.g.:" >&2
  echo "  ./install.sh --claude-code --codex" >&2
  exit 1
fi

count=0
for h in "${WANT[@]}"; do
  install_skill_dir "$SKILL_SRC" "$h" "$SKILL_NAME"
  count=$((count + 1))
  if [[ $INSTALL_SEATS -eq 1 ]]; then
    for seat_dir in "$SEATS_SRC"/*/; do
      seat="$(basename "$seat_dir")"
      [[ -f "$seat_dir/SKILL.md" ]] || continue
      install_skill_dir "$seat_dir" "$h" "$seat" >/dev/null
      count=$((count + 1))
    done
    echo "  (+ seat skills installed for $h)"
  fi
done

echo
echo "Done ($count skill install(s)). Say the trigger phrase to your agent:"
echo '  "War Room Protocol"'
