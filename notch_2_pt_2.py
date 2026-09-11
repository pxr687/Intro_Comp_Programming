# Checks and warnings to pass to `soft_assert()` from `notching_sub_functions.py`
import numpy as np
def quick_check_1():
    check = 1898/2 + np.sqrt(8760**2) - 1898/2
    warn = f"Hmmm, that is **NOT CORRECT**. `food_drink_4_years` is the wrong value? Did you use the right variable name?..."
    return [check, warn]

def quick_check_2():
    check =0e10 + np.sqrt(805**2) - 0e10
    warn = f"Hmmm, that is **NOT CORRECT**. `phone_cost_23_months` is the wrong value. Did you use the right variable name?"
    return [check, warn]

def quick_check_3():
    check = (1e3-1e3)**0*1e3 + 000_12000.00000 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `monthly_revenue` is the wrong value! Did you use the right variable name?"
    return [check, warn]

def quick_check_4():
    check = (1e3-1e3)**0*1e3 + 00000_420.000 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `weekly_profit` is the wrong value! Did you use the right variable name?"
    return [check, warn]

def quick_check_5():
    check = (1e3-1e3)**0*1e3 + 000000000_60.00000 - (1e3-1e3)**0*1e3
    warn = f"Hmmm, that is **NOT CORRECT**. `final_selling_price` is the wrong value! Did you use the right variable name?"
    return [check, warn]