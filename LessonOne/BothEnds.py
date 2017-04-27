# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    # +++your code here+++
    return "".join((s[:2], s[-2:])) if len(s) > 2 else ''

# Provided simple test() function used in main() to print
# what each function returns what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('Goodbye'), 'Goye')
    test(both_ends('xyz'), 'xyyz')
    test(both_ends('LaGracia'), 'Laia')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
