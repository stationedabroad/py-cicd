from binary_search import binary_search

def test_search():
    assert(binary_search(7, [0, 1, 2, 3, 4, 6, 7, 10]) == 6), "Found needle somewhere in haystack"
    assert(binary_search(1, [0, 1, 2, 3, 4, 6, 7, 10]) == 1), "Found needle somewhere in haystack"
    assert(binary_search(7, [0, 1, 2, 3, 4, 6, 7, 10]) == 6), "Found needle somewhere in haystack"
    try:
        _ = binary_search(100, [0, 1, 2, 3, 4, 6, 7, 10])
    except ValueError as e:
        print(type(e), e)
        assert isinstance(e, ValueError), "Not Found needle somewhere in haystack"
