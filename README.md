# linux-content

Content repo for the **Linux** topic in graphl-ux. Designed to load at runtime;
no content logic lives in the app code. Follows the **manifest +
notebook-as-source-of-truth** contract.

## Layout

```
linux-content/
  manifest.json     # wires modules: notebook ref + per-section overlay (scene/spine/audio)
  DESIGN.md         # the visual house style (calm filled blocks, palette, reel chrome)
  MODULES.md        # the curated module/section outline + spine/depth tiering
  notebooks/        # the 10 teaching .ipynb (the prose + code source of truth)
  scenes/           # reserved — scenes live in the graphl-ux app (src/scenes), not here
  tts/              # per-section narration scripts (plain spoken prose)
  audio/            # generated .wav narration
  scripts/          # colab_generate_audio.ipynb — TTS .tts -> .wav on a Colab GPU
```

## Generating audio

Narration `.wav`s are produced from the `tts/*.tts` scripts by
`scripts/colab_generate_audio.ipynb` (ChatterboxTTS on a Colab T4 GPU). It clones
this repo, generates one `audio/<stem>.wav` per `tts/<stem>.tts`, and commits +
pushes each clip straight from the Colab VM. Needs a Colab secret `GITHUB_TOKEN`
(a PAT with **Contents: Read/Write** on `schemabotview/linux-content`). Set
`FORCE=True` to regenerate existing clips, or `ONLY_STEM="01-02-what-is-linux"` to
do a single section. This is a convenience tool — there is otherwise nothing to
build or run in this repo.

## Contract

- The **notebook is the single source of truth** for a module's prose and code.
  The manifest only *wires* — it never duplicates notebook content.
- The app splits each notebook at every `## ` heading into **sections** (= pages).
  A section's diagram **images (`![]()`) are stripped** — the scene replaces them.
- The manifest overlay attaches, per section: a `scene` id (the diagram), a
  `spine` flag (drives feed-mode flow), an optional `role` (e.g. `hook`), an
  optional `highlight` (scene node ids that light AMBER), and an `audio` stem.
  Sections are matched to the overlay by normalized heading.
- A **scene** is a reusable `SceneSpec` (portrait 800×1200) referenced by id from
  many sections. Scenes are authored and bundled in the **graphl-ux app**
  (`src/scenes`, with the engine's pattern helpers) — they are **not** served from
  this repo. Styled per `DESIGN.md`.

## The scene

Every Linux module points at one dense scene, **`linux`** — the full
userspace → libc → syscall → kernel → hardware stack (authored in the graphl-ux
app at `src/data/scenes/linux.ts`). The app pages across a module's sections
without swapping the diagram; each section spotlights the relevant `lx-*` nodes
via its `highlight` list. See `MODULES.md` for the node-id map.

## Source

Notebooks are copied as-is from the runnable curriculum at `~/Projects/linux`
(the LFCS course). Keep them self-contained. The source curriculum ships one
`.tts` per notebook; here narration is **split per `## ` section** to align with
the app's pages.

## Status

All 10 notebooks are present in `notebooks/`. The manifest wires every content
section (the intro "What's covered" and the outro "What you've learned" are
dropped — they are framing, not slides) to the `linux` scene with spine flags,
per-section `highlight`, and a per-section `audio` stem. Per-section `tts/`
scripts are authored by splitting the source per-module narration; their `.wav`s
are generated via `scripts/colab_generate_audio.ipynb`.

**Serving.** graphl-ux fetches this repo at runtime over raw GitHub
(`https://raw.githubusercontent.com/schemabotview/linux-content/main/…`,
configurable via the app's `VITE_CONTENT_BASE_URL`). No app build bundles this
content; the app ships only the render engine + scenes.
