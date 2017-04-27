def sort_last(tuples):
    return sorted(tuples, key= lambda getKey: getKey[1])

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]), 
       [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
    main()