````markdown
### Sum of Two Lowest Positive Numbers

Create a function that returns the **sum of the two lowest positive numbers** given an array of **at least 4 positive integers**.  
No floats or non-positive integers will be passed.

#### Example

```python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# Examples:
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))        # Output: 7
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))  # Output: 3453455
```
````

#### Explanation

- `sorted(numbers)` sorts the array in ascending order.
- `[:2]` selects the first two (smallest) numbers.
- `sum()` adds them together.

**Category:** Arrays | Fundamentals

```

```
