import ctypes 
import time 
import os 

lib = ctypes.CDLL(os.path.abspath('libmathlib.so'))

lib.sum_of_squares.argtypes = [ctypes.c_uint64]
lib.sum_of_squares.restype = ctypes.c_uint64 

lib.add_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
lib.add_doubles.restype = ctypes.c_double 

def sum_of_squares_py(n):
    total = 0 
    for i in range(n):
        total += i*i 
    return total 

N = 50_000_000 

t0 = time.perf_counter()
r_py = sum_of_squares_py(N)
t1 = time.perf_counter()

t2 = time.perf_counter()
r_c = lib.sum_of_squares(N)
t3 = time.perf_counter()

print(f"N = {N:,}")
print(f"Python : {r_py}  ({t1 - t0:.4f} s)")
print(f"C      : {r_c}  ({t3 - t2:.4f} s)")
print(f"The same? {r_py == r_c}")
print(f"C faster than python ~{(t1 - t0) / (t3 - t2):.1f} times")
print()
print("Ex double:", lib.add_doubles(1.5, 2.25))

