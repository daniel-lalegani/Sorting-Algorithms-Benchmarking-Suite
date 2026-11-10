# Sorting Algorithms Benchmarking Suite

*A Python desktop application for running, comparing, and exploring sorting algorithms.*

<p align="center">
  <img src="Screenshot%20of%20application%20window.png" alt="Sorting Algorithms Benchmarking Suite application window" width="800">
</p>

I built this application independently in June 2022 without relying on external algorithmic libraries or boilerplate templates to better understand how sorting algorithms work beyond calling a built-in function. I implemented the algorithms in Python and created a Tkinter interface to generate or load data, run a selected algorithm, and inspect its output and performance.

## Features

- **Nine sorting algorithms implemented in Python:** Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix, and Bucket Sort.
- **Performance comparisons:** Records execution time and operation counts, including comparisons or conditional checks and swaps or data writes, as instrumented by each implementation.
- **Flexible input:** Enter values manually, import a `.txt` dataset, or generate random integers and floating-point values.
- **Dataset statistics:** Calculates standard deviation to help describe the spread of input values.
- **File handling:** Includes a custom Windows file browser using `win32api`, with options to import data and save sorted results.
- **Resizable interface:** Adjusts the Tkinter layout based on the display dimensions, using a 1366 × 768 reference layout.

## Sorting Algorithms

| Category | Algorithms | Notes |
| --- | --- | --- |
| Comparison-based | Bubble, Selection, Insertion | Simple algorithms useful for studying basic operations and quadratic-time behavior. |
| Comparison-based | Merge, Quick, Heap | More advanced approaches based on divide-and-conquer or heap structures. |
| Non-comparison-based | Counting, Radix | Intended for integer inputs in this application. |
| Distribution-based | Bucket | Intended for floating-point values in the range [0, 1). |

The application also offers **Python's built-in sorting** as a reference for comparison. Python's built-in implementation is not one of the nine algorithms implemented from scratch.

## Benchmarking Notes

The reported measurements are intended for **exploring and comparing implementations**, not for proving an algorithm's theoretical time complexity. Runtime depends on factors such as input size, data distribution, implementation details, and the computer running the application.

Operation counts are based on checks and assignments recorded in the code; they should not be interpreted as identical low-level operations across all algorithms. Timing values should likewise not be taken as a guarantee of microsecond measurement accuracy.

Standard deviation describes dataset dispersion, but it does not by itself determine how fast a particular sorting algorithm will run.

## Download & Execution

### Option 1: Standalone Executable (Windows)
Download the pre-compiled binary package directly from the [Releases Page](../../releases).

### Option 2: Run from Source
1. Ensure Python 3.10+ is installed.
2. Clone the repository:
   ```bash
   git clone [https://github.com/daniel-lalegani/Sorting-Algorithms-Benchmarking-Suite.git](https://github.com/daniel-lalegani/Sorting-Algorithms-Benchmarking-Suite.git)

## Project Scope

This was a personal learning project, not a new sorting-algorithm research contribution. Its main purpose was to practise Python programming, algorithm implementation, desktop interface development, and basic performance analysis.

**Author:** Daniel Lalegani
