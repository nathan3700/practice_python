# ATPG / DFT Verification Exercise: Scan Chain Model

## Purpose

This exercise evaluates verification ability in an ATPG and Design For Test (DFT) context. The emphasis is on understanding a behavioral specification, identifying incorrect assumptions, designing discriminating tests, and modeling observable faults.

DFT knowledge is useful, but the exercise can be completed without prior experience in a commercial ATPG tool.

## Scenario

You are given a partially implemented Python model of a serial scan chain. A scan chain contains a fixed number of scan cells. During shift operation, one bit enters at the scan input and one bit leaves at the scan output. During capture, a parallel circuit response is loaded into the chain.

The provided implementation and tests may contain defects. Treat both the implementation and the tests as review material: do not assume that every existing expectation is correct.

## Behavioral Contract

Use the following convention throughout the implementation and tests:

- A chain has a positive integer length.
- The internal state is represented from scan input side to scan output side.
- Initially, and after reset, every cell contains `0`.
- `shift_in(bit)` accepts only the integer values `0` and `1`.
- On each shift, the new bit is inserted at position `0`; the previous final cell is shifted out.
- `shift_in(bit)` returns the bit shifted out.
- `shift_pattern(pattern)` shifts each bit in iterable order and returns the list of shifted-out bits.
- A pattern may have any non-negative length. It is not required to equal the chain length.
- `capture(data)` replaces the complete chain state. `data` must contain exactly `length` bits.
- Capture and reset set the shift count to zero.
- `get_output()` returns the bit currently at the scan output side. An empty chain is invalid and must be rejected during construction.
- `get_chain_state()` returns a copy, so callers cannot mutate internal state accidentally.
- Invalid input must produce a specific, documented exception such as `ValueError` or `TypeError`.

The candidate should state any interpretation they believe is ambiguous before implementing it.

## Starting Material

The repository contains:

- `scan_chain_model.py`: a partially implemented model with intentional defects.
- `test_scan_chain.py`: an incomplete test suite containing both useful checks and questionable assumptions.

The candidate may modify the implementation and tests. They should not silently remove a failing test without explaining why its expectation is incorrect.

## Tasks

### Part 1: Specification and Test Review - 15 minutes

Review the implementation and existing tests. Document:

1. At least three functional defects or behavioral risks.
2. At least two test-quality problems, missing checks, or ambiguous expectations.
3. The assumptions that must be clarified before implementation.
4. A short test plan organized by normal behavior, invalid input, boundary conditions, and fault behavior.

At least one finding must distinguish between an actual implementation defect and a design choice that requires a specification decision.

### Part 2: Model Correction - 20 minutes

Update the scan-chain model so that it satisfies the behavioral contract.

The implementation should include:

- Constructor validation.
- Bit and sequence validation.
- Correct shift behavior and shifted-out values.
- Correct capture and reset behavior.
- Protection against external mutation of internal state.
- Clear exception types and useful error messages.

Keep the public API small and explain any API changes.

### Part 3: Verification and Fault Modeling - 20 minutes

Add a small verification-oriented capability. Choose one of the following approaches and document the choice:

#### Option A: Observable fault injection

Allow a test to configure a cell as stuck at `0` or stuck at `1` during shifting. Add a method that shifts a known pattern through the chain and reports whether the observed outputs match the expected outputs.

The fault model must be observable through the public behavior. A fault that only changes private state but cannot affect an output is not considered detected.

#### Option B: Reference-model comparison

Implement a simple independent reference model or checker that predicts shifted-out values. Add a verification method that compares the implementation's observed outputs against the reference for a sequence of operations.

The checker must report the first mismatch, including enough information to diagnose the operation and expected versus observed values.

For either option, include tests that demonstrate:

- A known-good chain passes.
- A detectable fault or injected mismatch is detected.
- A non-detectable or irrelevant fault is not incorrectly reported as detected.
- Invalid verification inputs are rejected.

### Part 4: Tests and Review - 15 minutes

Add or revise tests to cover:

- Construction with valid and invalid lengths.
- Single-bit and multi-bit shifting.
- A one-cell chain.
- Reset and capture behavior.
- Empty and overlong patterns, if supported by the contract.
- Invalid bit values and invalid data types.
- Capture data of the wrong length.
- Mutation of a list returned by `get_chain_state()`.
- Output ordering and shifted-out values.
- The selected fault or reference-model verification behavior.

At least one test should fail against the original implementation and pass after the fix. At least one test should demonstrate that an existing test expectation was ambiguous or incorrect, if applicable.

## Interviewer Evaluation

### Verification mindset

- Does the candidate challenge ambiguous assumptions?
- Do tests isolate one behavior at a time?
- Are negative tests intentional rather than incidental?
- Can the candidate explain what each test proves?
- Do they distinguish detection, diagnosis, and mere state change?

### DFT and ATPG reasoning

- Do they understand shift-in and shift-out ordering?
- Do they reason about controllability and observability?
- Do they understand that fault detection requires an observable effect and an expected response?
- Do they avoid claiming that shift history alone proves a stuck-at fault?

### Engineering quality

- Are validation and state ownership handled consistently?
- Are exception behavior and public interfaces clear?
- Is the reference/checking logic independent enough to catch mirrored implementation bugs?
- Are tests readable, deterministic, and focused?

## Suggested Scoring

Score each category from 0 to 3:

- Specification analysis and ambiguity handling
- Test strategy and edge-case coverage
- Correct scan-chain behavior
- Fault-model or reference-checker quality
- DFT/ATPG reasoning
- Code clarity and maintainability

A strong candidate does not need to complete every extension. Strong signals include identifying an invalid or underspecified requirement, writing a failing test before changing code, and explaining why a proposed test can or cannot detect a particular fault.

## Interviewer Follow-up Questions

Use these questions to probe reasoning without requiring more implementation time:

1. What is the exact order of bits observed at scan output after loading a pattern?
2. How would you prove that a chain is wired in the wrong order?
3. What additional observation is required to detect a stuck-at fault reliably?
4. How would you avoid a checker that contains the same bug as the design under test?
5. Which properties would you test for every sequence of shifts, rather than only with a few examples?
6. How would the approach change for multiple chains with XOR compaction?
7. What information would you include in a failure report from an ATPG verification environment?

## Constraints and Deliverables

The candidate should produce:

1. A short review of defects, ambiguities, and test risks.
2. A corrected scan-chain implementation.
3. A focused verification capability using either fault injection or an independent reference model.
4. Tests that demonstrate both correct behavior and meaningful failure detection.

The goal is not to build a production ATPG engine. The goal is to demonstrate disciplined verification thinking on a small, understandable DFT model.
