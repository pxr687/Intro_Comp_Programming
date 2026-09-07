# Checks and warnings to pass to `soft_assert()` from `notching_sub_functions.py`
def check_1():
    check = (1e3-1e3)**0*1e3 + 1e3-1e3+1e3 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `income_part_time` should be the result of multiplying 10 by 100..."
    return [check, warn]

def check_2():
    check = (1e3-1e3)**0*1e3 + 0.251e2 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. Did you use the right variable name?"
    return [check, warn]