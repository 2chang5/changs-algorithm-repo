
def main (array,find_item):

    left, right = 0, len(array)-1

    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] > find_item:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer



print(main([1,2,3,3,5,6,8,8,8,10],8))