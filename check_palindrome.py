def is_pal(word):
    """ -assumes that word is a string  
    
    """
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_pal(word[1:-1])

# test case: palindrome
word = 'anabana'

print(is_pal(word))

# test case: not palindrome
word = 'banana'

print(is_pal(word))

# expected output from test cases: 
# True
# False
# test

