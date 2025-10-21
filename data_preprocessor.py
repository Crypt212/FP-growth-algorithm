def count_item_frequency(transactions):
    """
    Count how often each item appears across all transactions
    """
    item_counts = {}  # Dictionary to store item: frequency pairs
    
    # Process each transaction in the dataset
    for transaction in transactions:
        # Examine each item within the current transaction
        for item in transaction:
            # If we've seen this item before, increment its count
            if item in item_counts:
                item_counts[item] += 1
            else:
                # First time seeing this item, initialize count to 1
                item_counts[item] = 1
    return item_counts


def sort_transactions(transactions, item_counts, min_support):
    """
    Clean and sort transactions by item frequency (descending)
    """
    sorted_transactions = []  # Will hold our processed transactions
    
    for transaction in transactions:
        # Filter out infrequent items and sort by frequency
        sorted_transaction = sorted(
            # Keep only items that meet minimum support threshold
            [item for item in transaction if item_counts[item] >= min_support],
            # Sort items by their frequency count (most frequent first)
            key=lambda item: item_counts[item],
            reverse=True  # Descending order (high to low frequency)
        )
        # Add the processed transaction to our results
        sorted_transactions.append(sorted_transaction)
    return sorted_transactions


def preprocess_data(transactions, min_support):
    """
    Main preprocessing pipeline: count frequencies and sort transactions
    """
    # Step 1: Calculate how often each item appears
    item_counts = count_item_frequency(transactions)
    
    # Step 2: Sort transactions and remove infrequent items
    sorted_transactions = sort_transactions(transactions, item_counts, min_support)
    
    return item_counts, sorted_transactions
