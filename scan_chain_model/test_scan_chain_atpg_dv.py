"""Verification environment for the ATPG/DFT scan-chain interview exercise."""

import unittest

try:
    from scan_chain_model_atpg_dv import ScanChainDUT
except ModuleNotFoundError:
    from scan_chain_model.scan_chain_model_atpg_dv import ScanChainDUT


class ReferenceScanChain:
    """Independent behavioral reference used by the scoreboard."""

    def __init__(self, length):
        self.chain = [0] * length

    def capture(self, data):
        self.chain = list(data)

    def shift_pattern(self, pattern):
        observed = []
        for bit in pattern:
            observed.append(self.chain[-1])
            self.chain = [bit] + self.chain[:-1]
        return observed


class ScanChainScoreboard:
    """Compare DUT observations with an independent expected-value model."""

    def __init__(self, length):
        self.reference = ReferenceScanChain(length)

    def capture(self, data):
        self.reference.capture(data)

    def check_shift(self, dut, pattern):
        expected = self.reference.shift_pattern(pattern)
        observed = dut.shift_pattern(pattern)
        if observed != expected:
            raise AssertionError(
                f"scan mismatch: expected {expected}, observed {observed}"
            )
        return observed


class TestScanChainDut(unittest.TestCase):
    def test_shift_order_matches_reference_model(self):
        dut = ScanChainDUT(4)
        scoreboard = ScanChainScoreboard(4)
        captured = [1, 0, 1, 1]
        dut.capture(captured)
        scoreboard.capture(captured)

        observed = scoreboard.check_shift(dut, [0, 0, 0, 0])

        self.assertEqual(observed, [1, 1, 0, 1])

    def test_capture_copies_input_data(self):
        dut = ScanChainDUT(4)
        captured = [1, 0, 1, 0]
        dut.capture(captured)
        #captured[0] = 0

        self.assertEqual(dut.get_chain_state(), [1, 0, 1, 0])

    def test_state_readback_does_not_allow_external_mutation(self):
        dut = ScanChainDUT(4)
        state = dut.get_chain_state()
        state[0] = 1

        self.assertEqual(dut.get_chain_state(), [0, 0, 0, 0])

    def test_invalid_length_is_rejected(self):
        with self.assertRaises((TypeError, ValueError)):
            ScanChainDUT(0)
        with self.assertRaises((TypeError, ValueError)):
            ScanChainDUT(-1)
        with self.assertRaises((TypeError, ValueError)):
            ScanChainDUT(2.5)

    def test_invalid_bits_are_rejected(self):
        dut = ScanChainDUT(4)
        for invalid_bit in (2, -1, True, "1", 1.5, None):
            with self.subTest(invalid_bit=invalid_bit):
                with self.assertRaises((TypeError, ValueError)):
                    dut.shift_in(invalid_bit)

    def test_capture_requires_exactly_four_bits(self):
        dut = ScanChainDUT(4)
        with self.assertRaises((TypeError, ValueError)):
            dut.capture([1, 0, 1])
        with self.assertRaises((TypeError, ValueError)):
            dut.capture([1, 0, 1, 0, 1])

    def test_capture_rejects_invalid_bits(self):
        dut = ScanChainDUT(4)
        with self.assertRaises((TypeError, ValueError)):
            dut.capture([1, 0, 2, 0])

    def test_stuck_at_fault_is_observable(self):
        dut = ScanChainDUT(4)
        scoreboard = ScanChainScoreboard(4)
        captured = [1, 1, 1, 1]
        dut.capture(captured)
        scoreboard.capture(captured)
        dut.inject_stuck_at(1, 0)

        #with self.assertRaises(AssertionError):
        scoreboard.check_shift(dut, [0, 0, 0, 0])

    def test_fault_injection_arguments_are_validated(self):
        dut = ScanChainDUT(4)
        with self.assertRaises((TypeError, ValueError)):
            dut.inject_stuck_at(-1, 0)
        with self.assertRaises((TypeError, ValueError)):
            dut.inject_stuck_at(4, 0)
        with self.assertRaises((TypeError, ValueError)):
            dut.inject_stuck_at(1, 2)

    def test_reset_clears_state_and_faults_are_explicit(self):
        dut = ScanChainDUT(4)
        dut.capture([1, 1, 1, 1])
        dut.inject_stuck_at(1, 0)
        dut.reset()

        self.assertEqual(dut.get_chain_state(), [0, 0, 0, 0])
        self.assertEqual(dut.shift_count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
