# gknilaynew

Vendored copies of Claude Code skills.

## Layout

```
.claude/skills/frontend-design/     # active skill — auto-discovered by Claude Code in this repo
├── SKILL.md
└── LICENSE.txt

.claude/skills/{banner-design,brand,design,design-system,slides,ui-styling,ui-ux-pro-max}/
                                     # active skills from the ui-ux-pro-max-skill plugin

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
```

`SKILL.md` is present in both trees for each skill. The `plugins/` copy preserves
the upstream plugin layout (including the `plugin.json` manifest, which is only
meaningful to the plugin marketplace). The `.claude/skills/` copy is what Claude
Code loads when working in this repository. Both are byte-identical to
upstream — update them together.

## What the skills do

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

## Provenance

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

## License

`frontend-design`: © Anthropic PBC. All rights reserved. Use is subject to
Anthropic's [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).

`ui-ux-pro-max` and its bundled skills: MIT License, © 2024 Next Level
Builder. See `plugins/ui-ux-pro-max/LICENSE`.
