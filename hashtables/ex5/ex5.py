# Your code here



def finder(files, queries):
    result = []
    query_cache = {}

    for query in queries:
        if query not in query_cache:
            query_cache[query] = 0
        query_cache[query] += 1

    for file in files:
        file_query = file.split("/")[-1]
        if file_query not in query_cache:
            continue
        result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
