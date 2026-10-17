import unittest

from policy import can_cancel


class CancelPolicy(unittest.TestCase):
    def test_pending_owner_can_cancel(self):
        for identity in ("alice", "bob"):
            with self.subTest(identity=identity):
                self.assertIs(can_cancel("pending", identity, identity), True)

    def test_status_identity_matrix(self):
        allowed_pairs = {("alice", "alice"), ("bob", "bob")}
        for status in ("pending", "approved", "unknown", ""):
            for owner in ("alice", "bob", ""):
                for actor in ("alice", "bob", ""):
                    with self.subTest(status=status, owner=owner, actor=actor):
                        expected = (owner, actor) in allowed_pairs if status == "pending" else False
                        self.assertIs(can_cancel(status, owner, actor), expected)
