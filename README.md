# fibonacci-memoization
Recursive Fibonacci in Python with memorization for efficient large-number computation.

# 🧠 Fibonacci Memoization in Python

An optimized implementation of the Fibonacci sequence in Python using **recursion** and **memoization** to efficiently handle large inputs.

---

## 📌 Overview

The Fibonacci sequence is a classic mathematical series defined as:

> **F(n) = F(n − 1) + F(n − 2)**  
> with base cases:  
> **F(0) = 0**, **F(1) = 1**

A straightforward recursive implementation is inefficient because it repeatedly performs the same calculations involving redundant calculations.
This project solves that problem using **memoization**, a core concept of **Dynamic Programming**.

---

## ⚡ Features

- 🔁 Recursive Fibonacci implementation  
- 🧠 Memoization (caching results for efficiency)  
- 🚀 Fast computation for large values (e.g. `F(301)`)  
- 📘 Clean and readable Python code  
- 🎓 Suitable for learning algorithms and optimization techniques  

---

## 🧮 How It Works

- Previously computed Fibonacci numbers are stored in a dictionary (`memo`)
- When a value is requested again, it is returned instantly from memory
- This reduces time complexity from **exponential** to **linear**

⏱️ **Time Complexity:** `O(n)`  
💾 **Space Complexity:** `O(n)`

---

## 🧪 Code Example

```python
def fibonacci(n, memo={}):
    """ Calculate nth Fibonacci number using memoization"""
    If n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(f"Fibonacci(200): {fibonacci(200)}")
print(f"Fibonacci(301): {fibonacci(301)}")
