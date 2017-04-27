# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    # +++your code here+++
    i = 'ing'
    y = 'ly'
    return s if len(s) < 3 else ("".join((s, i)) if s[-3:] != i  else "".join((s, y)))  

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    test(verbing('paingt'), 'paingting')

if __name__ == '__main__':
    main()
