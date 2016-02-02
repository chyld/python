# lists

odds = [3, 5, 7]
odds.append(9)          # added individually
odds.append(11)         # added individually
odds.extend([13, 15])   # spread out before added
odds += [17, 19]        # same as extend

print('odds:', odds)
odds.remove(17)
print('length of odds:', len(odds))
