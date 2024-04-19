from collections import defaultdict

T = lambda: defaultdict(T)
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/solutions/4744547/javacpython-trie/
root = (T := lambda: defaultdict(T))()
