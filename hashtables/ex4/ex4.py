def has_negatives(a):
    result = []
    number_cache = {}

    for number in a:
        if number not in number_cache:
            number_cache[number] = 0
        number_cache[number] += 1

        if number * -1 in number_cache and abs(number) not in result:
            if number is 0:
                if number_cache[number] < 2:
                    continue
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
