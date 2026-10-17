import unittest
from policy import can_cancel
from summary import status_label
class Base(unittest.TestCase):
    def test_approved_stays_closed(self): self.assertFalse(can_cancel('approved','alice','alice'))
    def test_unknown_label_is_preserved(self): self.assertEqual(status_label('unknown'),'unknown')
