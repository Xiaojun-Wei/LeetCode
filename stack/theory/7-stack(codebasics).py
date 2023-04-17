from collections import deque


"""
1. Write a function in python that can reverse a string using stack data structure.
"""


def reverse_string(sent):
    s = deque()
    for char in sent:
        s.append(char)
    reversed_str = ""
    while len(s) != 0:
        reversed_str += s.pop()

    return reversed_str


"""
2. Write a function in python that can reverse a string using stack data structure.
"""
paranthesis_dict={'(':')','[':']','{':'}'}

def is_balanced(string):
    d = deque()
    for char in string:
        if char in paranthesis_dict:
            if paranthesis_dict[char] in string:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    print(reverse_string("hello world"))
    print(is_balanced("({a+b})"))

