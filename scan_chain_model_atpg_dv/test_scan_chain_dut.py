"""Part 2 starter: black-box verification tests for ScanChainDUT.

Use only the public interface documented in ScanChainDUT. Do not inspect its
source, private attributes, or undocumented constants.
"""

import unittest

try:
    from scan_chain_dut_example1 import ScanChainDUT
except ImportError:
    from scan_chain_model_atpg_dv.scan_chain_dut_example1 import ScanChainDUT


class TestScanChainDutBlackBox(unittest.TestCase):
    def test_placeholder(self):
        # Replace with real black-box checks against ScanChainDUT.
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
