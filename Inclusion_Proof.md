## Merkle Tree with Odd Number of Leaf Nodes
Suppose the bottom layer (leaf nodes) has 5 transactions:
```
Tx0, Tx1, Tx2, Tx3, Tx4
```
## Step 1: Hash Each Transaction (Leaf Nodes)
We hash each transaction to get:

```
H0, H1, H2, H3, H4
```

## Step 2: Pair and Hash Adjacent Nodes
Since there are 5 nodes (odd number), the last node H4 has no pair.

To make pairs, we duplicate the last node H4 once, so it pairs with itself:

```
(H0 + H1), (H2 + H3), (H4 + H4)
```

We denote the new hashes as:


```
H01, H23, H44
```

## Simple Diagram:
```
Level 2 (Root)
       H012344
        /    \
Level 1       H44
  /   \         
H01   H23   
```
  

Level 0 (Leaves)
```
H0  H1  H2  H3  H4  H4 (duplicate of last node)
```
Notice how the bottom layer H4 is duplicated, making the total number of nodes even, which allows pairing without issues.

When Retrieving the Merkle Path:
If you want to find the sibling of H4, because we duplicated it, the sibling of H4 is itself (H4).

## Code Explanation:
python
```
if sibling_index >= len(level):
    sibling_index = index
```
If the sibling index goes beyond the length of nodes in this level (because originally there were fewer nodes, but logically we treat the last node as duplicated), we just use the node itself as its sibling.

## Why?
This approach handles the special case of odd numbers of leaf nodes in Merkle Trees by duplicating the last node to make pairing consistent. Using the node itself as its sibling ensures the hash calculations stay correct and consistent.
