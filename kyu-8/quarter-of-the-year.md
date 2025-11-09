````markdown
### Problem

Given a month as an integer from **1 to 12**, return the **quarter of the year** it belongs to as an integer.

---

### Examples

| Input | Output | Explanation |
| ------ | ------- | ------------ |
| `2` | `1` | February → Q1 |
| `6` | `2` | June → Q2 |
| `11` | `4` | November → Q4 |

---

### Constraint

`1 <= month <= 12`

---

### Task

Write a function that:
1. Takes a month number (1–12) as input.
2. Returns the quarter (1–4) that month belongs to.

---

### Example Implementation (Python)

```python
def quarter_of(month):
    return (month + 2) // 3
````

---

**Category:** Fundamentals / Mathematics

```
```
