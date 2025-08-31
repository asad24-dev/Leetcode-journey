def find_median(a, b):
    a_pointer = 0
    b_pointer = 0
    curr_length = 0
    isEven = (len(a) + len(b)) % 2 == 0
    prev1 = float('-inf')
    prev2 = 0
    while((a_pointer < len(a) or b_pointer < len(b)) and (curr_length <= ((len(a) + len(b)) / 2))):
        if (b_pointer>=len(b) or a[a_pointer] <= b[b_pointer]):
            prev2 = prev1
            prev1 = a[a_pointer]
            print(f"Current elements: {prev1}, {prev2}")
            a_pointer += 1
        elif (a_pointer>=len(a) or b[b_pointer] < a[a_pointer]):
            prev2 = prev1
            prev1 = b[b_pointer]
            print(f"Current elements: {prev1}, {prev2}")
            b_pointer += 1
        curr_length += 1
        print(f"Current length: {curr_length}, a_pointer: {a_pointer}, b_pointer: {b_pointer}")
    if isEven:
        return (prev1 + prev2) / 2
    return prev1

a = [1, 5, 7]
b = [2, 3, 10]
#[1,2,3,5,7,10] median = 4
print(find_median(a,b))