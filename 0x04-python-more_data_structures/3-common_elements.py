#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return the common elements between 2 sets
    Args:
        set_1 - Set one
        set_2 - Set two
    """
    return set_1.intersection(set_2)


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
