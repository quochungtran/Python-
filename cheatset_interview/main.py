"""
******** TWO POINTER ********
"""
# one input, opposite ends
def fn(arr: list) -> list:
    left = ans = 0
    right = len(arr)-1

    while(left < right):
        if CONDITION:
            left += 1
        else:
            right -= 1
    return ans

# two inputs: exhaust both
def fn(arr1: list, arr2: list):
    i = j = ans = 0

    while(i < len(arr1) and j < len(arr2)):
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # dologic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1

    return ans

"""
******** SLIDING WINDOW ********
"""
def fn(arr: list):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1
        
        # update ans
    return ans

"""
PREFIX SUM
"""
def fn(arr: list):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

"""
Efficient string building
"""
def fn(arr: list)->str:
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)

"""
Linked-list: fast and flow pointer
"""
def fn(head):
    slow = head
    fast = head 
    ans = 0
    while(fast and fast.next):
        # do logic
        slow = slow.next
        fast = fast.next.next
    
    return ans

"""
Reverse Linked-list
"""
def fn(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

"""
Find number of subarray that fits exact the criteria
idea basiclly came from prefix sum
"""
from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans

"""
Monotonic increasing stack
"""
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for decreasing just flip from > to <
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return ans

"""
Binary Tree: DFS(recursive)
"""
def dfs(root):
    if not root:
        return 
    ans = 0
    dfs(root.left)
    dfs(root.right)

    return ans

"""
Binary tree: DFS (iterative)
"""
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return ans

"""
Binary tree: BFS
"""
from collections import deque

def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        curr_len = len(queue)
        # do logic for curr level

        for _ in range(curr_len):
            node = queue.popleft()
            # do logic

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

"""
Graph: DFS (recursive)
"""
def fn(graph):
    def dfs(node):
        ans = 0
        # do logic

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)
        
        return ans

    seen = {START_NODE}
    return dfs(START_NODE)

"""
Graph: DFS (iterative)
"""
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans

"""
Graph: BFS
"""

def fn(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in graph:
                seen.add(neighbor)
                queue.append(neighbor)

    return ans

"""
Find top k elements with heap
"""
import heapq

def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's critea
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for num in heap]

"""
Binary search
"""
def fn(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            # do sth
            return 
        if arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    
    return left

# duplicate elements, left most

def fn(arr, target):
    left = 0
    right = len(arr) -1 
    while(left < right):
        mid = (left + right) // 2
        if arr[mid] <= target:
            right = mid
        else:
            left = mid+1
    
    return left

# duplicate elements, right most insection point
def fn(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid+1
    return left

"""
Backtracking
"""

def backtrack(curr, other_arg):
    if (BASE_CASE):
        # modify the answer
        return
    
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify the current state
        ans += backtrack(curr, other_arg)
        # undo the modification

    return ans

"""
Dynamic programming: top-down memoization
"""
def fn(arr):
    def dp(STATE):
        if BASE_STATE:
            return 0

        if STATE in memo:
            return memo[STATE]

        ans = RECURRENCE_RELATION(STATE)
        memo[STATE]= ans
        return ans
    
    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)

"""
Trie
"""

class TrieNode:
    def __init__(self):
        self.data = None
        self.children = {}

def fn(words):
    root = TrieNode()
    for word in words:
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
    
    return root

"""
Dijkstra algo
"""

from math import inf
from heapq import *

distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heappop(heap)
    if curr_dist > distances[node]:
        continue

    for nei, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[nei]:
            distances[nei] = dist
            heapq.heappush(heap, (dist, nei))