# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
my_list = [1, 5, 'apple', 20.5]
print(my_list[2])
my_list.append(10)
print(my_list)
my_list.remove(20.5)
print(my_list)
my_list.reverse
print(my_list)

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
person = {'name' : 'John' , 'age' : '30' , 'job' : 'teacher'}
print(person['job'])
person['city'] = 'Paris'
print(person)
del person['age']
for key, value in person.items():
    print(f"{key}: {value}")

# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:

    vowels = "aeiouAEIOU"
    vowel_count = 0
    for letter in s:
        if letter in vowels: 

            vowel_count += 1
    return vowel_count
      
        

    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    pass

    

def extend_list(list_to_extend_into, list_to_append_items_from):
    for item in list_to_append_items_from:
        list_to_extend_into.append(item)
    return list_to_extend_into

def extend_list_with_partial_list(list_to_extend_into, list_to_append_items_from, first_index_to_append_from):
    items_to_append = list_to_append_items_from[first_index_to_append_from:]
    for item in items_to_append:
        list_to_extend_into.append(item)
    return list_to_extend_into


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    pass
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # # for loop
    if not list1:
        return list2
    if not list2:
        return list1
    merged_list = []
    i1, i2 = 0, 0
    while len(merged_list) < len(list1) + len(list2):
        if list1[i1] < list2[i2]:
            merged_list.append(list1[i1])
            if i1+1 == len(list1):
                for item in list2[i2:]:
                    merged_list.append(item)
            else:
                i1 += 1
        else:
            merged_list.append(list2[i2])
            if i2 + 1 == len(list2):
                for item in list1[i1:]:
                    merged_list.append(item)
            else:
                i2 += 1
    return merged_list

                

    
    #  how_many_times = len(list1) + len(list2)
    #  index1 = 0
    #  index2 = 0
    #  index_list = range(0,how_many_times)
    #  for index in index_list:
    #      if list1[index1] > list2[index2]:
    #          merged_list.append(list2(index2))
    #          index2 += 1
    #      else:
    #          merged_list.append(list1[index1])
    #          index1 += 1
    #      if index1 == len(list1) or index2 == len(list2):
    #          if index1 == len(list1)
    #              #we have no more numbers to add to merged list from index 1 
    #              #add the remaining numbers from list2 to merged list
    #              while index2 < len(list2):
    #                  merged_list.append(list2[index2])
    #                  index1 += 1
    #                   return merged_list
    #              else:
    #                 #we have no more numbers to addd to merged list from index 2 
    #                 #add the remaning numbers from list2 to the merged list

    # # TODO: Implement this function
    # pass


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    # TODO: Implement this function
    pass

    word_lengths: list = []
    for words in words:
        word_lengths.append(len(words))
    return word_lengths



# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    pass
    #   def reverse_string(s: str) -> str:
    return s[:: -1]

# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    #step : create intersection list
    intersection_list: list = []
    #step 1 pick a list 
    #I am alwas picking list
    #step 2: iterate over the list
    for number in list1:
        #is number in list2
        if number in list2: 
            intersection_list.append(number)
    #the for loop is over now
    #is tere anything else we need to do?
    intersection_list = list(set(intersection_list))
    return intersection_list
    #step 3: fir each item, check if its in the other list
    #step 4: if it is add to the intersection list, oh wait , we need to
    #step 4.5: how do we remove duplicates
    # TODO: Implement this function

    pass


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
