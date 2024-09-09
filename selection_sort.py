arr = list(eval(input()))
for i in range(len(arr)):
    min = i
    for j in range(i, len(arr)):
        if arr[j]<=arr[min]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]
print(arr)
