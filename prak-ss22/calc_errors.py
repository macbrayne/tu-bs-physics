# Fehlerrechnung per Funktion

from sympy import *

def calculate_errors(f, error_vars = None, prefix = '___'):    
    if error_vars == None:
        error_vars = f.free_symbols
    result = None
    for v in error_vars:
        err = Symbol(prefix + v.name)
        diff = f.diff(v)
        tmp = diff * err
        with evaluate(False):
            if result == None:
                result = tmp**2
            else:
                result += tmp**2
    return sqrt(result, evaluate=false)