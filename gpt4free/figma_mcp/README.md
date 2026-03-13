# Figma MCP (Token-Efficient Skill Pack)

This module provides a lightweight MCP-style server layer for Figma workflows focused on:

- Visual Design
- User Experience
- Accessibility
- Compatibility across tech stacks
- Design Review
- Documentation
- AI-ready design systems

## Why this is lower-token

- Shrinks Figma payload to a compact subset (`compress_figma_payload`)
- Limits checks per skill (`max_checks_per_skill`)
- Generates concise response contract (`build_compact_skill_prompt`)

## Example

```python
from gpt4free.figma_mcp import FigmaMCPServer

server = FigmaMCPServer(figma_client=your_client)
result = server.tool_analyze_file(
    file_key="abc123",
    skills=["visual_design", "accessibility", "documentation"],
)
```

You can wire `result["analysis_prompt"]` into your preferred model runner.
