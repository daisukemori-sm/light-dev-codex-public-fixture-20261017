import unittest

from policy import can_cancel


class Finding1(unittest.TestCase):
    def test_finding_1_pending_non_owner_cannot_cancel(self):
        self.assertIs(can_cancel("pending", "alice", "bob"), False)
