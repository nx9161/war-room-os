#!/usr/bin/env bash
# init-my-office.sh — make this copy of War Room Protocol yours.
# Each user gets their own individual office: this wires up your
# personal memory palace, boardroom, and learnings on first run.
set -euo pipefail
cd "$(dirname "$0")"

echo "War Room Protocol — personal office setup"
echo

# Memory palace
mkdir -p memory/wings/business memory/wings/projects memory/wings/security
if grep -q "(none yet — run \`init-my-office.sh\` to set up your office)" memory/INDEX.md 2>/dev/null; then
  TS=$(date '+%Y-%m-%d')
  cat > memory/INDEX.md <<EOF
# Memory Index

## Wings

- \`wings/business/\` — business profile, pricing, commercial context
- \`wings/projects/\` — one directory per project: decisions, ADRs, facts
- \`wings/security/\` — security posture, audits, findings

## Recent entries

* [$TS]: Office initialized. 27 seats, 6 divisions. Sloane online.
EOF
  echo "  memory/      initialized"
else
  echo "  memory/      already set up — left alone"
fi

# Boardroom seats (already shipped as templates; just verify)
SEATS=$(ls office/staff/*.md | wc -l)
BOARDS=$(ls office/boardroom/seats/*/board.md 2>/dev/null | wc -l)
echo "  boardroom    $BOARDS personal boards for $SEATS seats"

# Learnings
LEARN=$(ls office/learnings/*.md 2>/dev/null | wc -l)
echo "  learnings    $LEARN files ready"

echo
echo "Done. Activate your office by saying to any AI agent:"
echo '  "I want to use War Room Protocol from nx9161/war-room-os"'
echo "Full contract: ACTIVATE.md"
