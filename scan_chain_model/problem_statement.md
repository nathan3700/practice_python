# DFT Phone Screen Coding Problem: Scan Chain Analyzer

## Background
In Design For Test (DFT), scan chains are critical for testing digital circuits. A scan chain is a series of flip-flops connected together to form a shift register, allowing test patterns to be shifted in and responses to be shifted out.

## Problem Statement
You are provided with a partially implemented `ScanChain` class that simulates a basic scan chain with the following features:
- Shift operations (shift in test data)
- Capture operations (capture circuit state)
- Basic chain integrity checking

Your task is to:
1. **Analyze** the provided code and identify potential bugs, edge cases, and design weaknesses
2. **Refactor** the code to improve its object-oriented design and maintainability
3. **Extend** the implementation with additional functionality (see requirements below)
4. **Test** your implementation by creating test cases that expose weaknesses in the original design

## Initial Code (Python)

```python
class ScanChain:
    def __init__(self, length):
        self.length = length
        self.chain = [0] * length
        self.shift_count = 0
    
    def shift_in(self, bit):
        # Shift in a single bit
        self.chain.pop()
        self.chain.insert(0, bit)
        self.shift_count += 1
    
    def shift_pattern(self, pattern):
        # Shift in a complete pattern
        for bit in pattern:
            self.shift_in(bit)
    
    def capture(self, data):
        # Capture data into scan chain
        self.chain = data
    
    def get_output(self):
        # Get the current output bit
        return self.chain[-1]
    
    def get_chain_state(self):
        # Get entire chain state
        return self.chain
    
    def reset(self):
        # Reset the chain
        self.chain = [0] * self.length
        self.shift_count = 0
```

## Requirements

### Part 1: Analysis (15 minutes)
Identify and document:
- At least 3 bugs or potential issues in the code
- At least 2 design weaknesses or missing validations
- Edge cases that could cause problems

### Part 2: Refactoring (20 minutes)
Refactor the code to:
- Fix identified bugs
- Add proper input validation
- Improve error handling
- Make the design more robust and maintainable
- Add appropriate documentation

### Part 3: Extension (15 minutes)
Add the following features:
1. **Compression Support**: Implement a simple scan compression scheme where multiple scan chains can be XOR'd together to reduce test time
2. **Stuck-at Fault Detection**: Add a method to detect if any bit position appears to be stuck at 0 or 1 based on shift history
3. **Chain Integrity Check**: Implement a method that can verify scan chain integrity by shifting a known pattern and checking the output

### Part 4: Testing (10 minutes)
Create test cases that:
- Demonstrate the bugs you found in the original code
- Verify your fixes work correctly
- Test edge cases and boundary conditions
- Validate the new features

## Evaluation Criteria
- **Analysis Skills**: Ability to identify real issues and weaknesses
- **Code Quality**: Clean, readable, well-documented code
- **OOP Design**: Proper use of encapsulation, abstraction, and design patterns
- **Testing Mindset**: Comprehensive test coverage and edge case handling
- **DFT Knowledge**: Understanding of scan chain concepts (bonus, not required)

## Deliverables
1. A document listing identified issues and design weaknesses
2. Refactored `ScanChain` class with improvements
3. Extended implementation with new features
4. Test suite demonstrating your work

## Time Allocation
Total: 60 minutes
- Part 1: 15 minutes
- Part 2: 20 minutes
- Part 3: 15 minutes
- Part 4: 10 minutes

## Notes for Interviewer
- The initial code has intentional bugs and design flaws
- Look for candidates who question assumptions and validate inputs
- Strong candidates will consider thread safety, performance, and extensibility
- The compression and fault detection features test algorithmic thinking
- Candidates familiar with DFT may recognize real-world scenarios, but this is not required

## Hints (provide if candidate gets stuck)
- Consider what happens with invalid inputs
- Think about data type consistency
- Consider the implications of mutable vs immutable operations
- What happens at boundary conditions (empty chain, single bit, etc.)?
