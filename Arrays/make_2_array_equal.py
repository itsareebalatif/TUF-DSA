def main():
    targets = [1, 2, 3]
    arrs = [3, 2,4]
    a=canBeEqual(targets,arrs)
    print(a)

def equal_array(target,arr):
    if len(target)==len(arr):
        return False
    target.sort()
    arr.sort()
    for i in range(len(target)):
        if target[i]!=arr[i]:
            return False        
    return True


def canBeEqual(target,arr) :  
    from collections import Counter
    
    # Count the frequency of each element in both arrays
    target_count = Counter(target)
    arr_count = Counter(arr)
    
    # Compare the two frequency counts
    return target_count == arr_count

if __name__=="__main__":
    main()
