"""
Bit manipulation involves performing operations directly on the binary representations of numbers. Here are some of the basic bit manipulation operations along with explanations and examples:

1. AND ( & )
  • Operation: Compares each binary digit (bit) of two numbers and returns 1 only if both corresponding bits are 1; otherwise, it returns 0.
  • Example:
    If A = 1010 (binary for 10) and B = 1100 (binary for 12), then:
     1010
     1100
     A & B = 1000 (which is 8 in decimal).

2. OR ( | )
  • Operation: Compares each bit of two numbers and returns 1 if at least one of the corresponding bits is 1.
  • Example:
    A = 1010 and B = 1100,
     1010
     1100
     A | B = 1110 (which is 14 in decimal).

3. XOR ( ^ )
  • Operation: Compares each bit of two numbers and returns 1 if the corresponding bits differ (i.e., one is 0 and the other is 1).
  • Example:
    A = 1010 and B = 1100,
     1010
     1100
     A ^ B = 0110 (which is 6 in decimal).

4. NOT ( ~ )
  • Operation: This is a unary operator that inverts every bit of the number (turning 1s to 0s and 0s to 1s). Note that in many programming languages, the NOT operator on integers is implemented as bitwise complement, so care must be taken with sign bits and representation (e.g., two’s complement in C/C++).
  • Example:
    If A = 1010 (for a simple 4-bit representation), then:
     ~A would be 0101.
    In practice, with fixed-width integers (say 32-bit), the result is computed accordingly.

5. Left Shift ( << )
  • Operation: Shifts the bits of a number to the left by a specified number of positions. Bits shifted off the left end are discarded, and new 0 bits are shifted in from the right.
  • Example:
    A = 0010 (binary for 2), and A << 2 shifts bits left two positions:
     0010 << 2 = 1000 (which is 8 in decimal).

6. Right Shift ( >> )
  • Operation: Shifts the bits of a number to the right by a specified number of positions. Depending on the type of right shift (logical vs. arithmetic), the vacated bits on the left might be filled with zeros or with the sign bit.
  • Example:
    A = 1000 (binary for 8), and A >> 2 shifts bits right two positions:
     1000 >> 2 = 0010 (which is 2 in decimal).

These operations are widely used in low-level programming, optimization, cryptography, and anywhere direct manipulation of bits is required. Most programming languages like C, C++, Java, and Python (using operators like &, |, ^, ~, <<, >>) support these basic operations, though details like operator precedence and integer sizes might differ across languages.

Let me know if you need further examples or more advanced bit manipulation techniques!

"""

"""
https://leetcode.com/problems/sum-of-two-integers/solutions/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/
"""

def main():
    # Define two numbers
    a = 10  # In binary: 1010
    b = 12  # In binary: 1100

    print("Number a:", a, "Binary:", bin(a))
    print("Number b:", b, "Binary:", bin(b))
    print()

    # Bitwise AND operation
    # Compares each bit: 1 if both bits are 1; otherwise 0.
    and_result = a & b
    print("a & b =", and_result, "Binary:", bin(and_result))

    # Bitwise OR operation
    # Compares each bit: 1 if either bit is 1.
    or_result = a | b
    print("a | b =", or_result, "Binary:", bin(or_result))

    # Bitwise XOR operation
    # Compares each bit: 1 if the bits differ.
    xor_result = a ^ b
    print("a ^ b =", xor_result, "Binary:", bin(xor_result))

    # Bitwise NOT operation (unary operator)
    # Inverts all the bits. In Python, ~a equals -(a+1) because of two's complement.
    not_result = ~a
    print("~a =", not_result, "Binary:", bin(not_result))
    # 01010 -> 10101 (in a 5-bit system) -> 11010 + 1 = 11011 -> -11
    # 0101 -> 1010 (in a 4-bit system) -> 1101 + 1 = 1110 -> -6
    # 1010 -> 0101 (in a 4-bit system) -> 5

    # Left Shift: Shifts bits to the left by 2 positions.
    # This is equivalent to multiplying by 2^2 (if there is no overflow).
    left_shift = a << 2
    print("a << 2 =", left_shift, "Binary:", bin(left_shift))

    # Right Shift: Shifts bits to the right by 2 positions.
    # This is roughly equivalent to dividing by 2^2 (discarding remainders).
    right_shift = a >> 2
    print("a >> 2 =", right_shift, "Binary:", bin(right_shift))

    # Swap numbers using XOR
    a = 5
    b = 7
    print("Before swapping: a =", a, "b =", b)
    a = a ^ b # a = 5 ^ 7 = 0101 ^ 0111 = 0010 = 2
    b = a ^ b # b = 2 ^ 7 = 0010 ^ 0111 = 0101 = 5
    a = a ^ b # a = 2 ^ 5 = 0010 ^ 0101 = 0111 = 7
    # ((a ^ b) ^ b)) = a ^ (b ^ b) = a ^ 0 = a
    # ((a ^ b) ^ a)) = b ^ (a ^ a) = b ^ 0 = b
    print("After swapping: a =", a, "b =", b)

    # Chcek if i'th is set or not
    n = 13 # 1101
    i = 2
    mask = 1 << i
    if n & mask:
        print(f"Bit {i} is set in {n}")
    else:
        print(f"Bit {i} is not set in {n}")

    # Set i'th bit
    n = 13 # 1101
    i = 1
    n = n | 1 << i
    print(f"Set {i}th bit in 13: {n}")

    # Unset i'th bit
    n = 13 # 1101
    i = 2
    n = n & ~(1 << i)
    print(f"Unset {i}th bit in 13: {n}")

    # Toggle i'th bit
    n = 13 # 1101
    i = 2
    n = n ^ 1 << i
    print(f"Toggle {i}th bit in 13: {n}")

    # Remove the last set bit or rightmost set bit
    n = 10 # 1010
    n = n & (n - 1) # 1010 & 1001 = 1000
    print(f"Remove the last set bit in 10: {n}")

    """
    40 -> 101000
    39 -> 100111 # after 40's rightmost bit all bits are set to 1
        101000
      & 100111
      --------
        100000 -> 32
    """

    # Get the rightmost different bit

    x = 12 # 1100

    res = x & -x # 1100 & 0100 = 0100
    print(f"Rightmost different bit: {res}")

    # Check if the number is power of 2
    n = 16
    if n & (n - 1) == 0:
        print(f"{n} is power of 2")
    else:
        print(f"{n} is not power of 2")


    # Count the number of set bits (brute force)
    n = 10 # 1010
    count = 0
    while n:
        count += n & 1
        n >>= 1
    print(f"Number of set bits in 10 (brute force): {count}")

    # Count the number of set bits (optimal)
    n = 10 # 1010
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    print(f"Number of set bits in 10 (optimal): {count}")

if __name__ == "__main__":
    main()
