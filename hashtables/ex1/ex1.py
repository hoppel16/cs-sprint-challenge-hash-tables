def get_indices_of_item_weights(weights, length, limit):
    for ind1 in range(0, length):
        if ind1 + 1 >= length:
            break
        for ind2 in range(ind1+1, length):
            if weights[ind1] + weights[ind2] is limit:
                return ind2, ind1

    return None


if __name__ == "__main__":
    weights = [1, 3, 5, 7, 12, 16]
    print(get_indices_of_item_weights(weights, len(weights), 15))
