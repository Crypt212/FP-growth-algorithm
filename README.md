# FP-Growth Algorithm

A modular implementation of the FP-Growth algorithm for frequent pattern mining in transactional datasets.

## Overview

FP-Growth (Frequent Pattern Growth) is an efficient algorithm for mining frequent itemsets without candidate generation. It compresses the database into a frequent-pattern tree (FP-tree) and extracts patterns directly from this compressed structure.

## Algorithm Workflow

### Step 1: Data Preprocessing
**Module: `data_preprocessor.py`**

- **Count Item Frequencies**: Calculate support count for each item across all transactions
- **Filter Infrequent Items**: Remove items below the minimum support threshold  
- **Sort Transactions**: Order items by descending frequency within each transaction

**Input**: Raw transactions  
**Output**: Frequency counts and sorted transactions

### Step 2: FP-Tree Construction
**Module: `fp_tree_builder.py`**

- **Build Tree Structure**: Create a compressed prefix tree where shared transaction prefixes are merged
- **Node Links**: Connect nodes containing the same item via linked lists for efficient traversal
- **Header Table**: Maintain index of first occurrence of each item for quick access

**Input**: Sorted transactions  
**Output**: FP-tree structure and header table

### Step 3: Pattern Mining  
**Module: `pattern_miner.py`**

- **Conditional Pattern Bases**: Extract all paths leading to each item from the FP-tree
- **Recursive Mining**: Build conditional FP-trees for frequent pattern discovery
- **Pattern Generation**: Combine items with their conditional patterns to generate complete frequent itemsets

**Input**: FP-tree and header table  
**Output**: All frequent patterns with their support counts

## Quick Start

```python
from data_preprocessor import preprocess_data
from fp_tree_builder import build_fp_tree
from pattern_miner import mine_patterns

# Sample market basket data
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

min_support = 2  # Items must appear in at least 2 transactions

# Execute FP-Growth pipeline
item_counts, sorted_trans = preprocess_data(transactions, min_support)
fp_tree, header_table = build_fp_tree(sorted_trans, min_support)
frequent_patterns = mine_patterns(header_table, min_support)

# Display results
for item, patterns in frequent_patterns.items():
    for path, count in patterns:
        print(f"{path + [item]}: {count}")
