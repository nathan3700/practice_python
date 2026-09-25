"""Verification environment for the ATPG/DFT scan-chain interview exercise."""

import unittest

try:
    from generic_scan_chain import GenericScanChain
except ImportError:
    from scan_chain_model_atpg_dv.generic_scan_chain import GenericScanChain


class TestScanChainDut(unittest.TestCase):
    def test_bug_invalid_length_accepted(self):
        """BUG: constructor should reject non-positive length."""
        with self.assertRaises((TypeError, ValueError)):
            GenericScanChain(0)

    def test_bug_invalid_bit_value_accepted(self):
        """BUG: shift_in should reject values other than 0 and 1."""
        dut = GenericScanChain(4)
        with self.assertRaises((TypeError, ValueError)):
            dut.shift_in(5)

    def test_shift_order_matches_reference_model(self):
        dut = GenericScanChain(4)
        captured = [1, 0, 1, 1]
        dut.capture(captured)

        observed = dut.shift_pattern([0, 0, 0, 0])

        self.assertEqual(observed, [1, 1, 0, 1])

    def test_state_readback_does_not_allow_external_mutation(self):
        dut = GenericScanChain(4)
        state = dut.get_chain_state()
        state[0] = 1

        self.assertEqual(dut.get_chain_state(), [0, 0, 0, 0])

    def test_stuck_at_fault_is_observable(self):
        dut = GenericScanChain(4)
        captured = [1, 1, 1, 1]
        dut.capture(captured)
        dut.inject_stuck_at(1, 0)

        observed = dut.shift_pattern([0, 0, 0, 0])
        expected = [1, 1, 1, 1]

        self.assertNotEqual(
            observed,
            expected,
            "the injected stuck-at fault should change the observed response",
        )

    def test_reset_clears_state_and_faults_are_explicit(self):
        dut = GenericScanChain(4)
        dut.capture([1, 1, 1, 1])
        dut.inject_stuck_at(1, 0)
        dut.reset()

        self.assertEqual(dut.get_chain_state(), [0, 0, 0, 0])
        self.assertEqual(dut.shift_count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
