#!/usr/bin/python3
import sys

def factorial(n):
    """Return factorial of n recursively."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # تحقق من وجود براميتر واحد
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    # تحقق من أن المدخل رقم صحيح
    if not sys.argv[1].isdigit():
        print("Error: input must be a non-negative integer.")
        sys.exit(1)

    n = int(sys.argv[1])

    # تحقق من أن الرقم غير سالب
    if n < 0:
        print("Error: factorial is not defined for negative numbers.")
        sys.exit(1)

    # حساب وعرض العاملية
    print(factorial(n))

if __name__ == "__main__":
    main()
