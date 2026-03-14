from typing import Dict, Iterable, Optional

from .optimizer import PromptBudget, build_compact_skill_prompt, compress_figma_payload
from .skills import resolve_skills


class FigmaClientProtocol:
    """Minimal protocol for plugging in a real Figma API client."""

    def get_file(self, file_key: str) -> Dict:
        raise NotImplementedError


class FigmaMCPServer:
    """Small MCP-style tool surface optimized for low token usage."""

    def __init__(self, figma_client: FigmaClientProtocol, budget: Optional[PromptBudget] = None) -> None:
        self.figma_client = figma_client
        self.budget = budget or PromptBudget()

    def tool_list_skills(self) -> Dict:
        return {
            "skills": [
                "visual_design",
                "user_experience",
                "accessibility",
                "compatibility",
                "design_review",
                "documentation",
                "ai_ready_design_systems",
            ]
        }

    def tool_analyze_file(self, file_key: str, skills: Iterable[str]) -> Dict:
        selected_skills = resolve_skills(skills)
        figma_file = self.figma_client.get_file(file_key)
        compact_payload = compress_figma_payload(figma_file)
        analysis_prompt = build_compact_skill_prompt(selected_skills, self.budget)

        return {
            "file_key": file_key,
            "selected_skills": [skill.name.value for skill in selected_skills],
            "analysis_prompt": analysis_prompt,
            "compact_payload": compact_payload,
            "token_strategy": {
                "max_chars": self.budget.max_chars,
                "max_checks_per_skill": self.budget.max_checks_per_skill,
                "payload_reduction_enabled": True,
            },
        }
