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


print(merge(intervals))