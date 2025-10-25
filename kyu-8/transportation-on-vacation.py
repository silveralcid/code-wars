def rental_car_cost(d):
    base = 40 * d
    if d >= 7:
        return base - 50
    elif 7 > d >= 3:
        return base - 20
    else:
        return base
