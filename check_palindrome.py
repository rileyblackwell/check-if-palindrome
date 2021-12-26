def is_pal(word):
    """ -assumes 
            word is a string  
            word maintains case sensitivity throughout (all upper or all lower)
            word contains no spaces 
    """
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_pal(word[1:-1])


# 2 required test cases palindrome True and palindrome False
# test case: palindrome True
word = 'anabana'

print(is_pal(word))

# test case: palindrome False
word = 'banana'

print(is_pal(word))

# expected output from test cases: 
# True
# False



