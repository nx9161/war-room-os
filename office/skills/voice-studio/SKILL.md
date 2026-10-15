# Voice Studio — Local Voice Cloning, Design & Dubbing for AI Agents

Clone voices, design original ones, synthesize speech, and dub videos —
running locally with no keys, credits, or subscription. Method distilled
from [VoiceStudio](https://github.com/debpalash/VoiceStudio) (open source —
credited, not copied).

## Consent boundary (binding)

Clone only with the explicit consent of the voice owner: your own voice,
licensed voices, or written agreement from the owner. Never impersonate a
real person without consent. No clones for deception, fraud, or fake
endorsements. No lawful basis → stop.

## The method — 5 steps

### 1. Capture
Get a clean voice sample from the owner. One good recording is enough to
start. Note the language and style — they carry into the clone.

### 2. Clone / Design
- **Clone:** build the voice model from the sample.
- **Design:** craft an original voice from parameters (pitch, pace,
  warmth, accent) — give every character its own voice.

If the VoiceStudio app is installed, use it (Electron app, downloadable
models, local API + MCP for agents). Otherwise use local TTS/voice
models directly — same steps.

### 3. Synthesize
Text in, speech out, in that voice. Iterate on pacing, emphasis, and
tone. For long-form (audiobooks, podcasts), synthesize per section and
keep voice settings fixed so the voice stays consistent.

### 4. Produce
- **Video dubbing:** timed speech per segment, matched to the video's
  pacing; translate-then-dub for other languages.
- **Audiobooks/podcasts:** chapter-by-chapter narration.
- **Characters:** a distinct designed voice per character.

### 5. Verify by ear
Listen to the output before it ships. If it doesn't sound human, it
goes back to step 3. The ear is the final gate — no exceptions.

## Output contract
- Deliver finished, listen-approved audio — never raw first-pass synthesis.
- Keep the voice model + settings with the project so the voice stays
  consistent across productions.
- State the consent basis for every cloned voice (own voice / licensed /
  written agreement).
