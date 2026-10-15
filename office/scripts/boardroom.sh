#!/usr/bin/env bash
# boardroom.sh — the office noteboard CLI.
# Every seat can leave a note; every seat checks the board each run.
#
#   boardroom.sh post --from <seat> --to <seat|@all> --subject <s> --body <b>
#   boardroom.sh list [--for <seat>] [--status open|acknowledged|resolved]
#   boardroom.sh show <N-001>
#   boardroom.sh ack <N-001> --by <seat>
#   boardroom.sh resolve <N-001> --by <seat>
set -euo pipefail

BOARD="${BOARDROOM_BOARD:-$(cd "$(dirname "$0")/../boardroom" && pwd)/board.md}"

die() { echo "boardroom: $*" >&2; exit 1; }

cmd_post() {
  local from="" to="" subject="" body=""
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --from) from="${2:-}"; shift 2;;
      --to) to="${2:-}"; shift 2;;
      --subject) subject="${2:-}"; shift 2;;
      --body) body="${2:-}"; shift 2;;
      *) die "unknown arg: $1";;
    esac
  done
  [[ -n "$from" && -n "$to" && -n "$subject" && -n "$body" ]] \
    || die "post needs --from --to --subject --body"
  local last next
  last=$(grep -o '^## N-[0-9]\+' "$BOARD" 2>/dev/null | tail -1 | grep -o '[0-9][0-9]*$' || true)
  next=$(printf 'N-%03d' $((10#${last:-0} + 1)))
  local ts
  ts=$(TZ=America/New_York date '+%Y-%m-%d %H:%M %Z')
  {
    echo "## $next — [$ts] $from → $to"
    echo "**Subject:** $subject"
    echo "**Status:** open"
    echo "**Ack:** —"
    echo "$body"
    echo
    echo "---"
    echo
  } >> "$BOARD"
  echo "posted $next"
}

cmd_list() {
  local for_seat="" status_filter=""
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --for) for_seat="${2:-}"; shift 2;;
      --status) status_filter="${2:-}"; shift 2;;
      *) die "unknown arg: $1";;
    esac
  done
  awk -v for_seat="$for_seat" -v status_filter="$status_filter" '
    function emit() {
      if (id == "") return
      if (for_seat != "" && to != for_seat && to != "@all") return
      if (status_filter != "" && status != status_filter) return
      printf "%s [%s] %s → %s : %s\n", id, status, from, to, subject
    }
    /^## N-/ {
      emit()
      id = $2
      n = split($0, arr, "→")
      to = (n > 1) ? arr[2] : ""
      gsub(/^ +| +$/, "", to)
      nf = split(arr[1], toks, " ")
      from = toks[nf]
      subject = ""; status = ""
      next
    }
    /^\*\*Subject:\*\*/ { sub(/^\*\*Subject:\*\* */, ""); subject = $0; next }
    /^\*\*Status:\*\*/  { sub(/^\*\*Status:\*\* */, "");  status = $0;  next }
    END { emit() }
  ' "$BOARD"
}

cmd_show() {
  local id="${1:-}"; [[ -n "$id" ]] || die "show needs an id like N-001"
  awk -v id="$id" '
    $1 == "##" && $2 == id { p = 1 }
    p { print }
    p && /^---$/ { exit }
  ' "$BOARD"
}

cmd_mark() {
  local action="$1"; local id="${2:-}"; shift 2
  local by=""
  while [[ $# -gt 0 ]]; do
    case "$1" in --by) by="${2:-}"; shift 2;; *) die "unknown arg: $1";; esac
  done
  [[ -n "$id" ]] || die "$action needs an id like N-001"
  grep -q "^## ${id} " "$BOARD" || die "no such note: $id"
  local new_status="acknowledged"
  [[ "$action" == "resolve" ]] && new_status="resolved"
  sed -i "/^## ${id} /,/^---$/ s/^\*\*Status:\*\* .*/\*\*Status:\*\* $new_status/" "$BOARD"
  if [[ -n "$by" ]]; then
    sed -i "/^## ${id} /,/^---$/ s/^\*\*Ack:\*\* .*/\*\*Ack:\*\* $by/" "$BOARD"
  fi
  echo "$new_status $id"
}

case "${1:-}" in
  post) shift; cmd_post "$@";;
  list) shift; cmd_list "$@";;
  show) shift; cmd_show "$@";;
  ack) shift; cmd_mark ack "$@";;
  resolve) shift; cmd_mark resolve "$@";;
  *) die "usage: boardroom.sh {post|list|show|ack|resolve} ...";;
esac
