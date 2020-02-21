'''
Algorithm 3:
    Compare  1st char to last char
    Compare 2nd char to second last char
    Stop  when middle of string is reached
'''
def is_palindrome_v3(s):
    ''' (str) -> bool

    Return True if and only  if s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    '''
    i = 0
    j = len(s) - 1
    # Only palindrome if middle of string is reached
    # for odd string, middle is reached when i = j
    # for even string, we stop when j <= i
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return j <= i
