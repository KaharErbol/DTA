def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = []
    for each in intervals:
        if not res or each[0] > res[-1][1]:
            res.append(each)
        else:
            res[-1][1] = max(res[-1][1], each[1])
    
    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals_2 = [[1,3],[2,6],[8,10],[15,18]]


print("1: ", merge(intervals))

def merge_2(intervals):
    intervals.sort(key = lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]

    res = []

    for i in range(len(intervals)):
        cur = intervals[i]
        if cur[0] > end:
            res.append([start, end])
            start = cur[0]
            end = cur[1]
        else:
            if cur[1] > end:
                end = cur[1]
    res.append([start, end])
    return res

print("2: ", merge_2(intervals_2))