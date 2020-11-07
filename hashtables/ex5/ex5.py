# Your code here



def finder(files, queries):
    """
    Given list of file paths and queries, return list of paths to queries
    """
    # Init dict with queries keyed
    # For each query, search appropriately-sized slices of file strings for matches
    # If match, add file path to dict as list value

    file_dict = {j: [] for j in queries}

    for q in queries:
        for f in files:
            if q == f[len(q)*-1:]:
                file_dict[q].append(f)
    
    result = []
    for q in queries:
        for path in file_dict[q]:
            result.append(path)

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
