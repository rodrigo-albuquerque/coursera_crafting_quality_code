'''
Algorithm 2:
    Split string in 2 halves
    Reverse second half
    Compare first half to reversed second half.

    len(s)//2 gives is the number of characters for each slice
    We can use this result as the last index in the slice in order to grab the first half of the string
    We can take len(s) - len(s)//2 to find index of first character in 2nd half of the string/
'''
def is_palindrome_v2(s):
    ''' (str) -> bool

    Return True if and only  if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    '''
    # Assuming, n = len(s)
    # s[:n//2] = first half
    # s[n - n//2:] = second half <- we want to reverse this and check if it's the same as first half
    # We're comparing first  half ofs to reverse of second half.
    # We're also  omitting the middle character of odd-length string.
    n = len(s)
    return s[:n // 2] == reverse(s[n-n // 2:])

def reverse(s):
    ''' (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    '''
    rev =  ''
    # For each character in s, add that char to the beginning of rev.
    for c in s:
        rev = c + rev
    return rev
