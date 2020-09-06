A = [-1, 1,2,3,4,5,6,7,8,9,10, 101]

def binary_search(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = (right+left) // 2
        if haystack[mid] < needle:
            left = mid + 1
        elif haystack[mid] > needle:
            right = mid - 1
        else:
            # print(f"L={left}\tR={right}\tM={mid}") 
            return mid  
        # print(f"L={left}\tR={right}\tM={mid}")             
    raise ValueError(f"Value {needle} not in haystack")
