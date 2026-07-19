import time

def faktorial_rekursif(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursif(n - 1)

def faktorial_iteratif(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def fibonacci_rekursif(n):
    if n <= 1:
        return n
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

def fibonacci_iteratif(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n_test = 10
print(f"--- Pengujian dengan n = {n_test} ---")
print(f"Faktorial Rekursif: {faktorial_rekursif(n_test)}")
print(f"Faktorial Iteratif: {faktorial_iteratif(n_test)}")
print(f"Fibonacci Rekursif: {fibonacci_rekursif(n_test)}")
print(f"Fibonacci Iteratif: {fibonacci_iteratif(n_test)}")