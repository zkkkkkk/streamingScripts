import sys

for line in sys.stdin:
    line = line.strip()
    friends_l = line.split(" ")
    for i in range(len(friends_l)-1):
        results = [friends_l[i+1], friends_l[0]]
        print("\t".join(results))
