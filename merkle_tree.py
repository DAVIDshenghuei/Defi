import hashlib

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(transactions: list[str]) -> list[list[str]]:
    """
    Build Merkle Tree and return all levels (bottom to top).
    Each level is a list of hashes.
    """
    # Convert transactions to leaf hashes
    current_level = [sha256(tx) for tx in transactions]
    tree = [current_level]  # Store all levels

    while len(current_level) > 1:
        # If odd number, duplicate last hash
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        next_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i+1]
            next_level.append(sha256(combined))
        tree.append(next_level)
        current_level = next_level

    return tree

def get_merkle_path(tree: list[list[str]], index: int) -> list[str]:
    """
    Get Merkle Path for the leaf at 'index'.
    Returns list of sibling hashes from bottom to top.
    """
    path = []
    for level in tree[:-1]:  # Skip root level
        # Determine sibling index
        if index % 2 == 0:
            sibling_index = index + 1
        else:
            sibling_index = index - 1

        # Handle edge case: if sibling_index out of range, use last node itself
        if sibling_index >= len(level):
            sibling_index = index

        path.append(level[sibling_index])
        index //= 2  # Move to parent index for next level

    return path

def verify_merkle_path(leaf_hash: str, merkle_path: list[str], root: str, index: int) -> bool:
    """
    Verify that the leaf_hash is included in the Merkle tree
    with the given root using the Merkle path.
    """
    computed_hash = leaf_hash
    for sibling_hash in merkle_path:
        if index % 2 == 0:
            combined = computed_hash + sibling_hash
        else:
            combined = sibling_hash + computed_hash
        computed_hash = sha256(combined)
        index //= 2
    return computed_hash == root

# Example usage
transactions = ["tx1", "tx2", "tx3", "tx4"]
tree = build_merkle_tree(transactions)
root = tree[-1][0]
print("Merkle Root:", root)

index = 2  # We want to prove "tx3"
leaf_hash = sha256(transactions[index])
path = get_merkle_path(tree, index)
print("Merkle Path for tx3:", path)

# Verify
is_valid = verify_merkle_path(leaf_hash, path, root, index)
print("Verification result:", is_valid)
