import os

# Dictionary of folder names and their content
content = {
    "basics": "# 🧱 Basics & Math\nFoundational concepts to build a strong base for DSA.\n\n## 🔑 Key Concepts\n- **Time & Space Complexity** (Big O analysis)\n- **Basic Hashing** (Frequency counting)\n- **Basic Math** (GCD, Divisors, Prime numbers)\n- **Recursion Basics** (Factorial, Fibonacci)",
    "sorting": "# 🧹 Sorting Algorithms\nUnderstanding how to organize data efficiently.\n\n## 🔑 Key Concepts\n- **Basic Sorts:** Selection, Bubble, Insertion ($O(N^2)$)\n- **Advanced Sorts:** Merge Sort, Quick Sort ($O(N \\log N)$)\n- **Recursive Sorting:** Recursive Bubble & Insertion Sort",
    "arrays": "# 📊 Arrays\nThe most fundamental data structure.\n\n## 🔑 Key Concepts\n- **Two Pointers** & Sliding Window\n- **Kadane's Algorithm** (Max Subarray Sum)\n- **Dutch National Flag** (Sort 0, 1, 2)\n- **Matrix / 2D Array** manipulation",
    "binary_search": "# 🔍 Binary Search\nOptimized searching in sorted spaces ($O(\\log N)$).\n\n## 🔑 Key Concepts\n- **1D Arrays:** Lower Bound, Upper Bound\n- **2D Arrays:** Row-col sorted matrices\n- **Search on Answers:** Book Allocation, Aggressive Cows",
    "strings": "# 🧵 Strings\nText processing and manipulation techniques.\n\n## 🔑 Key Concepts\n- **Basic:** Palindromes, Reverse words\n- **Medium:** Longest Palindromic Substring\n- **Hard:** Roman to Integer, ATOI",
    "linked_lists": "# 🔗 Linked Lists\nDynamic data structures involving nodes and pointers.\n\n## 🔑 Key Concepts\n- **Single LL:** Reverse, Middle, Merge\n- **Doubly LL:** Insert, Delete, Reverse\n- **Hard:** Detect Loop, LRU Cache",
    "recursion": "# 🔄 Recursion\nSolving problems by breaking them down.\n\n## 🔑 Key Concepts\n- **Subsequences:** Power Set\n- **Combination Sum:** Patterns I, II, III\n- **Backtracking:** N-Queens, Sudoku Solver",
    "bit_manipulation": "# 💡 Bit Manipulation\nLow-level binary operations.\n\n## 🔑 Key Concepts\n- **Operators:** XOR, AND, OR, Shifts\n- **Tricks:** Power of 2, Count set bits\n- **Advanced:** Single Number, XOR range",
    "stacks_queues": "# 📚 Stacks & Queues\nLIFO and FIFO structures.\n\n## 🔑 Key Concepts\n- **Implementation:** Arrays vs Linked Lists\n- **Monotonic Stack:** Next Greater Element\n- **Hard:** Largest Rectangle in Histogram",
    "sliding_window": "# 🪟 Sliding Window\nOptimizing nested loops.\n\n## 🔑 Key Concepts\n- **Fixed Size:** Max sum subarray\n- **Variable Size:** Longest Substring Without Repeats\n- **Advanced:** Minimum Window Substring",
    "heaps": "# 🏔️ Heaps\nPriority Queues for min/max access.\n\n## 🔑 Key Concepts\n- **Basics:** Min-Heap, Max-Heap\n- **Patterns:** Kth Largest Element\n- **Advanced:** Median from Data Stream",
    "greedy": "# 🤑 Greedy Algorithms\nLocally optimal choices.\n\n## 🔑 Key Concepts\n- **Scheduling:** N Meetings\n- **Knapsack:** Fractional Knapsack\n- **Logic:** Jump Game, Candy Problem",
    "binary_trees": "# 🌳 Binary Trees\nHierarchical structures.\n\n## 🔑 Key Concepts\n- **Traversals:** Inorder, Preorder, Postorder, BFS\n- **Views:** Top, Bottom, Left, Right\n- **Hard:** LCA, Diameter, Max Path Sum",
    "bst": "# 🌿 Binary Search Trees\nOrdered trees for efficient lookup.\n\n## 🔑 Key Concepts\n- **Operations:** Search, Insert, Delete\n- **Logic:** Ceil/Floor, Kth Smallest",
    "graphs": "# 🕸️ Graphs\nNodes and edges.\n\n## 🔑 Key Concepts\n- **Traversals:** BFS, DFS\n- **Shortest Path:** Dijkstra, Bellman-Ford\n- **MST:** Prim's, Kruskal's\n- **DSU:** Disjoint Set Union",
    "dp": "# ⚡ Dynamic Programming\nOptimization by caching.\n\n## 🔑 Key Concepts\n- **1D DP:** Climbing Stairs, Frog Jump\n- **2D DP:** Ninja's Training, Grid Paths\n- **Subsequences:** LCS, Knapsack",
    "tries": "# 🌲 Tries\nPrefix trees for string search.\n\n## 🔑 Key Concepts\n- **Basics:** Insert, Search, StartsWith\n- **Advanced:** Longest Word with All Prefixes"
}

# Loop through dictionary and write files
for folder, text in content.items():
    # Create folder if it doesn't exist (safety check)
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Write the README.md file
    with open(f"{folder}/README.md", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Created README for {folder}")