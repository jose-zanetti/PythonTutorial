def remove_adjacent(nums):
    
    return [num for i, num in enumerate(nums) if num != nums[i-1]]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([1, 2, 2, 2, 4, 6, 6, 3, 6]), [1, 2, 4, 6, 3, 6])

if __name__ == '__main__':
    main()