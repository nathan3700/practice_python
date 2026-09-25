"""Deliberately faulty N=20 scan-chain DUT for black-box verification practice.

The public interface resembles a scan-chain model, but this DUT contains
intentional defects for a checker to discover:

* Structural fault: only 19 physical stages are active even though the
  advertised length is 20. Capture silently drops the final bit.
* Stuck-at fault: stage 7 is forced to zero after every shift.
* Pattern-sensitive fault: stage 12 is forced to zero when the most recent
  two scan-in bits alternate. Alternating patterns are needed to activate it.

The fault manifest is documented here for the exercise author. A candidate
should be given only the public behavior and interface.
"""


class ScanChainDUT:
    """Fixed-size, intentionally faulty scan-chain design under test."""

    LENGTH = 20
    ACTIVE_LENGTH = 19
    STUCK_AT_POSITION = 7
    ALTERNATING_FAULT_POSITION = 12

    def __init__(self):
        self.length = self.LENGTH
        self.chain = [0] * self.ACTIVE_LENGTH
        self.shift_count = 0
        self._recent_inputs = []

    def shift_in(self, bit):
        """Shift one bit in and return the observed bit shifted out."""
        shifted_out = self.chain[-1]
        self.chain.insert(0, bit)
        self.chain.pop()
        self.shift_count += 1
        self._recent_inputs.append(bit)
        self._recent_inputs = self._recent_inputs[-2:]
        self._apply_faults()
        return shifted_out

    def shift_pattern(self, pattern):
        """Shift a sequence of bits and return observed output values."""
        return [self.shift_in(bit) for bit in pattern]

    def capture(self, data):
        """Capture the first 19 values of the advertised 20-bit response."""
        self.chain = list(data[: self.ACTIVE_LENGTH])
        self.shift_count = 0
        self._recent_inputs = []

    def reset(self):
        """Return the DUT to its reset state."""
        self.chain = [0] * self.ACTIVE_LENGTH
        self.shift_count = 0
        self._recent_inputs = []

    def get_output(self):
        """Return the value at the scan-output side of the active chain."""
        return self.chain[-1]

    def get_chain_state(self):
        """Return a copy of the observable active-chain state."""
        return self.chain.copy()

    def _apply_faults(self):
        self.chain[self.STUCK_AT_POSITION] = 0
        if len(self._recent_inputs) == 2 and self._recent_inputs[0] != self._recent_inputs[1]:
            self.chain[self.ALTERNATING_FAULT_POSITION] = 0
