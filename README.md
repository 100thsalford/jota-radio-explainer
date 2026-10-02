# JOTA Radio Explainer

An auto-looping, full-screen slideshow for a JOTA-JOTI station. It explains ham radio to Beavers, Cubs and Scouts while they wait for a turn on the microphone.

18 slides (about 4½ minutes per loop): the big idea, broadcast vs ham radio, press-to-talk, the journey of your voice, wave sizes, VHF/UHF vs HF, the radio alphabet, radio shorthand, signal reports, the J-Code and a simple contact script.

## Running it at the event

1. Open the Netlify URL in Chrome or Edge on the laptop connected to the screen.
2. Press **F** (or the Full screen button) to go full screen.
3. Leave it. It loops forever, hides the mouse pointer and keeps the screen awake.

Controls: **←/→** previous/next, **Space** pause/play, **S** voice on/off, **F** full screen. Move the mouse to show the control bar.

## Voiceover and captions

On load, click **Start with sound** once (browsers block sound until someone clicks). If nobody clicks within 25 seconds it starts quietly with captions; a tap on the screen turns the voice on.

Each slide plays its recorded clip from `audio/` if there is one, otherwise the browser reads the line aloud. Captions always show along the bottom. Slides wait for the voice to finish before moving on. For the best browser voice, use Microsoft Edge on Windows. See [RECORDING.md](RECORDING.md) for the script and file names.

## Set your callsign

Edit one line near the bottom of `deck.html`:

```js
const CONFIG = { callsign: "GB0XXX" };
```

The callsign and its phonetic spelling update everywhere in the deck.

## Files

- `deck.html` is the source (also published as a Claude artifact).
- `build.py` wraps it into `index.html`, which Netlify serves. Netlify runs it on every deploy.

Content adapted from the World Scouting *JOTA-JOTI Ham Radio Handbook* (2022).
