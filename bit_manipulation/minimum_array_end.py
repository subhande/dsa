# Minimum Array End
# https://leetcode.com/problems/minimum-array-end/description/?envType=problem-list-v2&envId=bit-manipulation


# Solution 1: Brute Force
# Time complexity: O(n) | Space complexity: O(1)
class Solution1:
    def minEnd(self, n: int, x: int) -> int:
        result = x

        # Step 1: Iterate n-1 times (since we already initialized result with x)
        while n > 1:
            # Step 2: Increment result and perform bitwise OR with x
            result = (result + 1) | x
            n -= 1

        return result

# Solution 2: Optimal Approach
# Time complexity: O(logn) | Space complexity: O(logn)
class Solution2:
    def minEnd(self, n: int, x: int) -> int:

        result = 0
        # Reducing n by 1 to exclude x from the iteration
        n -= 1

        # Step 1: Initialize lists to hold the binary representation of x and n-1
        binaryX = [0] * 64  # Binary representation of x
        binaryN = [0] * 64  # Binary representation of n-1

        # Step 2: Build binary representations of x and n-1
        for i in range(64):
            bit = (x >> i) & 1  # Extract i-th bit of x
            binaryX[i] = bit

            bit = (n >> i) & 1  # Extract i-th bit of n-1
            binaryN[i] = bit

        posX = 0
        posN = 0

        # Step 3: Combine binary representation of x and n-1
        while posX < 63:
            # Traverse binaryX until we find a 0 bit
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            # Copy bits from binaryN (n-1) into binaryX (x) starting from the first 0
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        # Step 4: Rebuild the final result from the combined binary representation
        for i in range(64):
            if binaryX[i] == 1:
                # convert binary bit to decimal value
                result += pow(2, i)

        return result


"""
This is a very insightful question, let's break down the intuition carefully to clarify:

---

## 🔍 **Step-by-Step Intuition Breakdown**

The core insight behind this solution is subtle yet powerful:

### 🎯 **1. What does the problem really ask for?**

The problem wants an array of length `n`, strictly increasing, whose bitwise AND is exactly equal to `x`.

This means:

- Every bit **set in `x`** must be **present in every number** of our array (otherwise AND-ing them would clear that bit).
- Bits **unset in `x`** are optional. They can be set or unset differently across array elements, as long as the final bitwise AND equals exactly `x`.

### 🎯 **2. Why must every element have bits of `x`?**

If we omit **any bit** of `x` in even a single element, then AND-ing with that element would turn **that bit off**, making the result smaller than `x`. Hence, every number must include **all bits** that `x` includes.

Thus, the **minimum possible number** we can have in our array is `x` itself.

### 🎯 **3. How to get a strictly increasing array minimally?**

We need the array numbers to be strictly increasing:

```
nums[0] < nums[1] < nums[2] < ... < nums[n-1]
```

Since we want **minimum last number**, we must pick **the smallest possible numbers** at every step.

We start from smallest possibility: **nums[0] = x**.

To make numbers strictly increasing, the next numbers must be greater, minimally.

- Ideally, to minimize, numbers differ minimally. So nums could be:
```
nums[0] = x
nums[1] = x + something_small
nums[2] = x + something_slightly_bigger
...
```

But remember, each of these numbers **must keep all the bits of `x`**. So we can only vary numbers in positions **where `x` has a 0 bit**, because we can't unset bits already set in `x`.

### 🎯 **4. Relating the number of bits we can play with to the value (n-1)**

- Notice: We have an array of size `n`, meaning we need `n-1` numbers bigger than `x`.
- To minimally accommodate these `(n-1)` bigger numbers, we realize we need to "encode" `(n-1)` into bits that are free (i.e., **unset bits in `x`**).

This is the critical intuition:

- If you have `k` free bits (unset in `x`), you can create up to `2^k` different numbers by varying these bits.
- We only need `(n-1)` numbers. Hence, minimally encode `(n-1)` into those free bits.

### 🎯 **5. **"Encoding" `(n-1)` into unset bits of `x` (The key intuition)**

- To make this minimal, you simply need to **place binary representation of `(n-1)` into the free bit positions** (the zero bits of `x`), from the least significant bit upwards.
- This "injection" of `(n-1)` into the unset bits of `x` is exactly the way to minimally achieve an array of size `n` with bitwise AND equals `x`.

**Why `(n-1)` instead of `n`?**
Because the first number is already taken (`x` itself), you're left needing exactly `(n-1)` numbers larger than `x`. Thus, the number to encode into these free bits is precisely `(n-1)`.

---

## 🧩 **Let's summarize with an illustrative example:**

### Example: `n = 3`, `x = 4` (`100` in binary)

- We need an array `[nums[0], nums[1], nums[2]]` (3 numbers)
- Bitwise AND must be `4` (100 in binary).

Initially:
- nums[0] must be ≥ 4 → minimal possible is **4 itself**.
- To minimally have 2 more numbers (`n-1 = 2`), encode `2` into the unset bits of `4`.

Let's check bits of `4`:

```
4 → (100)
bits: 2 1 0 (positions)
      1 0 0
```

- Bits unset: positions **0,1**.
- `n-1 = 2` in binary is `(10)`.

We put this `(10)` binary into unset positions **(from lower bits)**:

- bit 0 ← 0
- bit 1 ← 1

Thus, number is:

```
bit 2 = 1 (from x)
bit 1 = 1 (encoded from n-1)
bit 0 = 0 (encoded from n-1)
```

Number is `(110)` = **6** decimal.

Thus, minimal nums is `[4,5,6]`. **Last number is 6**, exactly the minimal we wanted.

---

## 🚀 **General Method (for intuition):**

**"To minimally get the last number, you encode `(n-1)` into the unset bits of `x`."**

That's the intuition and why you inject bits from `(n-1)` into `x`.

---

## 🎯 **How to easily realize this in an interview?**

- Every number **must have all bits of x** (due to AND requirement).
- You have `(n-1)` numbers to create → you minimally encode `(n-1)` into unset bits of `x`.
- Smallest way to encode a number into another number is from lowest to higher bits.
- Hence, we do exactly this in code.

---

**⚡ In short, the intuition behind injecting bits from `(n-1)` into `x` arises directly from these constraints:**

- **All bits of x must remain** (bitwise AND condition).
- **To minimize the last number**, encode **exactly `(n-1)` into available unset bits of `x`.

---

**✅ That's the full step-by-step intuition behind why we're injecting bits from `(n-1)` into `x` for minimal solution!**

"""

# Solution 3: Optimal Approach (without extra space)
# Time complexity: O(logn) | Space complexity: O(1)
class Solution3:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # we start counting from 0, so adjust n by subtracting 1
        result = x
        bit_pos = 0  # position to check/set bits in result

        while n > 0:
            # Check if current bit_pos is not set in x
            if not (x & (1 << bit_pos)):
                # Set this bit according to lowest bit of n
                if n & 1:
                    result |= (1 << bit_pos)
                n >>= 1  # Move to the next bit in n
            bit_pos += 1  # Check next bit position in result/x

        return result


if __name__ == '__main__':
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()


    # Test cases
    #
    # Example 1

    n = 3
    x = 4
    # Expected output: 7
    assert sol1.minEnd(n, x) == 6
    assert sol2.minEnd(n, x) == 6
    assert sol3.minEnd(n, x) == 6
