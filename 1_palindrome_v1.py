'''
Algorithm 1: Reverse string.
Compare the reversed string to original string.
'''

def is_palindrome_v1(s):
    ''' (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    '''
    return reverse(s) == s

def reverse(s):
    ''' (str) -> str

    Return a reversed version  of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    '''
    rev = ''

    # For each  character in s, a dd that char to beginning of rev.
    for c in s:
        rev = c + rev
    return rev
