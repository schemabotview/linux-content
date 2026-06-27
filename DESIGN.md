# Visual design — tuned for retention on mobile + Udemy video

Two delivery targets: a **mobile reel feed** and **recorded Udemy lessons**. Both
are served by the same dark, high-contrast, semantic-color system below. This is
the Linux topic's house style; it mirrors the shared graphl-ux look.

## Style: calm filled blocks (NOT neon)

The diagram reads like a clean reference figure, not a glowing dashboard. Color
lives in a **muted filled block**, not a neon outline. Rules:

- **No glow** (no `box-shadow`), **no backdrop-blur**, **no dotted grid**.
- Nodes are **filled** with the role hue mixed into a dark base (`#14161c`) at
  ~30% — a desaturated block, with a thin solid border one step brighter. White
  bold title; sub-caption a soft tint of the role color.
- **Edges are plain gray (`#5b6270`), thin**, with a **small slow gray flow dot**
  (2.4s) as a gentle directional cue — calm, not neon. Brighter color/motion is
  *reserved* for the narration spotlight, so the spotlight still stands apart.
  Keep edge count low — prefer 2 clean arrows over many crossing ones.

## Background

- Scene canvas + app: **`#16181d`** (flat neutral dark — no blue tint, no grid;
  avoids OLED smear / video banding; portrait pillarbox bars vanish into it).
- Code panel: **`#0d1117`** (github-dark, matches highlight.js theme).

## Semantic palette (FIXED roles — do not reuse a color for an unrelated concept)

The Linux scene is a layered stack; each band has a role color. The map below is
what the `linux` scene already encodes (`graphl-ux/src/data/scenes/linux.ts`).

| Token  | Hex       | Always means…                                                  |
| ------ | --------- | -------------------------------------------------------------- |
| BLUE   | `#5b8cff` | **Userspace surface** — shell, VFS, files, RAM                 |
| GREEN  | `#37d39a` | **Kernel compute** — processes, scheduler, the kernel itself   |
| PURPLE | `#b98bff` | **Privilege & memory** — users, permissions (DAC), MMU, CPU rings |
| ORANGE | `#ff7a59` | **Services & off-box I/O** — init/systemd, packages, network, NIC |
| TEAL   | `#3fd0d6` | **Data flow** — streams (fd 0/1/2), block I/O, block devices   |
| RED    | `#ff5d6c` | **Hard boundaries** — the syscall line, container isolation, package install |
| YELLOW | `#f5c542` | **Translation layer** — libc (glibc/musl), shell expansion     |
| GRAY   | `#9aa3b2` | **Inert / context** — boot, tracing, the `/`-tree view, hardware |

Color is a *memory cue*: a learner who sees kernel=green every time encodes it
faster. Keep ≤4–5 colors live on screen at once; push everything supporting to
GRAY so the colored nodes actually *mean* something.

## Spotlight (the video attention lever)

- **AMBER `#ffc24b`** is reserved for the **node(s) the narration is on right now**
  — brighter glow + the animated flow-in-path edge converging on them. A section's
  manifest `highlight` list names those `lx-*` node ids; the rest of the scene dims
  back. Spotlighting a container also lights its children. Omit `highlight` to show
  the scene full-strength (e.g. the module hook).
- Nothing else uses amber. Motion + a reserved highlight color drives the eye to
  exactly the concept being spoken — the biggest retention win in video/feed.

## Typography (legibility on small screens + after compression)

- Labels **bold, large** (≥ ~18px equiv at the 800×1200 scale); avoid thin weights
  — compression eats them.
- `term` chips (the label *is* the concept) use mono + a filled tint of the role
  color.

## Motion

- Edges animate a dot along the path (`flow-in-path`) to show direction/sequence.
- Reveal spine nodes in narration order; depth nodes appear with the panel.
- Keep it calm — one thing moving at a time, paced to the narration's 300 ms
  pauses (blank lines in the `.tts`).
