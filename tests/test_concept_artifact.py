"""Contract tests for ALEXARAC's current concept/specification artifact.

These checks validate the present design deliverable, not a shipped app or
measured engineering claims.
"""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AlexaracConceptArtifactTests(unittest.TestCase):
    def test_expected_design_artifacts_are_present(self) -> None:
        for relative in ("README.md", "BOM_MAP.md", "LICENSE"):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_readme_identifies_concept_stage_and_missing_runtime(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("design artifact, not a complete deployed web application", readme)
        self.assertIn("design / concept stage", readme)
        self.assertIn("does not contain that application implementation", readme)
        self.assertIn("no backend or external-service integration is shipped", readme)

    def test_bom_preserves_major_concept_areas(self) -> None:
        bom = (ROOT / "BOM_MAP.md").read_text(encoding="utf-8")
        for section in (
            "EarthDome Construction",
            "LED Amphitheater",
            "369 Vortex Water Wheel Cascade",
            "GRAPALACLAWZ Robotics",
            "Fleet Command",
            "Aethel Grid — Sensor Network",
            "Colony Infrastructure",
        ):
            with self.subTest(section=section):
                self.assertIn(section, bom)

    def test_bom_refuses_to_fabricate_pricing(self) -> None:
        bom = (ROOT / "BOM_MAP.md").read_text(encoding="utf-8").lower()
        self.assertIn("no fabricated pricing", bom)
        self.assertIn("costs tbd pending real supplier quotes", bom)
        self.assertIn("no prices listed", bom)

    def test_bom_requires_engineering_and_code_review(self) -> None:
        bom = (ROOT / "BOM_MAP.md").read_text(encoding="utf-8").lower()
        self.assertIn("subject to final engineering", bom)
        self.assertIn("local code review", bom)
        self.assertIn("site conditions", bom)
        self.assertIn("before procurement", bom)

    def test_current_tree_does_not_claim_an_application_file_exists(self) -> None:
        self.assertFalse((ROOT / "index.html").exists())
        self.assertFalse((ROOT / "src").exists())
        self.assertFalse((ROOT / "backend").exists())


if __name__ == "__main__":
    unittest.main()
