import hashlib

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(transactions: list[str]) -> str:
    if not transactions:
        return None

    # Convert each transaction into a hash
    hashes = [sha256(tx) for tx in transactions]

    # Keep merging until only the root remains
    while len(hashes) > 1:
        # If the number of hashes is odd, duplicate the last one (padding)
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])

        # Merge pairs and hash them again
        new_level = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            new_hash = sha256(combined)
            new_level.append(new_hash)
        hashes = new_level

    return hashes[0]  # Only one hash left, which is the Merkle Root

# Test data (simulate 4 transactions)
transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_root = build_merkle_tree(transactions)

print("Merkle Root:", merkle_root)
