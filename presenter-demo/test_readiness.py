import unittest

from readiness import release_state


class ReadinessTests(unittest.TestCase):
    def test_all_passed(self):
        self.assertEqual(release_state(["passed", "passed"]), "ready")

    def test_failed_check(self):
        self.assertEqual(release_state(["passed", "failed"]), "not_ready")

    def test_pending_check(self):
        self.assertEqual(release_state(["passed", "pending"]), "not_ready")

    def test_unknown_status(self):
        with self.assertRaises(ValueError):
            release_state(["unknown"])

    def test_preserves_input(self):
        checks = ["passed", "pending"]
        release_state(checks)
        self.assertEqual(checks, ["passed", "pending"])


if __name__ == "__main__":
    unittest.main()
