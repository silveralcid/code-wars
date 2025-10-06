# Are You Playing Banjo?

## Description
Create a function that answers the question:  
**"Are you playing banjo?"**

If a person's **name starts with the letter "R" or "r"**, they **are playing banjo**.

---

## Behavior
The function takes a **name** as its only argument and returns one of the following:

- `"<name> plays banjo"`  
- `"<name> does not play banjo"`

---

## Examples
| Input | Output |
|--------|---------|
| `"Rick"` | `"Rick plays banjo"` |
| `"rolf"` | `"rolf plays banjo"` |
| `"Adam"` | `"Adam does not play banjo"` |
| `"George"` | `"George does not play banjo"` |

---

## Requirements
- Input will always be a **valid string**.  
- The check should be **case-insensitive** (`R` or `r` both count).  
- Return the correct phrase based on the first letter of the name.  

---

**Category:** `Strings` `Fundamentals`
