"""
--------------------------------------------
Name: Het Bharatkumar Patel
SID: 1742431
CCID: hetbhara
AnonID: 1000348298
CMPUT 274, Fall 2022

Assessment: Weekly Exercise 03 - Word Frequency
--------------------------------------------
"""

import sys


def command_line():
    """
        Read input filename from passed command line,
        and return filename from the passed command line

        Arguments: There are no arguments to be passed to this function

        Returns:
            filename: A file name which is read from the command
            line argument passed, and this file will be
            used further in the code
    """

    filename = sys.argv[1]
    return(filename)


""" This if-else statements read the command line argument and
check number of arguments in the command line. If there are
more/less than 2 command line arguments, program will be exited,
else freq_count will be implemented """

if len(sys.argv) < 2:
    exit("Too few arguments. Usage: python3 freq.py <input_file_name>")
elif len(sys.argv) > 2:
    exit("Too many arguments. Usage: python3 freq.py <input_file_name>")
else:
    filename = command_line()


def freq_count(filename):

    """ This function will open the input file, count the number and
        frequency of all the words from that file, make an output file
        with table of word, number of time it occurs and frequency of
        all the words

        Arguments:
                  filename: The name of the file read from the command line
                  argument

        Return:
                This function doesn't return anything but makes a new output
                file with the table of words, count and frequency of the word
    """

    fin = open(filename, "r")           # file will be opened and saved as fin
    total_words = []

    """
    This for loop will strip and split the words from the input file
    """

    for line in fin:
        sep_words = line.strip().split()
        total_words.extend(sep_words)

    word_dict = {}

    """
    This for loop counts number of times each word occurs using the
    dictionary
    """
    for word in total_words:
        word_dict[word] = total_words.count(word)

    fout = open(filename+".out", "w")            # Opens the new output file

    """
    Thi for loop makes table in the new output file of word, no. of
    words and frequency at which it occurs
    """

    for keyWord, wordCount in sorted(word_dict.items()):
        frequency = str(round(wordCount/len(total_words), 3))
        fout.write(keyWord + " " + str(wordCount) + " " + frequency + "\n")

    fin.close()
    fout.close()


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    freq_count(filename)
    pass
