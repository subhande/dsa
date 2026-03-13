# Table of Contents
- [Bit Manipulation Basics](#bit-manipulation-basics)
  - [Bitwise Operators](#bitwise-operators)
  - [Common Properties Used in Bit Manipulation](#common-properties-used-in-bit-manipulation)
  - [Common Tricks and Problems](#common-tricks-and-problems)

# Bit Manipulation Basics


3 -> 0000 0011
5 -> 0000 0101

1's complement of 3 -> ~3 -> 1111 1100
2's complement of 3 -> ~3 + 1 -> 1111 1100 + 1 -> 1111 1101

## Bitwise Operators
- `&` (AND): Returns 1 if both bits are 1, otherwise returns 0.
```
3      => 0000 0011
5      => 0000 0101
--------------------
3 & 5  => 0000 0001 (1 in decimal)
```
- `|` (OR): Returns 1 if at least one of the bits is 1, otherwise returns 0.
```
3      => 0000 0011
5      => 0000 0101
--------------------
3 | 5  => 0000 0111 (7 in decimal)
```
- `^` (XOR): Returns 1 if the bits are different, otherwise returns 0.
```
3      => 0000 0011
5      => 0000 0101
--------------------
3 ^ 5  => 0000 0110 (6 in decimal)
```
- `~` (NOT): Inverts the bits (0 becomes 1 and 1 becomes 0).
```
3      => 0000 0011
--------------------
~3     => 1111 1100 (-4 in decimal, due to two's complement representation)
```
- `<<` (Left Shift): Shifts bits to the left by a specified number of positions, filling with 0s.
```
3      => 0000 0011
--------------------
3 << 1 => 0000 0110 (6 in decimal)
```
- `>>` (Right Shift): Shifts bits to the right by a specified number of positions, filling with 0s (for unsigned) or the sign bit (for signed).
```
3      => 0000 0011
--------------------
3 >> 1 => 0000 0001 (1 in decimal)
```

## Common Properties Used in Bit Manipulation
- `n & (n - 1)`: This expression clears the least significant set bit
```
n     => 0000 1101 (13 in decimal)
n - 1 => 0000 1100 (12 in decimal)
--------------------
n & (n - 1) => 0000 1101 & 0000 1100 => 0000 1100 (12 in decimal, least significant set bit is cleared)
```
- `n & -n`: This expression isolates the least significant set bit
- `n ^ (n - 1)`: This expression sets all bits to the right
- `n & ~(n - 1)`: This expression isolates the least significant set bit (alternative to `n & -n`)
- `a ^ b ^ b`: This expression returns `a` (useful for finding the unique element in an array where every other element appears twice)
- `a & (a - 1) == 0`: This expression checks if `a` is a power of two

## Common Tricks and Problems
- Binary to decimal
- Decimal to binary
- Swapping Two Numbers Without a Third Variable
```python
'''
A = 3
B = 5

1. A = A ^ B  => A = 0000 0011 ^ 0000 0101 => A = 0000 0110 (6 in decimal)
2. B = A ^ B  => B = 0000 0110 ^ 0000 0101 => B = 0000 0011 (3 in decimal)
3. A = A ^ B  => A = 0000 0110 ^ 0000 0011 => A = 0000 0101 (5 in decimal)
'''
def swap(A, B):
    A = A ^ B
    B = A ^ B
    A = A ^ B
    return A, B
```
- Checking if the i-th Bit is Set
```python
# Left Shift
n = 13, i = 2
n      => 0000 1101
1 << i => 0000 0100
--------------------
n & (1 << i) => 0000 1101 & 0000 0100 => 0000 0100 (non-zero, so the bit is set)

def is_ith_bit_set(n, i):
    return (n & (1 << i)) != 0
    
# Right Shift
n = 13, i = 2
n      => 0000 1101
n >> i => 0000 0011
--------------------
(n >> i) & 1 => 0000 0011 & 0000
0001 => 0000 0001 (non-zero, so the bit is set)

def is_ith_bit_set(n, i):
    return ((n >> i) & 1) != 0

```
- Setting the i-th Bit
```python
n = 13, i = 2
n      => 0000 1101
1 << i => 0000 0100
--------------------
n | (1 << i) => 0000 1101 | 0000
0100 => 0000 1101 (13 in decimal, bit was already set)

def set_ith_bit(n, i):
    return n | (1 << i)
```

- Clearing the i-th Bit
```python
n = 13, i = 2
n      => 0000 1101
1 << i => 0000 0100
--------------------
n & ~(1 << i) => 0000 1101 & 1111 1011 => 0000 1001 (9 in decimal, bit is cleared)

def clear_ith_bit(n, i):
    return n & ~(1 << i)
```
- Toggling the i-th Bit
```python
n = 13, i = 2
n      => 0000 1101
1 << i => 0000 0100
--------------------
n ^ (1 << i) => 0000 1101 ^ 0000 0100 => 0000 1001 (9 in decimal, bit is toggled)

def toggle_ith_bit(n, i):
    return n ^ (1 << i)
```
- Removing the Last Set Bit
```python
n = 13
n      => 0000 1101
n - 1  => 0000 1100
--------------------
n & (n - 1) => 0000 1101 & 0000 1100 => 0000 1100 (12 in decimal, last set bit is removed)

def remove_last_set_bit(n):
    return n & (n - 1)
```
- Checking if a Number is a Power of 2
```python

n = 16
n      => 0001 0000
n - 1  => 0000 1111
--------------------
n & (n - 1) => 0001 0000 & 0000 1111 => 0000 0000 (0 in decimal, so n is a power of 2)

n = 13
n      => 0000 1101
n - 1  => 0000 1100
--------------------
n & (n - 1) => 0000 1101 & 0000 1100 => 0000 1100 (non-zero, so n is not a power of 2)

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0
```
- Counting the Number of Set Bits (Using a Loop and Bitwise AND)
```python
# Approach 1: Using a Loop and Bitwise AND
n = 13
count = 0
while n > 0:
    count += n & 1  # Increment count if the least significant bit is set
    n >>= 1          # Right shift n to check the next bit
print(count)  # Output: 3 (since 13 has three set bits)

def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count
# Approach 2: Using Brian Kernighan's Algorithm
def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)  # Remove the least significant set bit
        count += 1    # Increment count for each set bit removed
    return count
```
