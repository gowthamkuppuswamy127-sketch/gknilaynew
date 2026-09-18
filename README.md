# gknilaynew

Two unrelated things live in this repository.

## 1. Nilayaa Interiors website

A four-page static marketing site at the repository root — `index.html`,
`portfolio.html`, `services.html`, `contact.html`. No build step, no backend.

* **[SITE.md](SITE.md)** — how it is built, how to edit it, how to deploy it
* **[CONTENT-TODO.md](CONTENT-TODO.md)** — what to replace before going live
* **[assets/images/README.md](assets/images/README.md)** — photo slots and sizes

Run it: `python3 -m http.server 8000`

## 2. Vendored Claude Code skills

Vendored copies of Claude Code skills.

### Layout

```
.claude/skills/frontend-design/     # active skill — auto-discovered by Claude Code in this repo
├── SKILL.md
└── LICENSE.txt

.claude/skills/{banner-design,brand,design,design-system,slides,ui-styling,ui-ux-pro-max}/
                                     # active skills from the ui-ux-pro-max-skill plugin

.claude/skills/{taste-skill,taste-skill-v1,gpt-tasteskill,image-to-code-skill,
                imagegen-frontend-web,imagegen-frontend-mobile,brandkit,
                redesign-skill,soft-skill,output-skill,minimalist-skill,
                brutalist-skill,stitch-skill}/
                                     # active skills from the taste-skill plugin

plugins/frontend-design/            # verbatim mirror of the upstream plugin
├── .claude-plugin/plugin.json
├── skills/frontend-design/SKILL.md
├── README.md
└── LICENSE.txt

plugins/ui-ux-pro-max/              # verbatim mirror of the upstream plugin
├── .claude-plugin/plugin.json
├── skills/{banner-design,brand,design,design-system,slides,ui-styling,ui-ux-pro-max}/
├── README.md
└── LICENSE

plugins/taste-skill/                # verbatim mirror of the upstream plugin
├── .claude-plugin/plugin.json
├── skills/{taste-skill,taste-skill-v1,gpt-tasteskill,image-to-code-skill,
│           imagegen-frontend-web,imagegen-frontend-mobile,brandkit,
│           redesign-skill,soft-skill,output-skill,minimalist-skill,
│           brutalist-skill,stitch-skill}/, skills/llms.txt
├── README.md
└── LICENSE
```

`SKILL.md` is present in both trees for each skill. The `plugins/` copy preserves
the upstream plugin layout (including the `plugin.json` manifest, which is only
meaningful to the plugin marketplace). The `.claude/skills/` copy is what Claude
Code loads when working in this repository. Both are byte-identical to
upstream — update them together.

### What the skills do

**frontend-design** — Guides Claude toward distinctive, intentional visual
design when building or reshaping a UI: aesthetic direction, typography, and
choices that don't read as templated defaults. Claude picks it up
automatically for frontend work.

See `plugins/frontend-design/README.md` for usage examples.

**ui-ux-pro-max plugin** (7 skills: `banner-design`, `brand`, `design`,
`design-system`, `slides`, `ui-styling`, `ui-ux-pro-max`) — Design
intelligence for building and reviewing UI/UX: searchable local databases of
UI styles, color palettes, font pairings, chart types, icons, and UX
guidelines across 22 tech stacks, plus brand identity, design tokens, banner
design, and HTML slide/presentation generation. Claude picks these up
automatically for design and UI work.

See `plugins/ui-ux-pro-max/README.md` for usage examples. Note: the upstream
repository also ships an npm CLI installer, a Next.js marketing gallery, and
docs/example scaffolding used to build and publish the skill across multiple
AI platforms — only the skill payload (`.claude/skills/` + the plugin
manifest) is vendored here, per its own `CLAUDE.md`.

**taste-skill plugin** (13 skills) — "Anti-slop" frontend design taste
skills: stronger layout, typography, motion, and spacing instead of
boilerplate-looking AI UIs, plus image-generation skills for design
reference boards. Install names and jobs:

| Skill (folder) | Install name | Job |
| --- | --- | --- |
| `taste-skill` | `design-taste-frontend` | Default anti-slop skill (v2, experimental): brief inference, three tunable dials (variance/motion/density), design-system mapping, GSAP code skeletons, pre-flight checklist. |
| `taste-skill-v1` | `design-taste-frontend-v1` | Original v1, preserved for projects pinned to its exact behavior. |
| `gpt-tasteskill` | `gpt-taste` | Stricter variant tuned for GPT/Codex: higher layout variance, stronger GSAP direction. |
| `image-to-code-skill` | `image-to-code` | Generate design reference images first, analyze them, then implement the frontend to match. |
| `redesign-skill` | `redesign-existing-projects` | Audits an existing UI before fixing layout, spacing, and hierarchy. |
| `soft-skill` | `high-end-visual-design` | Polished, calm, premium UI with soft contrast and spring motion. |
| `output-skill` | `full-output-enforcement` | Stops the model shipping half-finished work or placeholder comments. |
| `minimalist-skill` | `minimalist-ui` | Editorial product UI (Notion/Linear style), restrained palette. |
| `brutalist-skill` | `industrial-brutalist-ui` | Hard mechanical language: Swiss type, sharp contrast. |
| `stitch-skill` | `stitch-design-taste` | Google Stitch-compatible design rules, with a `DESIGN.md` export format. |
| `imagegen-frontend-web` | `imagegen-frontend-web` | Image-generation only: website comps (hero, landing, multi-section). |
| `imagegen-frontend-mobile` | `imagegen-frontend-mobile` | Image-generation only: mobile screens and flows. |
| `brandkit` | `brandkit` | Image-generation only: brand-kit boards (logo directions, palettes, type). |

Claude picks the relevant one up automatically for frontend/design work; see
`plugins/taste-skill/README.md` for the full upstream usage guide. Note: the
upstream repository also ships marketing assets (`assets/`), background
research notes (`research/`), example renders (`examples/`), and README-build
scripts (`scripts/`) unrelated to skill behavior — only the skill payload
(`skills/` + the plugin manifest, `README.md`, `LICENSE`) is vendored here.

### Provenance

| | |
|---|---|
| Source | `anthropics/claude-code` @ `31a3b00bef145a0393d9dbf840a98674fec07712` |
| Path | `plugins/frontend-design/` |
| Plugin version | 1.1.0 |
| `SKILL.md` sha256 | `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3` |

| | |
|---|---|
| Source | `nextlevelbuilder/ui-ux-pro-max-skill` @ `15de38fb70bc80ae9276fa7703b48ae861a672e6` |
| Path | `.claude/skills/`, `.claude-plugin/plugin.json` |
| Plugin version | 2.13.0 |
| `ui-ux-pro-max/SKILL.md` sha256 | `ea087c341bfb5b23195c7302027268ede86da802554c18a5c4896a6017b439f9` |

| | |
|---|---|
| Source | `Leonxlnx/taste-skill` @ `e79ca9ec7e071eb3a3b623c4fb752e853fc3ed58` |
| Path | `skills/`, `.claude-plugin/plugin.json` |
| Plugin version | 1.0.0 |
| `taste-skill/SKILL.md` sha256 | `aa194351b246b8b4799099d4ed7b033d29eab6e6e3d58d8d2172978be7b3ec89` |

### License

`frontend-design`: © Anthropic PBC. All rights reserved. Use is subject to
Anthropic's [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).

`ui-ux-pro-max` and its bundled skills: MIT License, © 2024 Next Level
Builder. See `plugins/ui-ux-pro-max/LICENSE`.

`taste-skill` and its bundled skills: MIT License, © 2026 Leonxlnx. See
`plugins/taste-skill/LICENSE`.
