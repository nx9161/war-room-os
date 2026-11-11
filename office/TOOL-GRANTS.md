# Tool Grants — what each seat may use

Intelligence Upgrade, Layer 5 (owner order 2026-10-30). A seat that
can verify beats a smarter seat guessing. This matrix declares, per
seat, the tools it may reach for when spawned. Grants are stamped
into each seat's frontmatter (`metadata.tool_grants`, via
`office/scripts/apply-tool-grants.py`) and surfaced in every spawn
packet header (`office/scripts/spawn-packet.py`, whose `--check-all`
gate fails any seat with no grants stamped).

## Binding rules

- **A grant is a may-use list, never a permission expansion.** Every
  owner gate stands exactly as before: no spend, no production
  deploys, no external sends or commitments, no contracts, without
  the owner's explicit approval.
- **Grants name tools, never credentials.** Secret values are never
  part of a grant. Where a grant says `doppler-secret-names`, the
  seat may reference secret NAMES to wire a config; values move only
  through the secure connector flow, as always.
- **Read before write.** A grant defaults to reading/verifying.
  Writing through a granted tool (a PR, a doc edit, a dashboard
  change) follows the normal house rules for that surface.
- **Not granted = ask, don't improvise.** A seat that needs a tool
  outside its grants routes the request through Sloane; MCP Maker
  builds what's missing, per the standing protocol.
- **Universal grants — the office tool skills (owner order
  2026-11-01).** Every seat holds a grant for each registered tool
  skill — `archify-diagrams`, `pxl-pixel-art`, `typesafe-ai`,
  `voice-studio` — and may use any of them directly, wherever it
  helps its work, deciding for itself whether the skill is needed.
  No routing through the custodian and no separate approval. Each
  skill keeps a custodian who owns its standard and reviews work on
  missions in their domain (Art Director — pxl; Architecture
  Visualizer — archify; Decision Model — typesafe; Voice Designer —
  voice-studio); custodians never gatekeep. A universal grant covers
  the skill and its local tooling only: any paid API, account, key,
  or external service behind a skill (e.g. TypeSafe's Jev API) stays
  behind the standing spend and credential gates above.
- **Platform material stays off the repo.** `local-platform-toolchain`
  (Console Platform) operates under NDA rules: SDK material never
  enters this repository, packets, or any shared surface.

## The matrix

| Seat | Tool grants |
|---|---|
| ai-red-teamer | web, local-test-harnesses, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| appsec-lead | codescene, github, web, sentry, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| architecture-visualizer | archify-diagrams, browser, pxl-pixel-art, voice-studio, typesafe-ai |
| art-director | browser, media-generation, pxl-pixel-art, web, archify-diagrams, voice-studio, typesafe-ai |
| business-analyst | google-sheets, web, stripe-read, palace, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| casting-director | web, local-skills-tree, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| console-platform-engineer | local-platform-toolchain, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| connector-operator | doppler, github, boardroom, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| decision-model | typesafe-ai, palace, pxl-pixel-art, archify-diagrams, voice-studio |
| devops-sre | vercel, github, datadog, sentry, doppler-secret-names, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| diagram-designer | local-diagram-tools, browser, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| document-artisan | google-docs, google-sheets, google-slides, local-doc-tools, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| enterprise-architect | github, palace, archify-diagrams, web, boardroom, pxl-pixel-art, voice-studio, typesafe-ai |
| excel-specialist | local-sheet-tools, google-sheets, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| financial-analyst | google-sheets, stripe-read, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| game-architect | local-game-toolchain, palace, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| game-producer | boardroom, palace, github, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| game-ui-ux-designer | figma, browser, local-playtest-builds, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| gameplay-designer | local-playtest-builds, palace, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| general-counsel | web, palace, google-docs, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| global-tech-law-lead | web, palace, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| harness-engineer | local-skills-tree, github, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| knowledge-wizard | web, browser, palace, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| launch-strategist | web, social-search, notion, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| lead-backend-dev | github, git, supabase, neon, sentry, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| lead-code-reviewer | github, git, codescene, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| lead-frontend-dev | github, git, browser, browserstack, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| mcp-maker | web, git, local-cli-scaffolding, doppler-secret-names, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| memory-keeper | palace, learnings, boardroom, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| mission-control | boardroom, palace, github, goal-tracking, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| penetration-tester | local-pentest-sandbox, codescene, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| product-owner | notion, google-docs, palace, boardroom, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| product-visualizer | media-generation, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| prompt-writer | palace, boardroom, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| qa-manager | browser, browserstack, local-test-runners, github, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| reverse-engineer | local-re-tools, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| sales-agent | web, gmail-drafts, notion, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| scriptwriter | web, google-docs, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| seo-specialist | web, browser, github, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| sloane | boardroom, palace, office-scripts, github, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| social-media-strategist | instagram, threads, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| tax-strategist | web, palace, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| ui-ux-designer | figma, browser, web, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| voice-designer | voice-studio, web, pxl-pixel-art, archify-diagrams, typesafe-ai |
| word-specialist | local-doc-tools, google-docs, pxl-pixel-art, archify-diagrams, voice-studio, typesafe-ai |
| connector-aiven | aiven, boardroom, palace |
| connector-apple-notes | apple-notes, boardroom, palace |
| connector-appwrite | appwrite, boardroom, palace |
| connector-blackfire | blackfire, boardroom, palace |
| connector-browserstack | browserstack, boardroom, palace |
| connector-camber | camber, boardroom, palace |
| connector-clerk | clerk, boardroom, palace |
| connector-cloudflare | cloudflare, boardroom, palace |
| connector-codescene | codescene, boardroom, palace |
| connector-datadog | datadog, boardroom, palace |
| connector-deepnote | deepnote, boardroom, palace |
| connector-doppler | doppler, boardroom, palace |
| connector-heroku | heroku, boardroom, palace |
| connector-icloud-mail | icloud-mail, boardroom, palace |
| connector-lambdatest | lambdatest, boardroom, palace |
| connector-legacy-elevenlabs | legacy-elevenlabs, boardroom, palace |
| connector-mapwarper | mapwarper, boardroom, palace |
| connector-neon | neon, boardroom, palace |
| connector-newrelic | newrelic, boardroom, palace |
| connector-prisma | prisma, boardroom, palace |
| connector-reddit | reddit, boardroom, palace |
| connector-sentry | sentry, boardroom, palace |
| connector-sentry-api | sentry-api, boardroom, palace |
| connector-supabase | supabase, boardroom, palace |
| connector-testmail | testmail, boardroom, palace |
| connector-upstash | upstash, boardroom, palace |
| connector-vercel-cli | vercel-cli, boardroom, palace |
| connector-zyte | zyte, boardroom, palace |
| connector-trophy-account | trophy-account, boardroom, palace |
| connector-turso | turso, boardroom, palace |
| connector-agoda | agoda, boardroom, palace |
| connector-apple-healthkit | apple-healthkit, boardroom, palace |
| connector-asana | asana, boardroom, palace |
| connector-box | box, boardroom, palace |
| connector-calendly | calendly, boardroom, palace |
| connector-canva | canva, boardroom, palace |
| connector-dropbox | dropbox, boardroom, palace |
| connector-duffel | duffel, boardroom, palace |
| connector-evernote | evernote, boardroom, palace |
| connector-facebook-cli | facebook-cli, boardroom, palace |
| connector-figma | figma, boardroom, palace |
| connector-flightaware | flightaware, boardroom, palace |
| connector-function-health | function-health, boardroom, palace |
| connector-ghl | ghl, boardroom, palace |
| connector-github | github, boardroom, palace |
| connector-gmail | gmail, boardroom, palace |
| connector-google-calendar | google-calendar, boardroom, palace |
| connector-google-contacts | google-contacts, boardroom, palace |
| connector-google-docs | google-docs, boardroom, palace |
| connector-google-drive | google-drive, boardroom, palace |
| connector-google-forms | google-forms, boardroom, palace |
| connector-google-health-connect | google-health-connect, boardroom, palace |
| connector-google-sheets | google-sheets, boardroom, palace |
| connector-google-slides | google-slides, boardroom, palace |
| connector-google-tasks | google-tasks, boardroom, palace |
| connector-granola | granola, boardroom, palace |
| connector-gumroad-mcp | gumroad-mcp, boardroom, palace |
| connector-healthex | healthex, boardroom, palace |
| connector-instagram | instagram, boardroom, palace |
| connector-instagram-messages | instagram-messages, boardroom, palace |
| connector-klaviyo | klaviyo, boardroom, palace |
| connector-linear | linear, boardroom, palace |
| connector-lovable | lovable, boardroom, palace |
| connector-messenger-read | messenger-read, boardroom, palace |
| connector-meta-ads | meta-ads, boardroom, palace |
| connector-meta-catalog-search | meta-catalog-search, boardroom, palace |
| connector-moneyforward-me | moneyforward-me, boardroom, palace |
| connector-muse-mail | muse-mail, boardroom, palace |
| connector-notion | notion, boardroom, palace |
| connector-onepassword | onepassword, boardroom, palace |
| connector-opentable | opentable, boardroom, palace |
| connector-outlook-calendar | outlook-calendar, boardroom, palace |
| connector-outlook-contacts | outlook-contacts, boardroom, palace |
| connector-outlook-mail | outlook-mail, boardroom, palace |
| connector-peloton | peloton, boardroom, palace |
| connector-philips-hue | philips-hue, boardroom, palace |
| connector-places | places, boardroom, palace |
| connector-plaid | plaid, boardroom, palace |
| connector-printify | printify, boardroom, palace |
| connector-quickbooks | quickbooks, boardroom, palace |
| connector-readwise-mcp | readwise-mcp, boardroom, palace |
| connector-replit | replit, boardroom, palace |
| connector-runway-mcp | runway-mcp, boardroom, palace |
| connector-shop-pay | shop-pay, boardroom, palace |
| connector-shopback-mcp | shopback-mcp, boardroom, palace |
| connector-shopify | shopify, boardroom, palace |
| connector-shopify-ucp | shopify-ucp, boardroom, palace |
| connector-slack | slack, boardroom, palace |
| connector-spotify | spotify, boardroom, palace |
| connector-stripe | stripe, boardroom, palace |
| connector-stripe-link | stripe-link, boardroom, palace |
| connector-tailscale | tailscale, boardroom, palace |
| connector-tessie | tessie, boardroom, palace |
| connector-threads | threads, boardroom, palace |
| connector-threads-messages | threads-messages, boardroom, palace |
| connector-ticketmaster | ticketmaster, boardroom, palace |
| connector-todoist | todoist, boardroom, palace |
| connector-vercel | vercel, boardroom, palace |
| connector-vidiq-mcp | vidiq-mcp, boardroom, palace |
| connector-withings | withings, boardroom, palace |
| connector-zapier | zapier, boardroom, palace |
| connector-zoom | zoom, boardroom, palace |

## Tool keys

`web` = search + full-page reads of official sources · `browser` =
live-browser verification · `github`/`git` = the owner's repos via the
GitHub connector / gh · `palace` = the repo memory palace ·
`boardroom` = the office noteboard · `learnings` = seat learning
files · `office-scripts` = the office's own scripts · `stripe-read` =
read-only Stripe balance/payment reads · `gmail-drafts` = draft only,
sending needs the owner's approval per message · `media-generation` =
image/video generation through the host · `social-search` = public
social listening · `doppler-secret-names` = secret names only, never
values · `local-*` = toolchains on the host machine (docs, sheets,
diagrams, RE, pentest sandbox, game/platform toolchains, test
runners, playtest builds, CLI scaffolding) · named connectors
(figma, notion, vercel, sentry, datadog, codescene, browserstack,
supabase, neon, instagram, threads, google-*) = the owner's connected
services, used through their connector docs.
