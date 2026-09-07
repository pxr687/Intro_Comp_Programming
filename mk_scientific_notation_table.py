# Example for the Numbers page (on Scientific Notation)
from jupyprint import jupyprint

def strip_trailing(num):
    return format(num, "f").rstrip("0").rstrip(".")

def scientific_notation_table(input_num):
    jupyprint("### $\\text{Value} = "+f"{input_num}"+" * 10^{x}$")
    table = f"""
| $x$ | Value                  | Python Scientific Notation |
| ---: | --------------------: | -------------------------: |
|    6 |       {strip_trailing(input_num*10**6)} | `{input_num}e06` |
|    5 |       {strip_trailing(input_num*10**5)} | `{input_num}e05` |
|    4 |       {strip_trailing(input_num*10**4)} | `{input_num}e04` |
|    3 |       {strip_trailing(input_num*10**3)} | `{input_num}e03` |
|    2 |       {strip_trailing(input_num*10**2)} | `{input_num}e02` |
|    1 |       {strip_trailing(input_num*10**1)} | `{input_num}e01` |
|    0 |       {strip_trailing(input_num*10**0)} | `{input_num}e00` |
|   -1 | {strip_trailing(input_num*10**-1)} | `{input_num}e-01` |
|   -2 | {strip_trailing(input_num*10**-2)} | `{input_num}e-02` |
|   -3 | {strip_trailing(input_num*10**-3)} | `{input_num}e-03` |
|   -4 | {strip_trailing(input_num*10**-4)} | `{input_num}e-04` |
|   -5 | {strip_trailing(input_num*10**-5)} | `{input_num}e-05` |
|   -6 | {strip_trailing(input_num*10**-6)} | `{input_num}e-06` |
"""
    jupyprint(table)
