import sys
import itertools

current_friend = None
common_friend_l = []

for line in sys.stdin:

    line = line.strip()
    common_friend, friend = line.split("\t")

    if not current_friend:
        current_friend = common_friend

    if current_friend == common_friend:
        common_friend_l += friend

    else:
        common_friend_l = list(set(common_friend_l))
        for j in itertools.combinations(common_friend_l, 2):
            print(",".join(str(v) for v in list(j)) + " " + current_friend)
        current_friend = common_friend
        common_friend_l = [friend]

common_friend_l = list(set(common_friend_l))
for j in itertools.combinations(common_friend_l, 2):
    print(",".join(str(v) for v in list(j)) + " " + current_friend)
    
