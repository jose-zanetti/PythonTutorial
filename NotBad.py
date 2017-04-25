# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    n = 'not'
    b = 'bad'
    g = 'good'

    if n in s and b in s and s.rfind(n) < s.rfind(b):
        s = ''.join((s[:s.rfind(n)], g, s[s.rfind(b) + len(b):]))
    return s

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
    test(not_bad("It's bad yet not, is not so bad!!"), "It's bad yet not, is good!!")
  
if __name__ == '__main__':
    main()
