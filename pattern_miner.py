def find_prefix_path(item, node):
    """
    Extract all paths that lead to a given item (conditional pattern base)
    Returns list of (path, count) pairs where path leads to the target item
    """
    cond_patterns = []  # Store conditional patterns for this item

    # Traverse all nodes that contain this item (via header table links)
    while node:
        path = []  # Will store the path from root to this node (excluding the item itself)
        parent = node.parent  # Start from current node's parent

        # Traverse up the tree to collect all ancestors
        while parent and parent.item:  # Stop at root (which has no item)
            path.append(parent.item)   # Add parent's item to path
            parent = parent.parent     # Move up to next parent

        path.reverse()  # Reverse to get path from root to node (correct order)

        # Only add non-empty paths (exclude direct root-to-item paths)
        if path:
            # Store the path and how many transactions follow this path
            cond_patterns.append((path, node.count))

        # Move to next node with the same item (via header table linking)
        node = node.link

    return cond_patterns


def mine_patterns(header_table, min_support):
    """
    Mine all frequent patterns from the FP-Tree using conditional pattern bases
    """
    frequent_patterns = {}  # Will store {item: [(conditional_patterns)]}

    # Process items in ascending order of frequency (least frequent first)
    # This bottom-up approach ensures we find all combinations
    for item in sorted(header_table.keys(), key=lambda k: header_table[k].count):
        # Get all paths that lead to this item (conditional pattern base)
        cond_patterns = find_prefix_path(item, header_table[item])

        # Merge duplicate paths and sum their counts
        merged_patterns = {}
        for path, count in cond_patterns:
            # Convert list to tuple so it can be used as dictionary key
            path_tuple = tuple(path)

            # If we've seen this path before, add to its count
            if path_tuple in merged_patterns:
                merged_patterns[path_tuple] += count
            else:
                # New path, initialize with its count
                merged_patterns[path_tuple] = count

        # Convert back to list format and store with the target item
        frequent_patterns[item] = [(list(path), count)
                                   for path, count in merged_patterns.items()]

    return frequent_patterns
