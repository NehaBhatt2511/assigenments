def binarys(li, n):
    if n not in li:
        print("not found")

    else:
        start = 0
        end = len(li) - 1
        while start < end:
            mid = (start + end) // 2
            if li[mid] == n:
                print(mid)
                break
            elif li[mid] < n:
                start = mid + 1
            else:
                end = mid - 1


list1 = [1, 2, 3, 4, 4, 5, 6, 7, 8]
print(binarys(list1, 2))
