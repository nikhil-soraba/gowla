def check(k) -> bool:
    pass # if conditions met, return True; Otherwise, return False

left, right = 1, 10 # [left,right)

while left < right:
    mid = left + (right - left) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid
# return left     # If min that doesn't satisfy the check is needed
# return left - 1 # If max that       satisfies the check is needed
