# gknilaynew

Vendored copy of the **frontend-design** skill from
[anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design).

## Layout

```
.claude/skills/frontend-design/     # active skill — auto-discovered by Claude Code in this repo
├── SKILL.md
└── LICENSE.txt

plugins/frontend-design/            # verbatim mirror of the upstream plugin
├── .claude-plugin/plugin.json
├── skills/frontend-design/SKILL.md
├── README.md
└── LICENSE.txt
```

`SKILL.md` is present in both trees. The `plugins/` copy preserves the upstream
plugin layout (including the `plugin.json` manifest, which is only meaningful to
the plugin marketplace). The `.claude/skills/` copy is the one Claude Code loads
when working in this repository. Both are byte-identical to upstream — update
them together.

## What the skill does

Guides Claude toward distinctive, intentional visual design when building or
reshaping a UI: aesthetic direction, typography, and choices that don't read as
templated defaults. Claude picks it up automatically for frontend work.

See `plugins/frontend-design/README.md` for usage examples.

## Provenance

| | |
|---|---|
| Source | `anthropics/claude-code` @ `31a3b00bef145a0393d9dbf840a98674fec07712` |
| Path | `plugins/frontend-design/` |
| Plugin version | 1.1.0 |
| `SKILL.md` sha256 | `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3` |

## License

© Anthropic PBC. All rights reserved. Use is subject to Anthropic's
[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
