def sum_two_num(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Non-interger input is not allowed")
    return a + b


sum_two_num(1,2)