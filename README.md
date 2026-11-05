# 📊 Sorting Algorithms Benchmarking Suite (Tkinter)

> A first-principles desktop application built from scratch to visualize, execute, and benchmark the time complexity and mechanical efficiency of 9 distinct sorting algorithms.

*Note: This project was developed entirely from scratch in June 2022 (Pre-AI) without relying on external algorithmic libraries or boilerplate templates. Every sorting mechanism was manually implemented to study algorithmic data structures under the hood.*

---

## 🛠️ Core Features

* **Custom Algorithm Implementations:** Pure Python, from-scratch implementations of Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix, and Bucket Sort.
* **Granular Performance Benchmarking:** Instead of just measuring execution time, the engine tracks exact internal mechanics:
  * Number of Swaps / Memory Writes.
  * Number of Conditional Checks (`if` statements / comparisons).
  * Microsecond-level execution timing (`datetime`).
* **Data Dispersion Analysis:** Automatically calculates the Standard Deviation (`stdev`) of imported datasets to evaluate how data dispersion inversely affects the efficiency of non-comparative algorithms like Counting Sort.
* **Custom I/O & File Browser:** Features a custom-built file navigation tree utilizing `win32api` to interface with Windows logical drives, allowing users to import raw `.txt` datasets and export sorted arrays.
* **Dynamic Resolution Scaling:** Custom mathematical scaling architecture that dynamically calculates screen ratio bounds (`1366x768` baseline) to render Tkinter absolute coordinates adaptively on any monitor.

---

## 🔬 Algorithmic Mechanics Addressed

1. **Comparative Sorts:**
   - **Quick Sort:** Recursive partitioning with pivot optimization.
   - **Merge Sort:** Recursive divide-and-conquer utilizing manual array popping and index reconstruction.
   - **Heap Sort:** Manual max-heap structural modeling and extraction.
   - **Insertion / Selection / Bubble:** Fundamental $O(n^2)$ array manipulations.
2. **Non-Comparative Sorts (Integer/Float Specific):**
   - **Counting Sort:** Frequency array mapping (validated for integer-only input).
   - **Radix Sort:** Least Significant Digit (LSD) base-10 digit extraction algorithm.
   - **Bucket Sort:** Optimized for $range(0,1)$ floating-point datasets utilizing sub-array clustering.

---

## 📦 Download & Execution

### Option 1: Standalone Executable (Windows)
Download the pre-compiled binary package directly from the [Releases Page](../../releases).

### Option 2: Run from Source
1. Ensure Python 3.10+ is installed.
2. Clone the repository:
   ```bash
   git clone [https://github.com/daniel-lalegani/Sorting-Algorithms-Benchmarking-Suite.git](https://github.com/daniel-lalegani/Sorting-Algorithms-Benchmarking-Suite.git)
