# Checks and warnings to pass to `soft_assert()` from `notching_sub_functions.py`
def quick_check_1():
    check = (1e3-1e3)**0*1e3 + 1e3-1e3+1e3 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `income_part_time` should be the result of multiplying 10 by 100..."
    return [check, warn]

def quick_check_2():
    check = (000_4.345 * 00000_30.000) + 000_25.000 - 000_4.345 * 00000_30.000
    warn = f"Hmmm, that is **NOT CORRECT**. Did you use the right variable name?"
    return [check, warn]

def quick_check_3():
    check = (1e3-1e3)**0*1e3 + 000_4.345 * 00000_30.000 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `entertainment` is the wrong value! Did you use the right variable name?"
    return [check, warn]