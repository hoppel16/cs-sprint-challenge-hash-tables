def get_indices_of_item_weights(weights, length, limit):
    weight_cache = {}

    for index, weight in enumerate(weights):
        weight_cache[weight] = index

    for first_weight_index in range(0, length):
        weight = weights[first_weight_index]

        if limit - weight in weight_cache:
            second_weight_index = weight_cache[limit - weight]
            if first_weight_index is second_weight_index:
                continue
            result = [first_weight_index, second_weight_index]
            return sorted(result, reverse=True)

    return None


if __name__ == "__main__":
    weights = [1, 3, 5, 7, 12, 16]
    print(get_indices_of_item_weights(weights, len(weights), 15))
