Consider the following version of Bubble Sort:

```
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
```

**Task**

Given an `n`-element array, `A` = a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n-1</sub>, of distinct elements, sort array `A` in ascending order using the _Bubble Sort_ algorithm above. Once sorted, print the following three lines:

1. `Array is sorted in numSwaps swaps.`, where `numSwaps` is the number of swaps that took place.
2. `First Element: firstElement`, where `firstElement` is the first element in the sorted array.
3. `Last Element: lastElement`, where `lastElement` is the last element in the sorted array.

**Hint**: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

**Input Format**

The first line contains an integer, `n`, denoting the number of elements in array `A`. 
The second line contains `n` space-separated integers describing the respective values of a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n-1</sub>.

**Constraints**

- ` 2 ≤ n ≤ 600 `
- ` 1 ≤ a<sub>i</sub> ≤ 2 X 10<sup>6</sup>, ∀ i ∈ [0, n-1] `

**Output Format**

You must print the following three lines of output:

1. `Array is sorted in numSwaps swaps.`, where `numSwaps` is the number of swaps that took place.
2. `First Element: firstElement`, where `firstElement` is the first element in the sorted array.
3. `Last Element: lastElement`, where `lastElement` is the last element in the sorted array.
