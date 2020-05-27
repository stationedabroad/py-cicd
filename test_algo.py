from binary_search import binary_search

def test_search_first():
    assert(binary_search(0, [0, 1, 2, 3, 4, 6, 7, 10]) == 0), "Found needle somewhere in haystack"

def test_search_last():
    assert(binary_search(10, [0, 1, 2, 3, 4, 6, 7, 10]) == 7), "Found needle somewhere in haystack"    

def test_value_not_found():
    try:
        _ = binary_search(100, [0, 1, 2, 3, 4, 6, 7, 10])
    except ValueError as e:
        print(type(e), e)
        assert isinstance(e, ValueError), "Not Found needle somewhere in haystack"
