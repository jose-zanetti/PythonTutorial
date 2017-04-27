def mix_up(a, b):
    
    return " ".join(("".join((b[:2], a[2:])), "".join((a[:2], b[2:]))))

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()