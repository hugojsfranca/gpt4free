from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List


class SkillName(str, Enum):
    VISUAL_DESIGN = "visual_design"
    USER_EXPERIENCE = "user_experience"
    ACCESSIBILITY = "accessibility"
    COMPATIBILITY = "compatibility"
    DESIGN_REVIEW = "design_review"
    DOCUMENTATION = "documentation"
    AI_READY_DESIGN_SYSTEMS = "ai_ready_design_systems"


@dataclass(frozen=True)
class SkillDefinition:
    name: SkillName
    objective: str
    checks: List[str]
    output_shape: List[str]


SKILLS: Dict[SkillName, SkillDefinition] = {
    SkillName.VISUAL_DESIGN: SkillDefinition(
        name=SkillName.VISUAL_DESIGN,
        objective="Evaluate hierarchy, spacing rhythm, typography and color contrast consistency.",
        checks=[
            "Detect inconsistent typography tokens",
            "Find spacing scale drift",
            "Flag color usage outside approved styles",
        ],
        output_shape=["summary", "top_issues", "suggested_tokens"],
    ),
    SkillName.USER_EXPERIENCE: SkillDefinition(
        name=SkillName.USER_EXPERIENCE,
        objective="Review information architecture and task completion friction.",
        checks=[
            "Map primary user flows",
            "Spot high-friction transitions",
            "Identify missing feedback states",
        ],
        output_shape=["flow_risks", "usability_fixes", "confidence"],
    ),
    SkillName.ACCESSIBILITY: SkillDefinition(
        name=SkillName.ACCESSIBILITY,
        objective="Validate inclusive design choices against core WCAG checkpoints.",
        checks=[
            "Text/background contrast check",
            "Touch target size and spacing",
            "Focus order and semantic labeling hints",
        ],
        output_shape=["wcag_failures", "severity", "fix_plan"],
    ),
    SkillName.COMPATIBILITY: SkillDefinition(
        name=SkillName.COMPATIBILITY,
        objective="Translate design intent to multiple front-end stacks safely.",
        checks=[
            "Map tokens to CSS/Tailwind/native variables",
            "Identify implementation ambiguities",
            "Produce framework-neutral specs",
        ],
        output_shape=["token_map", "stack_notes", "handoff_contract"],
    ),
    SkillName.DESIGN_REVIEW: SkillDefinition(
        name=SkillName.DESIGN_REVIEW,
        objective="Create concise design review with priority-ranked issues.",
        checks=[
            "Cluster duplicate issues",
            "Score impact and effort",
            "Recommend next sprint actions",
        ],
        output_shape=["review_summary", "p0_p1_p2", "next_actions"],
    ),
    SkillName.DOCUMENTATION: SkillDefinition(
        name=SkillName.DOCUMENTATION,
        objective="Generate concise component docs and usage guardrails.",
        checks=[
            "Document component intent",
            "Capture do/don't examples",
            "Track variants and states",
        ],
        output_shape=["component_docs", "usage_rules", "open_questions"],
    ),
    SkillName.AI_READY_DESIGN_SYSTEMS: SkillDefinition(
        name=SkillName.AI_READY_DESIGN_SYSTEMS,
        objective="Structure design system metadata for agent-ready automation.",
        checks=[
            "Normalize naming and taxonomy",
            "Bind tokens to machine-readable schema",
            "Define safe generation constraints",
        ],
        output_shape=["schema", "automation_rules", "governance"],
    ),
}


def resolve_skills(skill_names: Iterable[str]) -> List[SkillDefinition]:
    resolved: List[SkillDefinition] = []
    for raw_name in skill_names:
        key = SkillName(raw_name)
        resolved.append(SKILLS[key])
    return resolved
