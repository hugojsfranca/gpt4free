import unittest

from gpt4free.figma_mcp.optimizer import PromptBudget, build_compact_skill_prompt, compress_figma_payload
from gpt4free.figma_mcp.server import FigmaMCPServer
from gpt4free.figma_mcp.skills import SKILLS, SkillName


class FakeFigmaClient:
    def get_file(self, file_key: str):
        return {
            "name": "Checkout Flows",
            "lastModified": "2026-03-10",
            "styles": {"1": {}, "2": {}},
            "components": {"a": {}, "b": {}, "c": {}},
            "document": {
                "id": "0:1",
                "name": "Root",
                "type": "DOCUMENT",
                "children": [{"id": str(i), "name": f"Frame {i}"} for i in range(100)],
            },
        }


class TestFigmaMCP(unittest.TestCase):
    def test_prompt_is_compact(self):
        prompt = build_compact_skill_prompt(
            [SKILLS[SkillName.VISUAL_DESIGN], SKILLS[SkillName.ACCESSIBILITY]],
            PromptBudget(max_chars=250, max_checks_per_skill=1),
        )
        self.assertLessEqual(len(prompt), 250)
        self.assertIn("[visual_design]", prompt)

    def test_payload_compression_reduces_nodes(self):
        payload = FakeFigmaClient().get_file("abc")
        compressed = compress_figma_payload(payload, max_nodes=5)
        self.assertEqual(len(compressed["document"]["children"]), 5)
        self.assertTrue(compressed["payload_reduced"])

    def test_server_analysis_output_shape(self):
        server = FigmaMCPServer(figma_client=FakeFigmaClient())
        result = server.tool_analyze_file(
            file_key="file_1",
            skills=["visual_design", "design_review", "documentation"],
        )
        self.assertEqual(result["file_key"], "file_1")
        self.assertEqual(result["selected_skills"][0], "visual_design")
        self.assertIn("token_strategy", result)


if __name__ == "__main__":
    unittest.main()
