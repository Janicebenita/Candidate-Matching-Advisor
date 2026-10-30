import unittest
from agent import compare_candidate


class CandidateTests(unittest.TestCase):
    def test_missing_skill_is_reported(self):
        result = compare_candidate({"required_skills": ["Python", "SQL"]}, {"skills": ["Python"]})
        self.assertEqual(result["missing_skills"], ["sql"])
        self.assertTrue(result["recruiter_review_required"])


if __name__ == "__main__":
    unittest.main()
