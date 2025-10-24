### Problem
You are given the length and width of a 4-sided polygon.  
The polygon can either be a rectangle or a square.

- If it is a **square**, return its **area**.  
- If it is a **rectangle**, return its **perimeter**.

---

### Examples
| Input | Output |
|--------|---------|
| 6, 10 | 32 |
| 3, 3  | 9  |

---

### Explanation
- For **6, 10** → Not equal → Rectangle → Perimeter = `2 × (6 + 10) = 32`
- For **3, 3** → Equal → Square → Area = `3 × 3 = 9`

---

### Function (Python)
```python
def area_or_perimeter(length, width):
    if length == width:
        return length * width  # Square: return area
    else:
        return 2 * (length + width)  # Rectangle: return perimeter
