"""
Scan Chain Implementation (Buggy Version for Phone Screen)
This version contains intentional bugs and design flaws for candidates to find.
"""
import unittest

class ScanChain:
    def __init__(self, length):
        self.length = length
        self.chain = [0] * length
        self.shift_count = 0
    
    def shift_in(self, bit):
        """Shift in a single bit from the input"""
        # BUG 2: No input validation - what if bit is not 0 or 1?
        # BUG 7: Using pop/insert is inefficient and modifies list in place
        self.chain.pop()
        self.chain.insert(0, bit)
        self.shift_count += 1
    
    def shift_pattern(self, pattern):
        """Shift in a complete pattern"""
        # BUG 5: No validation of pattern length or content
        # BUG 8: What if pattern is None or not iterable?
        for bit in pattern:
            self.shift_in(bit)
    
    def capture(self, data):
        """Capture data into scan chain"""
        #if self.length != len(data):            
        #    raise Exception("Data length must match chain length")
        # BUG 3: No length validation - data could be wrong size
        # BUG 6: Direct assignment breaks encapsulation
        # BUG 4: shift_count not reset, causing inconsistent state
        self.chain = data
    
    def get_output(self):
        """Get the current output bit"""
        # BUG 1: No check if chain is empty
        return self.chain[-1]
    
    def get_chain_state(self):
        """Get entire chain state"""
        # Return a copy to prevent external modification of internal state
        return self.chain.copy()
    
    def reset(self):
        """Reset the chain"""
        self.chain = [0] * self.length
        self.shift_count = 0


# Example usage (also has issues)
if __name__ == "__main__":
    # Create a 4-bit scan chain
    sc = ScanChain(4)
    
    # Shift in some bits
    sc.shift_in(1)
    sc.shift_in(0)
    sc.shift_in(1)
    sc.shift_in(1)
    
    print(f"Chain state: {sc.get_chain_state()}")
    print(f"Output bit: {sc.get_output()}")
    print(f"Shift count: {sc.shift_count}")
