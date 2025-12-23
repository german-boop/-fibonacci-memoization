
# 🧠 Fibonacci Memoization 

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
    " " "# Fibonacci Memoization

An optimized implementation of the Fibonacci sequence in Python using **recursion** and **memoization** for efficient computation with large numbers.

---

## 📌 Overview

The Fibonacci sequence is a classic mathematical series defined as:

> **F(n) = F(n − 1) + F(n − 2)**  
> with base cases:  
> **F(0) = 0**, **F(1) = 1**

A straightforward recursive implementation can be inefficient because it repeatedly calculates the same values. This project addresses that issue by utilizing **memoization**, a key concept in **Dynamic Programming**.

---

## ⚡ Features

- 🔁 Recursive Fibonacci implementation
- 🧠 Memoization (caching results for improved efficiency)
- 🚀 Fast computation for large values (e.g., `F(301)`)
- 📘 Clean and readable Python code
- 🎓 Ideal for learning algorithms and optimization techniques

---

## 🧮 How It Works

- Previously computed Fibonacci numbers are stored in a dictionary (`memo`).
- If a value is requested again, it is returned instantly from memory.
- This approach reduces time complexity from **exponential** to **linear**.

⏱️ **Time Complexity:** `O(n)`  
💾 **Space Complexity:** `O(n)`

---

## 🧪 Code Example

```python
def fibonacci(n, memo={}):
    """ Calculate the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(f"Fibonacci(200): {fibonacci(200)}")
print(f"Fibonacci(301): {fibonacci(301)}")
```

This version clarifies the text and corrects any errors to enhance comprehension. Calculate nth Fibonacci number using memoization"""
    If n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(f"Fibonacci(200): {fibonacci(200)}")
print(f"Fibonacci(301): {fibonacci(301)}")


▶️ How to Run

1. Make sure Python 3 is installed
2. Save the file as fibonacci.py
3. Run:
python fibonacci.py

🎯 Use Cases
* 📚 Learning recursion and dynamic programming
* 🧠 Understanding algorithm optimization
* 🧪 Python practice projects
* 🧮 Mathematical computing

🏷️ Topics

python · fibonacci · memoization · dynamic-programming · recursion · algorithms

📜 License

📝 This project is licensed under the MIT License — free to use, modify, and share.

⭐ Acknowledgment

If you find this repository useful, feel free to ⭐ star it and share it!

Happy coding! 🚀

