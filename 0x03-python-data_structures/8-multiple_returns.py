#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns the length of a str & it's first letter
    Args:
        sentence - String
    Return:
        (length, first_char)
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]


if __name__ == '__main__':
    l, f = multiple_returns("At school, i learnt C!")
    print("Length: {:d} - First character: {}".format(l, f))
