Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool together `money` dollars for ice cream. On any given day, the parlor offers a line of `n` flavors. Each flavor, `i`, is numbered sequentially with a unique ID number from `1` to `n` and has a cost, `cost`<sub>i</sub>, associated with it.

Given the value of `money` and the cost of each flavor for `t` trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

**Note**: Two ice creams having unique IDs `i` and `j` may have the same cost (i.e., `cost`<sub>i</sub> := `cost`<sub>j</sub>).

**Input Format**

The first line contains an integer, `t`, denoting the number of trips to the ice cream parlor. The `3t` subsequent lines describe all of Sunny and Johnny's trips to the parlor; each trip is described as follows:

1. The first line contains `money`.
2. The second line contains `n`.
3. The third line contains `n` space-separated integers denoting the cost of each respective flavor. The `i`<sup>th</sup> integer corresponds to the cost, `cost`<sub>i</sub>, for the ice cream with ID number `i` (where `1 ≤ i ≤ n`).

**Constraints**
- `1 ≤ t ≤ 50`
- `2 ≤ money ≤ 10`<sup>9</sup>
- `2 ≤ n ≤ 5 * 10`<sup>4</sup>
- `1 ≤ cost`<sub>i</sub>` ≤ 10`<sup>9</sup>, where `i ∈ [1, n] `
- It is guaranteed that there will always be a unique solution.

**Output Format**

Print two space-separated integers denoting the respective ID numbers for the two distinct flavors they choose to purchase, where the smaller ID is printed first and the larger ID is printed second. Recall that each ice cream flavor has a unique ID number in the inclusive range from `1` to `flavors`.