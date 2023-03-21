"""
--------------------------------------------
Name: Het Bharatkumar Patel
SID: 1742431
CCID: hetbhara
AnonID: 1000348298
CMPUT 274, Fall 2022

Assessment: Weekly Exercise 04 - Text Preprocessor
--------------------------------------------

"""

import re
import sys
# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
    ]


def read_words():
    """ Makes a list of space seperated words enetered by user
    using input function

    Arguments:
        This function doesn't require any arguments

    Returns:
        This function returns a list of space separated strings
        from the text entered by user
    """
    text_list = list(map(str, input().split()))
    return(text_list)


def lower_case(words):
    """ Takes every string from the list which we got from the
    previous function and convert it to lower case string

    Arguments:
        words: list of strings from the previous function

    Returns:
        words: list of lower case strings
    """
    for i in range(len(words)):
        x = words[i].lower()
        words[i] = x
    return(words)


def symb_remove(out_1):
    """ Removes symbols, punctuations from the strings in the
    list we got from the previous function

    Arguments:
        out_1: list of lower case strings from the previous function

    Returns:
        out_1: list of strings from which every symbol and punctuations
        have been removed
    """
    for i in range(len(out_1)):
        x = re.sub(r'[\W_+]', '', out_1[i])
        out_1[i] = x
    return(out_1)


def num_remove(out_2):
    """ Removes digits from the string but doesn't remove the
    the string if it has only digits in it

    Arguments:
        out_2: list of strings

    Returns:
        out_2: list of words which has no digits attached with
        string but the strings which has only digits in it
    """
    for k in range(len(out_2)):
        if not out_2[k].isdigit():
            x = ''.join(i for i in out_2[k] if not i.isdigit())
            out_2[k] = x
    return(out_2)


def stopWords_remove(out_3):
    """ Removes all the Stop Words from the list given in the code

    Arguments:
        out_3: list of strings

    Returns:
        out_3: list of strings which has no stop words in it
    """
    del_words = []
    for word in out_3:
        if word in Stop_Words or word == '':
            del_words.append(word)
    for i in del_words:
        out_3.remove(i)
    return(out_3)


def processed_output(processed_words):
    """ joins the strings from the list and print a sentence

    Arguments:
        processed_words: list of words which are properly processed

    Returns:
        This function doesn't return anything but prints the sentence
        made from the list by joining the words from the argument list
    """
    processed_words = ' '.join(processed_words)
    print(processed_words)


def command_line():
    """ This function processes command line and acts accordingly
    It calls other fucntions from the code as necessary

    Arguments: This funciton has no arguments

    Returns: This funtion doesn't return anything but prints error
    message and proper usage if user enters wrong command line
    """
    if len(sys.argv) == 2:
        if sys.argv[1] == "keep-digits":
            out_1 = read_words()
            out_2 = lower_case(out_1)
            out_3 = symb_remove(out_2)
            out_4 = stopWords_remove(out_3)
            processed_output(out_4)
        elif sys.argv[1] == "keep-stops":
            out_1 = read_words()
            out_2 = lower_case(out_1)
            out_3 = symb_remove(out_2)
            out_4 = num_remove(out_3)
            processed_output(out_4)
        elif sys.argv[1] == "keep-symbols":
            out_1 = read_words()
            out_2 = lower_case(out_1)
            out_3 = num_remove(out_2)
            out_4 = stopWords_remove(out_3)
            processed_output(out_4)
        else:
            print("ERROR: Error in command line")
            print("PROPER USAGE: python3 preprocess.py <mode>")
            print("< mode > must be one of these: ")
            print("'keep-digits', 'keep-stops', 'keep-symbols'")
            exit(1)
    elif len(sys.argv) == 1:
        out_1 = read_words()
        out_2 = lower_case(out_1)
        out_3 = symb_remove(out_2)
        out_4 = num_remove(out_3)
        out_5 = stopWords_remove(out_4)
        processed_output(out_5)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    command_line()
    pass
