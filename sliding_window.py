def shrinkableWindow(nums):
    l_ptr = ans = 0

    for r_ptr, num in enumerate(nums):
        # code using num to update the state 
        # that might invalidate the window
        while invalid():
            # code using nums[l_ptr] to update the state
            # and shrink the left edge while the window is invalid
            l_ptr += 1
        # longest window so far = len([i, j])
        ans = max(ans, r_ptr - l_ptr + 1)

    return ans

def unshrinkableWindow(nums):
    l_ptr = 0

    for r_ptr, num in enumerate(nums):
        # code using num to update the state 
        # that might invalidate the window
        if invalid():
            # code using nums[l_ptr] to update the state
            # and shift the window sideways. 
            # the window grows if the state is valid 
            # and shifts if it's invalid.
            l_ptr += 1
        
    # the maximum size of the window
    return r_ptr - l_ptr