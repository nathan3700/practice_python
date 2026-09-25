"""Starter DUT model for an ATPG/DFT verification interview exercise.

The model is intentionally incomplete. Candidates should use the accompanying
verification environment to identify and correct behavioral defects.
"""


class ScanChainDUT:
    """Small scan-chain DUT with optional stuck-at fault injection."""

    def __init__(self, length):
        self.length = length
        self.chain = [0] * length
        self.shift_count = 0
        self.stuck_at = {}

    def shift_in(self, bit):
        """Shift one bit in and return the bit shifted out."""
        shifted_out = self.chain[-1]
        self.chain.insert(0, bit)
        self.chain.pop()
        self.shift_count += 1
        self._apply_faults()
        return shifted_out

    def shift_pattern(self, pattern):
        """Shift a sequence of bits and return the observed output sequence."""
        return [self.shift_in(bit) for bit in pattern]

    def capture(self, data):
        """Load a parallel response into the scan cells."""
        self.chain = data
        self.shift_count = 0

    def reset(self):
        """Return the DUT to its reset state."""
        self.chain = [0] * self.length
        self.shift_count = 0

    def get_output(self):
        """Return the value at the scan-output side of the chain."""
        return self.chain[-1]

    def get_chain_state(self):
        """Return the current chain state."""
        return self.chain.copy()

    def inject_stuck_at(self, position, value):
        """Force a cell to zero or one after a shift operation."""
        self.stuck_at[position] = value

    def clear_faults(self):
        """Remove all injected faults."""
        self.stuck_at.clear()

    def _apply_faults(self):
        for position, value in self.stuck_at.items():
            self.chain[position] = value
