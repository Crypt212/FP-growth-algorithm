class FPTreeNode:
    """
    Represents a node in the FP-Tree structure
    Each node tracks an item, its count, and connections to other nodes
    """

    def __init__(self, item, count=1):
        self.item = item      # The item this node represents (None for root)
        self.count = count    # How many transactions contain this path
        self.children = {}    # Child nodes: {item: FPTreeNode}
        self.parent = None    # Reference to parent node
        self.link = None      # Link to next node with same item (for traversal)

    def increment(self, count=1):
        """Increase the count of this node"""
        self.count += count


def build_fp_tree(transactions, min_support):
    """
    Construct the FP-Tree from sorted transactions
    The tree compresses transaction data while preserving frequency information
    """
    # Create root node (has no item, serves as tree starting point)
    root = FPTreeNode(None, 1)

    # Header table: maps items to their first occurrence in tree
    # Used for efficient pattern mining later
    header_table = {}

    # Process each transaction to build the tree
    for transaction in transactions:
        current_node = root  # Start at root for each new transaction

        # Add each item in the transaction to the tree
        for item in transaction:
            # If current node already has this item as a child
            if item in current_node.children:
                # Just increment the count (path already exists)
                current_node.children[item].increment()
            else:
                # Create new node for this item
                new_node = FPTreeNode(item)
                new_node.parent = current_node  # Set parent reference

                # Add new node as child of current node
                current_node.children[item] = new_node

                # Update header table with links to nodes of same item
                if item in header_table:
                    # Item exists in header table, find end of linked list
                    current = header_table[item]
                    while current.link:  # Traverse to last node in chain
                        current = current.link
                    current.link = new_node  # Add new node to end of chain
                else:
                    # First time seeing this item in header table
                    header_table[item] = new_node

            # Move down the tree to process next item
            current_node = current_node.children[item]

    return root, header_table
