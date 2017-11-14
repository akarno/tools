

def fun(x):
    if not isinstance(x, int):
        raise ValueError
    return x + 1

def fun_exception():
    raise SystemExit(1)
