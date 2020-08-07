def intersection(arrays):
    result = []

    elem_cache = {}

    for array in arrays:
        for elem in array:
            if elem not in elem_cache:
                elem_cache[elem] = 0
            elem_cache[elem] += 1
            if elem_cache[elem] == len(arrays):
                result.append(elem)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
