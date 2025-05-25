"""
wiki: https://en.wikipedia.org/wiki/Anagram
"""

from collections import defaultdict

def check_anagrams(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made up of the same letters but are
    arranged differently (ignoring the case).
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('This is    a      string', 'Is     this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    first_str = first_str.lower().strip()
    second_str = second_str.lower().strip()
    
    # remove space
    first_str = first_str.replace(" ", "")
    second_str = second_str.replace(" ", "")

    if len(first_str) != len(second_str):
        return False

    # 26 alphabets from a to z
    count = [0] * 26

    for i in range(len(first_str)):
        count[ord(first_str[i]) - ord('a')] += 1
        count[ord(second_str[i]) - ord('a')] -= 1
    
    return all(_count == 0 for _count in count)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_a = input("Enter the first string ").strip()
    input_b = input("Enter the second string ").strip()

    # string is immutable object, so if we pass a string as argument to a function
    # and modify it within function, the global var will be not changed
    status = check_anagrams(input_a, input_b)
    print(f"{input_a} and {input_b} are {'' if status else 'not '}anagrams.")