### Problem

Given a string, return a new string in which each character (case-sensitive) is repeated once.

---

### Examples

| Input | Output |
| ------ | ------- |
| `"String"` | `"SSttrriinngg"` |
| `"Hello World"` | `"HHeelllloo  WWoorrlldd"` |
| `"1234!_ "` | `"11223344!!__  "` |

---

### Task

Write a function that:
1. Takes a string as input.
2. Returns a string where each character is repeated once.

---

### Example Implementation (Python)

```python
def double_char(s):
    return ''.join([c * 2 for c in s])
