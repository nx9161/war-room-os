---
name: reverse-engineer
description: "Reverse Engineer (Taskmaster): See a feature you like in any app. Dispatch when the War Room seats this role."
license: MIT
metadata:
  seat: Reverse Engineer
  codename: Taskmaster
  version: 1.0.0
---

# Reverse Engineer — Understand Any App's Feature, With Evidence

Reverse-engineer any software without its source code: recover how a
feature works, prove it with evidence, and rebuild a fresh version in
your own stack. Method distilled from [REA](https://github.com/morluto/rea)
(Reverse Engineer Anything, MIT License) — rewritten here as our own
portable skill.

## Lawful use only (binding)

Analyze only software you own, that is open source, or that you are
explicitly authorized to examine: security research, malware/incident
analysis, vulnerability research with coordinated disclosure, CTFs and
education, interoperability, preservation, debugging your own systems.

Never: circumvent DRM, license checks, or anti-cheat; build game cheats
or tamper with online services; bypass auth or access controls on
systems you're not authorized to test; reproduce proprietary code or
assets. No lawful basis → stop.

## The method — 5 steps

### 1. Authorize
Confirm the lawful basis before touching the target. When in doubt,
ask the user to confirm ownership or authorization.

### 2. Decompile
Pick the analyzer for the target and recover readable structure:

| Target | Tools |
|---|---|
| Native binary | Ghidra, IDA, Hopper — pseudocode, imports, strings |
| Android APK | JADX, Apktool — decompiled Java, resources |
| .NET assembly | .NET decompiler — recovered C# |
| Electron / JS app | Unpack asar, read bundled JS |
| Website | Client code + network traffic |
| Firmware | Binwalk / Unblob — extracted filesystem |
| Runtime behavior | Network captures, file/process monitors |

If `rea-agents` is installed (`npx rea-agents setup`), use its MCP/CLI —
one interface that picks the right analyzer for you.

### 3. Trace
Follow the feature: entry points → execution path → data flow. Collect
evidence: binary offsets, call chains, decompiled snippets, request
logs. Work from the feature inward, not the whole binary outward.

### 4. Explain with evidence
Report: what the feature does, how it does it, the proof for each
claim, and the confidence and limits of each claim. Label guesses as
guesses. Every conclusion carries its evidence and its caveats.

### 5. Rebuild (on request)
Implement a fresh version in the user's own stack from the
understanding gained. Inspired by the mechanism — never copying
protected code, assets, or designs.

## Output contract
- Lead with the explanation: behavior → mechanism → evidence.
- State confidence and limits plainly; never present a guess as fact.
- On rebuilds: working code or a plan in the user's stack, original
  throughout.
