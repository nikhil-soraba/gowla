# Inclusive prefix sum
pre_sum, prev = [], 0

for num in arr:
    prev += num
    pre_sum.append(prev)

# Exclusive prefix sum
pre_sum, prev = [], 0

for num in arr:
    pre_sum.append(prev)
    prev += num
