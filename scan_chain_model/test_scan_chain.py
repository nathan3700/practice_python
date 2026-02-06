"""
Test Suite for Scan Chain Implementation
Demonstrates bugs in original code.
"""

import unittest
from scan_chain_model import ScanChain as ScanChain


class TestImplementation(unittest.TestCase):
    """Tests that should FAIL when bugs are present in the implementation"""

    def test_bug_empty_chain_output(self):
        """BUG 1:get_output should handle empty chain gracefully"""
        sc = ScanChain(0)
        # Should work for initialized chain
        output = sc.get_output()
        self.assertIn(output, [0, 1], "get_output should return valid bit")

    
    def test_bug_invalid_bit_input(self):
        """BUG 2: No validation of bit input - should raise error for invalid values"""
        sc = ScanChain(4)
        # These should raise errors but buggy version accepts them
        with self.assertRaises(Exception):
            sc.shift_in(5)  # Invalid bit value
        with self.assertRaises(Exception):
            sc.shift_in("1")  # String instead of int
        with self.assertRaises(Exception):
            sc.shift_in(1.5)  # Float instead of int
    
    
    def test_bug_capture_wrong_length(self):
        """BUG 3: capture should validate data length matches chain length"""
        sc = ScanChain(4)
        # Should raise errors for wrong length but buggy version doesn't validate
        with self.assertRaises(Exception):
            sc.capture([1, 0, 1])  # Too short
        with self.assertRaises(Exception):
            sc.capture([1, 0, 1, 1, 0, 1])  # Too long
    
    def test_bug_capture_inconsistent_state(self):
        """BUG 4: shift_count should be reset on capture"""
        sc = ScanChain(4)
        sc.shift_in(1)
        sc.shift_in(1)
        self.assertEqual(sc.shift_count, 2)
        
        sc.capture([0, 0, 0, 0])
        # shift_count should be reset to 0 (but isn't in buggy version)
        self.assertEqual(sc.shift_count, 0, 
                        "shift_count should be reset to 0 after capture")
        
    def test_bug_invalid_pattern_content(self):
        """BUG 5: shift_pattern should validate pattern contains only 0s and 1s"""
        sc = ScanChain(4)
        # Should raise error for invalid bit values in pattern
        with self.assertRaises(Exception):
            sc.shift_pattern([1, 0, 5, 1])  # Contains invalid bit value
        with self.assertRaises(Exception):
            sc.shift_pattern([1, "0", 1, 0])  # Contains string
    
    
    def test_bug_capture_invalid_data(self):
        """BUG 3 & 6: capture should validate data contains only 0s and 1s"""
        sc = ScanChain(4)
        # Should raise error for invalid bit values
        with self.assertRaises(Exception):
            sc.capture([1, 0, 5, 1])  # Contains invalid bit value
        with self.assertRaises(Exception):
            sc.capture([1, "0", 1, 0])  # Contains string


if __name__ == "__main__":
    print("Running Scan Chain Test Suite for Buggy Implementation\n")
    unittest.main(verbosity=2)
