from dataclasses import dataclass
from typing import Dict, List

from .skills import SkillDefinition


@dataclass(frozen=True)
class PromptBudget:
    max_chars: int = 2200
    max_checks_per_skill: int = 2


def _trim_line(line: str, max_len: int = 180) -> str:
    if len(line) <= max_len:
        return line
    return line[: max_len - 1].rstrip() + "…"


def build_compact_skill_prompt(skills: List[SkillDefinition], budget: PromptBudget) -> str:
    lines: List[str] = [
        "You are a Figma MCP analysis engine. Return compact JSON only.",
        "Avoid repeated text and include only actionable outputs.",
    ]

    for skill in skills:
        checks = skill.checks[: budget.max_checks_per_skill]
        lines.append(f"[{skill.name.value}] obj={_trim_line(skill.objective)}")
        lines.append("checks=" + "; ".join(_trim_line(item, 110) for item in checks))
        lines.append("out=" + ",".join(skill.output_shape))

    prompt = "\n".join(lines)
    return _trim_line(prompt, budget.max_chars)


def compress_figma_payload(figma_payload: Dict, max_nodes: int = 60) -> Dict:
    document = figma_payload.get("document", {})
    children = document.get("children", [])
    trimmed_children = children[:max_nodes]

    return {
        "name": figma_payload.get("name"),
        "lastModified": figma_payload.get("lastModified"),
        "styles_count": len(figma_payload.get("styles", {})),
        "components_count": len(figma_payload.get("components", {})),
        "document": {
            "id": document.get("id"),
            "name": document.get("name"),
            "type": document.get("type"),
            "children": trimmed_children,
        },
        "payload_reduced": len(children) > len(trimmed_children),
    }
