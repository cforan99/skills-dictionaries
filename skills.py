# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    # Splits string into a list of words
    words = input_string.split()

    # Creates an empty dictionary
    word_counts = {}

    # Adds each word to the dictionary with an initial count of 1
    # If the word in already in the dictionary, it increments the count for each occurance of the word.

    for word in words:

        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    # Returns the entire dictionary of words and their counts, not just a list of the unique words
    return word_counts


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # Without dictionaries, more straightforward

    # common_items =[]

    # for i in range(len(list1)):
    #     item_in_list1 = list1[i]
    #     for item_in_list2 in list2:
    #         if item_in_list2 == item_in_list1:
    #             common_items.append(item_in_list2)
    #
    # return common_items

    ## With dictionaries, more complex

    # Cretes new empty dictionary to hold the common items
    common_items = {}

    # Loops through each item in list1
    for i in range(len(list1)):
        item_in_list1 = list1[i]

        # Then loops through each item in list2 to find a match
        # When found the item from list1 is added to the dictionary as a key
        # and the match from list2 is added to a list of values for that key.
        for item_in_list2 in list2:
            if item_in_list1 == item_in_list2:
                if common_items.get(item_in_list1, 0) == 0:
                    common_items[item_in_list1] = [item_in_list2]
                else: 
                    common_items[item_in_list1].append(item_in_list2)

    # Creates a list of the values, since this function needs to return a list of common items 
    lists = common_items.values()

    # Since the values are also lists, they need to be combined into one list rather than a list of lists.
    common_items_list = []
    for lst in lists:
        common_items_list += lst

    return common_items_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # # Without dictionaries, much more concise

    # # Converts lists to sets
    # set1 = set(list1)
    # set2 = set(list2)

    # # Finds the intersection of the two sets and stores it as a list of unique common items
    # unique_list = list(set1.intersection(set2))

    # return unique_list

    ## With dictionaries, much more complex
    # Similar to the find_common_items function

    unique_common_items = {}

    for i in range(len(list1)):
        item_in_list1 = list1[i]

        # Then loops through each item in list2 to find a match
        # When found the item from list1 is added to the dictionary as a key
        # and the match from list2 is added to a SET of values for that key.
        for item_in_list2 in list2:
            if item_in_list1 == item_in_list2:
                if unique_common_items.get(item_in_list1, 0) == 0:
                    unique_common_items[item_in_list1] = {item_in_list2}
                else: 
                    unique_common_items[item_in_list1].add(item_in_list2)
                    # Cannot append to set so the add method is used instead
                    # Sets will not repeat duplicate values

    # Creates a list of the values, since this function needs to return a list of common items 
    values = unique_common_items.values()

    # Since the values are sets, they need to be combined into one set rather than a list of sets.
    # Empty set is created and each value set is merged in using the union method.
    unique_common_items_set = set()
    for value in values:
        unique_common_items_set = unique_common_items_set.union(value)

    # Converts set to list since this function must return a list
    unique_common_items = list(unique_common_items_set)

    return unique_common_items


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    ## Without dictionaries: INCOMPLETE, DO NOT UNCOMMENT

    # pairs = []
    # for number in input_list:
    #     for i in range(len(input_list)):
    #         if number + input_list[i] == 0:
    #             sublist = [number, input_list[i]]
    #             if sublist not in pairs:
    #                 pairs.append(sublist)
    # return pairs

    ## With dictionaries

    zero_pairs = {}

    # Takes each negative number in the list and loops through the list to find its positive zero sum pair.
    # If found, that negative number is added to the dictionary as a key, and the positive pair is added as a value.
    # Since dictionaries can only have unique keys and one number can only have one zero pair, it is ok if keys and values get overwritten. 
    for i in range(len(input_list)):
        for number in input_list:
            if (number >= 0) and (number + input_list[i] == 0):
                zero_pairs[input_list[i]] = number

    # Creates a list of zero sum pairs from the keys and values in the dictionary.
    zero_pairs_list = []
    for pair in zero_pairs:
        zero_pairs_list.append([pair, zero_pairs[pair]])

    return zero_pairs_list




def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # Very much like count_unique function

    unique_words = {}

    # Adds each word to the dictionary with an initial count of 1 only one time.
    for word in words:

        if unique_words.get(word, 0) == 0:
            unique_words[word] = 1
        else:
            pass

    # Create a list of words that only occur once from the dictionary
    unique_words_list = unique_words.keys()

    return unique_words_list


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    encoded_phrase = ""

    for char in phrase:
        if char == "e":
            encoded_phrase += "p"
        elif char == "a":
            encoded_phrase += "d"
        elif char == "t":
            encoded_phrase += "o"
        elif char == "i":
            encoded_phrase += "u"
        else:
            encoded_phrase += char

    return encoded_phrase


# def sort_by_word_length(words):
#     """Given list of words, return list of ascending [(len, [words])].

#     Given a list of words, return a list of tuples, ordered by word-length.
#     Each tuple should have two items--the length of the words for that
#     word-length, and the list of words of that word length.

#     For example:

#         >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

#     """

#     return []


# def get_pirate_talk(phrase):
#     """Translate phrase to pirate talk.

#     Given a phrase, translate each word to the Pirate-speak equivalent.
#     Words that cannot be translated into Pirate-speak should pass through
#     unchanged. Return the resulting sentence.

#     Here's a table of English to Pirate translations:

#     English     Pirate
#     ----------  ----------------
#     sir         matey
#     hotel       fleabag inn
#     student     swabbie
#     boy         matey
#     madam       proud beauty
#     professor   foul blaggart
#     restaurant  galley
#     your        yer
#     excuse      arr
#     students    swabbies
#     are         be
#     lawyer      foul blaggart
#     the         th'
#     restroom    head
#     my          me
#     hello       avast
#     is          be
#     man         matey

#     For example:

#         >>> get_pirate_talk("my student is not a man")
#         'me swabbie be not a matey'

#     You should treat words with punctuation as if they were different
#     words:

#         >>> get_pirate_talk("my student is not a man!")
#         'me swabbie be not a man!'

#     """

#     return ""

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


# def adv_get_top_letter(input_string):
#     """Given an input string, return a list of letter(s) which appear(s) the most the input string.

#     If there is a tie, the order of the letters in the returned
#     list should be alphabetical.

#     For example:
#         >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
#         ['i', 'n']

#     If there is not a tie, simply return a list with one item.

#     For example:
#         >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
#         ['f']

#     Spaces do not count as letters.

#     """

#     return ''


# def adv_alpha_sort_by_word_length(words):
#     """Given a list of words, return a list of tuples, ordered by word-length.

#     Each tuple should have two items--a number that is a word-length,
#     and the list of words of that word length. In addition to ordering
#     the list by word length, order each sub-list of words alphabetically.
#     Now try doing it with only one call to .sort() or sorted(). What does the
#     optional "key" argument for .sort() and sorted() do?

#     For example:

#         >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

#     """

#     return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
