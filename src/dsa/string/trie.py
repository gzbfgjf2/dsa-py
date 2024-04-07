from collections import defaultdict

T = lambda: defaultdict(T)
root = (T := lambda: defaultdict(T))()
