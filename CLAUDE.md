# CLAUDE.md

Guidance for working in this repo. Read alongside `README.md`, `DESIGN.md`, and
`MODULES.md` — this file is the orientation; those three are the source contracts.

## What this is

A **content repo**, not an app. It holds the **Linux** topic (an LFCS course)
that the `graphl-ux` app (sibling repo) loads **at runtime**. No content logic, no
render engine, and no scenes live here — the app fetches this repo's
`manifest.json` + notebooks over the network and renders them.

There is **nothing to build, run, or test** in this repo. Changes are content and
JSON; correctness is verified by the `graphl-ux` app consuming them. (The one
executable is `scripts/colab_generate_audio.ipynb`, a Colab tool that turns the
`tts/` scripts into `audio/` `.wav`s — see "Narration" below.)

## The core contract (do not break)

1. **The notebook is the single source of truth** for a module's prose and code.
   The `manifest.json` only *wires* — it must never duplicate notebook content.
2. The app splits each notebook at every `## ` heading into **sections** (= pages).
   Sections are matched to the manifest overlay by **normalized heading text**, so
   a heading edit in a notebook must be mirrored in the manifest `heading` field.
3. A section's diagram **images (`![]()`) are stripped** by the app — a **scene**
   replaces them. Don't rely on inline notebook images surviving.
4. **Scenes live in the `graphl-ux` app** (`src/data/scenes`), authored with the
   engine's pattern helpers — **not** in this repo. The local `scenes/` dir is
   reserved/empty (`.gitkeep`). Here you only reference a scene **by id**.

## The scene

Every module points at one dense scene, **`linux`** — the full
userspace → libc → syscall → kernel → hardware stack (graphl-ux
`src/data/scenes/linux.ts`). The app pages across a module's sections without
swapping the diagram; each section spotlights the relevant `lx-*` nodes via its
`highlight` list. The node ids live in the scene TS; `MODULES.md` keeps the map.

## Layout

```
manifest.json   # wires all 10 modules: notebook ref + per-section overlay (scene/spine/role/audio/highlight)
DESIGN.md       # FIXED visual house style — palette, calm filled blocks, spotlight
MODULES.md      # the 10-module / per-section outline + spine tiering + node-id map
notebooks/      # the teaching .ipynb (prose + code source of truth) — 01..10
tts/            # per-section narration scripts (plain spoken prose)
audio/          # generated .wav narration (per-section)
scenes/         # reserved/empty — real scenes live in graphl-ux app
scripts/        # colab_generate_audio.ipynb — tts/*.tts -> audio/*.wav on a Colab GPU
```

## manifest.json shape

- Top level: `concept`, `design` (→ DESIGN.md), `scenes[]` (id/title/status), and
  `presentations[]` (one per module).
- Each presentation: `id`, `title`, `notebook` (path), `defaultScene`, and
  `sections[]`.
- Each section overlay: `heading` (must match a notebook `## ` heading, normalized),
  `scene` (a scene id), `spine` (bool — drives feed-mode linear narration), an
  optional `role` (e.g. `"hook"`), an optional `highlight` (string[] of scene
  **node ids**) — those nodes light AMBER for the section and the rest dim back;
  omit it to show the scene full-strength (e.g. the module hook) — and an `audio`
  (a repo-relative path, e.g. `"audio/01-02-what-is-linux.wav"`). Spotlighting a
  container also lights its children.

## Narration (per-section TTS)

One `.tts` script **per section**, plain spoken prose — what a teacher would say at
a whiteboard. Anchor narration to what's on screen: the notebook `## ` section.
The source curriculum (`~/Projects/linux/tts/`) ships **one `.tts` per notebook**;
here that per-module script is **split per section**, dropping the intro
("What's covered") and outro ("What you've learned" / "next up") framing — those
are not slides.

### TTS guidelines

`.tts` files are read aloud by ChatterboxTTS (typically on a T4 GPU via
`scripts/colab_generate_audio.ipynb`). They must be plain spoken prose.

- **Plain prose only** — no markdown, no `#` headings, no bullets, no backticks, no
  asterisks. Write section titles as a plain sentence ending with a full stop (e.g.
  `What is linux.`).
- **No raw code or shell commands** — describe what a command does in prose.
  `ls -la /etc` becomes "list the contents of slash e-t-c with long format and
  hidden files shown."
- **Spell out symbols, paths, and shorthand:**
  - Paths: `/etc/passwd` → "slash e-t-c slash passwd", `~/.bashrc` → "tilde slash
    dot bash-r-c"
  - Operators: `|` → "pipe", `>` → "redirect to", `>>` → "append to", `2>&1` →
    "redirect standard error to standard output", `&&` → "and-and", `||` → "or-or"
  - File descriptors: `stdin/stdout/stderr` → "standard input, standard output,
    standard error"
  - Acronyms: OS → "operating system", PID → "process I-D", UID → "user I-D",
    GID → "group I-D", CPU → "see-pee-you", RAM → "ram", DNS → "dee-en-ess", SSH →
    "ess-ess-h", TCP → "tee-see-pee", IP → "eye-pee", I/O → "input output", LVM →
    "logical volume manager", ACL → "access control list", SUID → "set user I-D"
  - Commands as words: `chmod` → "change mode", `chown` → "change owner",
    `systemctl` → "system control", `mkfs` → "make filesystem"
  - Permissions: `0755` → "octal seven-five-five"
  - Signals: `SIGTERM` → "sig-term", `SIGKILL` → "sig-kill", `SIGHUP` → "sig-hup"
- **Natural spoken flow** — write as a teacher explains at a whiteboard. Use
  transitional phrases: "notice that", "the key insight here is", "picture this".
- **Skip code outputs and tables** — never read aloud columnar output. Describe the
  takeaway instead.
- **Pace with paragraph breaks** — each paragraph = one idea. A blank line between
  paragraphs gives the TTS engine a natural pause. Aim for 2–4 sentences per
  paragraph.

### Naming & generation

- **Naming:** `tts/<NN>-<SS>-<slug>.tts` → `audio/<NN>-<SS>-<slug>.wav`, where `NN`
  is the module number and `SS` the section order (e.g. `01-02-what-is-linux`). The
  stem is shared by the `.tts`, the `.wav`, and the manifest `audio` field. `SS`
  keeps the Colab glob (`tts/*.tts`, sorted) in section order. (This per-section
  naming differs from the source curriculum, where one `.tts` matches the notebook
  stem — here narration is split per `## ` section to align with the app's pages.)
- **Generate** with `scripts/colab_generate_audio.ipynb` (ChatterboxTTS, Colab T4):
  one `.wav` per `.tts`, committed + pushed from the Colab VM. See README.

## How content is served

The app fetches this repo at runtime over **raw GitHub**:
`https://raw.githubusercontent.com/schemabotview/linux-content/main/…`
(configurable in the app via `VITE_CONTENT_BASE_URL`). No app build bundles this
content — so a content change is live once pushed to `main`, no app rebuild needed.

## Source of notebooks

Notebooks are copied as-is from the runnable curriculum at `~/Projects/linux`.
Keep them self-contained.
