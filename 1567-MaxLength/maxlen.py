def getMaxLen(nums):
    start = 0
    first_neg = -1
    last_neg = -1
    neg_count = 0
    maxlen = 0

    for i, num in enumerate(nums):
        if num == 0:
            # process current chunk [start .. i-1]
            if neg_count % 2 == 0:
                maxlen = max(maxlen, i - start)
            else:
                maxlen = max(maxlen, i - first_neg - 1, last_neg - start)
            # reset for next chunk
            start = i + 1
            first_neg = -1
            last_neg = -1
            neg_count = 0
        else:
            if num < 0:
                neg_count += 1
                if first_neg == -1:
                    first_neg = i
                last_neg = i

    # don’t forget the last chunk after loop
    if neg_count % 2 == 0:
        maxlen = max(maxlen, len(nums) - start)
    else:
        maxlen = max(maxlen, len(nums) - first_neg - 1, last_neg - start)
    return maxlen
print(getMaxLen([1,2,3,5,-6,4,0,10, -2, -3, 5, 4, -1]))  # Output: 2