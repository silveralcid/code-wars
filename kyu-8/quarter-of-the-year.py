def quarter_of(month):
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12 inclusive")
    return (month - 1) // 3 + 1
