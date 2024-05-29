lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8


def two_sum(lst, target):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if target == lst[i] + lst[j]:
                return (i, j)

def two_sum_hashed(lst, target):
    dict = {}
    negativeDict = {}
    tempDict = {}
    for k in range(len(lst)):
        dict[k] = lst[k]
    for k in range(len(lst)):
        negativeDict[k] = target - dict[k]
    for k in range(len(lst)):
        num = negativeDict.get(k)
        value = list(dict.values())
        keys = list(dict.keys())
        if num in value[k + 1:len(lst)]:
            num = value.index(num, k + 1, len(lst))
            keyValue = keys.pop(num)
            tempDict.setdefault(k, [keyValue])
    finalDict = tempDict.items()
    print(finalDict)

if __name__ == "__main__":
    print(two_sum_hashed(lst, target))
