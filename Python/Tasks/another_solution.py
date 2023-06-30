def find_max(lst):
    max = lst[0]
    for num in lst:
        for i in lst:
            if num < i:
                break
        else:
            max = num
    return max

#def find_max(lst):
    # return sorted(lst)[-1]


def remove_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                del lst[j]
    return lst

# def remove_duplicates(lst):
#     return list(set(lst))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# def factorial(n):
#     result = 1
#     while n > 0:
#         result = result * n
#         n -= 1
#     return result