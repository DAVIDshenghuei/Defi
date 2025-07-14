# 🔐 What is a Merkle Tree?
A Merkle Tree is a binary tree where each leaf node is a hash of data (like a transaction), and each non-leaf node is a hash of its children. It allows efficient and secure verification of the contents of large data structures, and is a core component in blockchain systems like Bitcoin and Ethereum.

## 🧩 Future Improvements
Visualize the tree structure

Add Merkle proof verification

Support for different hash algorithms

## 🧬 Merkle Tree Generator in Python

A simple Python script to generate a Merkle Tree from a list of transactions and compute the Merkle Root. This is useful for understanding how blockchain ensures data integrity using hash trees.

---

## 📦 Features

- SHA-256 hashing of transactions
- Builds a binary Merkle Tree
- Handles odd number of transactions by duplicating the last hash
- Outputs the Merkle Root

[Inclusion_Proof] = (Inclusion_Proof.md)

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x

### 💻 Run the Script

```bash
python merkle_tree.py
```
You can edit the transactions list in the script to test different datasets.

🧠 How It Works
Each transaction string is hashed using SHA-256.

Adjacent hashes are concatenated and hashed again to build upper levels.

If there's an odd number of hashes, the last one is duplicated.

This process repeats until only one hash remains — the Merkle Root.

📊 Example
Input transactions:

python
```bash
["tx1", "tx2", "tx3", "tx4"]
```
Output:
```bash
Merkle Root: 8e2fbb56a3e18962d9f5c6cf589e5f9832be50e6adf9c117c087db0f511c476d
```
📚 Files
```bash
merkle_tree.py – Main script to build the Merkle Tree
```
```bash
        Merkle Root
            │
       ┌────┴────┐
     H12        H34
    ┌──┴──┐    ┌──┴──┐
  H1     H2   H3    H4
```

## 🚀 Let's say you have 4 transactions:
```bash
Tx1, Tx2, Tx3, Tx4
```
Step 1: Hash Each Transaction with SHA-256 (Become Leaf Nodes)
```bash
H1 = hash(Tx1)
H2 = hash(Tx2)
H3 = hash(Tx3)
H4 = hash(Tx4)
```
Step 2: Concatenate Each Pair of Hashes and Hash Again
```bash
H12 = hash(H1 + H2)
H34 = hash(H3 + H4)
```
Step 3: Repeat Until Only One Hash Remains — the Merkle Root
```bash
H12, H34
```
```bash
Root = hash(H12 + H34)
```
This final Root is the top of the Merkle Tree — and it's called the Merkle Root for this set of transactions.
