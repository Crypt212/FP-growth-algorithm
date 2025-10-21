from data_preprocessor import preprocess_data
from fp_tree_builder import build_fp_tree
from pattern_miner import mine_patterns


def main():
    """
    Main module that orchestrates the FP-Growth algorithm
    """
    # Sample transaction data
    transactions = [
        ['I2', 'I1', 'I5'],
        ['I2', 'I4'],
        ['I2', 'I3'],
        ['I2', 'I1', 'I4'],
        ['I1', 'I3'],
        ['I2', 'I3'],
        ['I1', 'I3'],
        ['I2', 'I1', 'I3', 'I5'],
        ['I2', 'I1', 'I3'],
    ]
    min_support = 2

    print("=" * 60)
    print("FP-GROWTH ALGORITHM")
    print("=" * 60)

    # Person 1: Data Preprocessing
    print("\n Data Preprocessing")
    print("-" * 40)
    item_counts, sorted_transactions = preprocess_data(transactions, min_support)
    print("Item Counts:", item_counts)
    print("Sorted Transactions:", sorted_transactions)

    # Person 2: FP-Tree Construction
    print("\n FP-Tree Construction")
    print("-" * 40)
    fp_tree, header_table = build_fp_tree(sorted_transactions, min_support)
    print("FP-Tree Root:", fp_tree.item if fp_tree else "None")
    print("Header Table Items:", list(header_table.keys()))

    # Person 3: Pattern Mining
    print("\n Pattern Mining")
    print("-" * 40)
    frequent_patterns = mine_patterns(header_table, min_support)

    print("\nFrequent Patterns Found:")
    print("-" * 25)
    for item, patterns in frequent_patterns.items():
        print(f"Item {item}:")
        for path, count in patterns:
            print(f"  Pattern: {path} (Support: {count})")


if __name__ == "__main__":
    main()
