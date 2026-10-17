import unittest

from summary import status_label


class StatusLabels(unittest.TestCase):
    def test_known_statuses_have_japanese_labels(self):
        for status, expected in (
            ("pending", "申請中"),
            ("approved", "承認済み"),
            ("cancelled", "取り消し済み"),
        ):
            with self.subTest(status=status):
                self.assertEqual(status_label(status), expected)
