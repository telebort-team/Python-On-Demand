def even_only(x):
    evens = []
    for item in x:
        if item % 2 == 0:
            evens.append(item)
    return evens


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = even_only(numbers)
print(result)
