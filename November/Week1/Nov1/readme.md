# DSA Practice – Recursion & Dynamic Programming

## 1. Fibonacci Number (LeetCode 509)

### Problem

Find the nth Fibonacci number. Each number is the sum of the previous two numbers.

### Brute Force – Recursion

- Use the base cases `n <= 1`, where the function returns `n`.
- Recursively calculate `fib(n-1) + fib(n-2)`.
- The same subproblems are calculated multiple times.

**Time Complexity:** O(2^n)
**Space Complexity:** O(n) – Recursion stack.

### Optimal – Iterative Approach

- Initialize two variables `a = 0` and `b = 1`.
- Iterate from 2 to n.
- Calculate the next Fibonacci number using `a + b`.
- Update both variables in every iteration.
- Return the required Fibonacci number.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

## 2. Climbing Stairs (LeetCode 70)

### Problem

Find the number of distinct ways to climb n stairs when you can take either 1 or 2 steps at a time.

### Brute Force – Recursion

- At every step, there are two possible choices:
  - Climb 1 step.
  - Climb 2 steps.
- Recursively explore both possibilities.
- Add the number of ways from both recursive calls.

**Time Complexity:** O(2^n)
**Space Complexity:** O(n) – Recursion stack.

### Optimal – Iterative Dynamic Programming

- The number of ways to reach step n is the sum of the ways to reach steps n-1 and n-2.
- Initialize the first two values.
- Use two variables to store the previous two results.
- Update them iteratively until n is reached.

Recurrence relation:

`dp[n] = dp[n-1] + dp[n-2]`

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

## 3. Min Cost Climbing Stairs (LeetCode 746)

### Problem

Find the minimum cost required to reach the top of a staircase. You can start from index 0 or 1 and climb either 1 or 2 steps at a time.

### Brute Force – Recursion

- Start by considering the two possible starting positions.
- From each step, explore the next 1-step and 2-step moves.
- Add the cost of the current step.
- Find the minimum cost among the possible paths.

Recurrence relation:

`f(i) = cost[i] + min(f(i-1), f(i-2))`

**Time Complexity:** O(2^n) – Exponential due to repeated recursive calls.
**Space Complexity:** O(n) – Recursion stack.

### Optimal – Iterative Dynamic Programming

- Maintain two variables representing the minimum cost to reach the previous two steps.
- Calculate the minimum cost of reaching the current step.
- Update the variables in each iteration.
- Return the minimum cost of reaching the top.

Recurrence relation:

`dp[i] = cost[i] + min(dp[i-1], dp[i-2])`

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

## Complexity Comparison

| Problem                  | Approach     | Time Complexity | Space Complexity |
| ------------------------ | ------------ | --------------- | ---------------- |
| Fibonacci                | Brute Force  | O(2^n)          | O(n)             |
| Fibonacci                | Iterative    | O(n)            | O(1)             |
| Climbing Stairs          | Brute Force  | O(2^n)          | O(n)             |
| Climbing Stairs          | Iterative DP | O(n)            | O(1)             |
| Min Cost Climbing Stairs | Brute Force  | O(2^n)          | O(n)             |
| Min Cost Climbing Stairs | Iterative DP | O(n)            | O(1)             |
