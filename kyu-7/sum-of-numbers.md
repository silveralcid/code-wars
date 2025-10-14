### Problem Statement

Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between and including them, and return it.  
If the two numbers are equal, return either `a` or `b`.

> **Note:** `a` and `b` are not ordered (i.e., `a` may be greater or less than `b`).

---

### Examples

| Input `(a, b)` | Output | Explanation                     |
|----------------|---------|----------------------------------|
| (1, 0)         | 1       | 1 + 0 = 1                       |
| (1, 2)         | 3       | 1 + 2 = 3                       |
| (0, 1)         | 1       | 0 + 1 = 1                       |
| (1, 1)         | 1       | Both are the same               |
| (-1, 0)        | -1      | -1 + 0 = -1                     |
| (-1, 2)        | 2       | -1 + 0 + 1 + 2 = 2              |

---

### Requirements

Your function should:
- Return only the numeric result (not the explanation).
- Handle both positive and negative integers.

---

### Tags

`Fundamentals` · `Algorithms`
