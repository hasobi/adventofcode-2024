import numpy as np

data = np.loadtxt('day1.txt', dtype=int)
column1 = data[:, 0].tolist()
column2 = data[:, 1].tolist()

print("Day 1, Part 1 ", np.sum(np.abs(np.array(sorted(column1)) - np.array(sorted(column2)))))
print("Day 1, Part 2 ", sum([column1.count(key) * column2.count(key) * key for key in set(column1)]))