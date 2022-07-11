# Binary Search

## Inspiration 

[LC Discussion – Powerful Ultimate Binary Search Template by `@zhijun_liao`](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

NOTE: This document is almost the same as the discussion linked above, but it's re-written here in case the original 
post gets taken down!  

---

While solving a problem or a sub-problem, if there comes a time when we need to **search something in a sorted array**, 
the first thing that we should check is – can we do binary search? In most cases, the answer would be **yes!** 

With binary search, the time complexity is reduced from linear `O(n)` to logarithmic `O(logn)` 

## Generalized Template

Suppose we have a **search space**. It could be an array, a range, etc. Usually it's sorted in ascending order. For most 
tasks, we can transform the requirement into the following generalized form:

```
Minimize k, such that condition(k) is True
```

This can be generalized to the following code snippet:

```python
def binary_search(array):
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)  # could be [0, n], [1, n] etc. depends on the problem
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid  # search left subarray
        else:
            left = mid + 1  # search right subarray
    return left
```

In most cases, we only need to **modify three parts** of this template:

- Correctly initialize the boundary variables `left` and `right` to specify search space. 
  - Rule: set up the boundary to **include all possible elements**
- Decide return value. Is it `return left` or `return left - 1`?
  - Remember: **after exiting the while loop, `left` is the minimal k satisfying the `condition` function**
- Design the condition function. Most difficult and most beautiful part!

## Applications

Toy application of this template can be found in [`binary_search.py`](binary_search.py)

### Basic

There will be cases where it's fairly straightforward to identify the search space and the `left` and `right` bounds.

- [LC 278 – First Bad Version [Easy]](https://leetcode.com/problems/first-bad-version/)
- [LC 69 – Square Root [Easy]](https://leetcode.com/problems/sqrtx/) | [code](applications/lc_69.py)
- [LC 35 – Search Insert Position [Easy]](https://leetcode.com/problems/search-insert-position/) | [code](applications/lc_35.py)

### Advanced

The above problems already came with an array input to be searched. However, **more often are the situations where the 
search space and search target are not so readily available**. Sometimes it's difficult to realize that the problem 
can/should be solved with binary search -- we might just turn to dynamic programming or DFS and get stuck for a very 
long time.

As for the question "When can we use binary search?" -- **if we can discover some kind of monotonicity, for example, if 
`condition(k) is True` then `condition(k + 1) is True`, then we can consider binary search**.

- [LC 1101 – Capacity To Ship Packages Within D Days [Medium]](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [code](applications/lc_1101.py)
- [LC 410 – Split Array Largest Sum [Hard]](https://leetcode.com/problems/split-array-largest-sum/) | [code](applications/lc_410.py)
- [LC 875 – Koko Eating Bananas [Medium]](https://leetcode.com/problems/koko-eating-bananas/) | [code](applications/lc_875.py)
- [LC 1482 – Minimum Number of Days to Make m Bouquets [Medium]](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | [code](applications/lc_1482.py)
- [LC 668 – Kth Smallest Number in Multiplication Table [Hard]](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/) | [code](applications/lc_668.py)
- [LC 719 – Find K-th Smallest Pair Distance [Hard]](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | [code](applications/lc_719.py)
- [LC 1201 – Ugly Number III [Medium]](https://leetcode.com/problems/ugly-number-iii/) | [code](applications/lc_1201.py)
- [LC 1283 – Find the Smallest Divisor Given a Threshold [Medium]](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | [code](applications/lc_1283.py)
