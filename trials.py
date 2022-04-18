"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)

def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for item in nums:
        if item%2 == 0:
            even_nums.append(item)
    return even_nums


def get_odd_indices(items):
    # TODO: replace this line with your code
    odd_index = []
    for index in range(len(items)):
        if index % 2 != 0:
            odd_index.append(items[index])
    return odd_index

def print_as_numbered_list(items):
    # TODO: replace this line with your code
    i = 0
    for item in items:
        i += 1
        print(f'{i}. {item}')

def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    for number in range(start, stop):
        nums.append(number)
    return nums

def censor_vowels(word):
    # TODO: replace this line with your code
    chars = []
    vowels = ['a','e','i','o','u']
    for letter in word:
        if letter in vowels: 
            chars.append('*')
        else:
            chars.append(letter)
    chars = "".join(chars)
    return chars

def snake_to_camel(string):
    # TODO: replace this line with your code
    camelCase = []
    words = string.split('_')
    for word in words:
        camelCase.append(f'{word[0].upper()}{word[1::]}')
    return "".join(camelCase)


def longest_word_length(words):
    # TODO: replace this line with your code
    longest = len(words[0])

    for word in words:
        if (len(word) > longest):
            longest = len(word)
    return longest

def truncate(string):
    # TODO: replace this line with your code
    result = []
    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)
   
    return "".join(result)
    
def has_balanced_parens(string):
    pass # TODO: replace this line with your code
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        
    return parens==0

def compress(string):
    # TODO: replace this line with your code
    compressed = []
    curr_char = ''
    char_count = 0
    for char in string:
        if char not in curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        char_count += 1
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
    return ''.join(compressed)