

def find_all_max_position(arr):
    start = 0 
    end = len(arr) - 1
    max_index = find_max(arr, start, end) 
    start = max_index
    res = [max_index]

    while start < end:
        print res
        next_max = find_next_max(arr, start, end, arr[start])
        if next_max == -1 or next_max == end:
            break

        if arr[next_max + 1] > arr[next_max]:
            res = []
            max_index = find_max(arr, next_max, end)
            start = max_index
            res.append(max_index)
        else:
            res.append(next_max)
            start = next_max

    return res

def find_max(arr, start, end):
    base = start 
    while base + 1 <= end:
        if arr[base+1] > arr[base]:
            base += 1
        else:
            break
    return base

def find_next_max(arr, start, end, target):
    start = start + 1
    i = abs(target - arr[start])

    while start < end:
        try:
            # print target, start, arr[start + i], i
            if arr[start + i] == target:
                return start + i 
            else:
                new_start = start + i 
                i = abs(target - arr[start + i])
                start = new_start
        except:
            break
            print "index out of"
    return -1

arr = [4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 5, 6, 7, 8, 7, 6, 7, 8, 9, 10]*10
print 'len', len(arr)
print find_all_max_position(arr)
