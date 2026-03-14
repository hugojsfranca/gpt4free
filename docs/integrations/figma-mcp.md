# Figma MCP integration (standalone)

This repository now keeps Figma MCP work under `integrations/figma_mcp` instead of the core `gpt4free` package.

## Why this location

- `gpt4free/` is reserved for model provider and completion logic.
- `integrations/` is the place for external tool servers and platform adapters.
- This keeps architecture clean and makes future extraction into a dedicated repo easier.

## Modules

- `integrations/figma_mcp/server.py`: MCP-style tool surface.
- `integrations/figma_mcp/skills.py`: skill definitions for design analysis.
- `integrations/figma_mcp/optimizer.py`: prompt/payload token optimization.

## Current scope

The integration includes skill packs for:
- visual design
- user experience
- accessibility
- compatibility with different tech languages/frameworks
- design review
- documentation
- AI-ready design systems
