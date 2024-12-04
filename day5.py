order, updates = open('day5.txt').read().split('\n\n') # change this line to read the file from path
pairs = [p.split('|') for p in order.splitlines()]

def after(x): return [a for a,b in pairs if x==b]
def index(x, nums): return len(set(after(x)).intersection(nums))

was_sorted = {True: [], False: []}
for nums in [x.split(',') for x in updates.splitlines()]:
    nums2 = sorted(nums, key=lambda x: index(x, nums=nums))
    was_sorted[nums == nums2].append(nums2)

answer = [sum(int(nums[len(nums)//2]) for nums in part) for part in was_sorted.values()]
print(f"part 1 and part 2 answer is {answer}")