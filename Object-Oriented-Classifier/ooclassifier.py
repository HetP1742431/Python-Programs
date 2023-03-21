# Copyright 2020-2022 Paul Lu
# -------------------------------------------------------------
# Assignment 01 - OO Classifier
# -------------------------------------------------------------
import sys
import copy     # for deepcopy()
import re

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


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


def lower_case(words):
    """ Takes every string from the list and convert
    it to lower case string
    Arguments:
        words: list of strings
    Returns:
        words: list of lower case strings
    """
    for i in range(len(words)):
        x = words[i].lower()
        words[i] = x
    return(words)


def symb_remove(words):
    """ Removes symbols, punctuations from the strings in the
    list
    Arguments:
        words: list of lower case strings
    Returns:
        words: list of strings from which every symbol and punctuations
        have been removed
    """
    for i in range(len(words)):
        x = re.sub(r'[\W_+]', '', words[i])
        words[i] = x
    return(words)


def num_remove(words):
    """ Removes digits from the string but doesn't remove the
    the string if it has only digits in it
    Arguments:
        words: list of strings
    Returns:
        words: list of words which has no digits attached with
        string but the strings which has only digits in it
    """
    for k in range(len(words)):
        if not words[k].isdigit():
            x = ''.join(i for i in words[k] if not i.isdigit())
            words[k] = x
    return(words)


def stopWords_remove(words):
    """ Removes all the Stop Words from the list given
    in the code
    Arguments:
        words: list of strings
    Returns:
        words: list of strings which has no stop words in it
    """
    del_words = []
    for word in words:
        if word in Stop_Words or word == '':
            del_words.append(word)
    for i in del_words:
        words.remove(i)
    return(words)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        super().__init__()      # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self, printSorted=True):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self, printSorted=True):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class ClassifyByTopN(ClassifyByTarget):

    def __init__(self, lw=[]):
        """ This function invokes the __init__ method of it's
        parent function ClassifyByTarget
        """
        super().__init__()
        return

    def target_top_n(self, tset, num=5, label=''):
        """ Selects top words with highest frequency from all
        the words in training dataset
        Arguments:
            tset (Training set): contains training instances
            num (int): the number of most frequent words to be taken
            label (str): label of training instances to be processed
        Returns: None
        """
        word_dict = {}
        words_count = []

        # This for loop iterates over all training set
        for instance in tset.get_instances():
            if instance.get_label() == label:
                words_count += instance.get_words()

        # increase the value of word in dictionary, and if the
        # word is not available then add it to the dictionary
        for word in words_count:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        TopN = []
        # make a list of a word in a dictionary with both keys
        # and value as a list in it, this list is made up in
        # decending order of values of the words
        x = word_dict.items()
        word_list = sorted(x, key=lambda item: item[1], reverse=True)

        # selects top words with highest frequency, this for loop
        # selects words up to num (can be any integer)
        # Selects word more than num if it occurs same time
        # as the last word
        for i in range(len(word_list)):
            if i < num:
                TopN.append(word_list[i][0])
            elif i >= num:
                if word_list[i][1] == word_list[i-1][1]:
                    TopN.append(word_list[i][0])
                else:
                    break

        self.set_target_words(TopN)
        return


class TrainingInstance(C274):
    def __init__(self):
        super().__init__()              # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def preprocessed_output(self, mode=''):
        """ preprocess the words from training set as per the
        conditions
        Arguments:
            mode: Can be "keep-digits", "keep-symbols" or
                  "keep-stops"
                  keep-digits: doesn't remove digits from the words
                  keep-symbols: doesn't remove symbols from the words
                  keep-stops: doesn't remove stop-words from the list
        Returns:
            None
            Just change the words in training set according to the
            conditions
        """

        self.inst["words"] = lower_case(self.inst["words"])

        if (mode == ''):
            self.inst["words"] = symb_remove(self.inst["words"])
            self.inst["words"] = num_remove(self.inst["words"])
            self.inst["words"] = stopWords_remove(self.inst["words"])
        elif (mode == "keep-digits"):
            self.inst["words"] = symb_remove(self.inst["words"])
            self.inst["words"] = stopWords_remove(self.inst["words"])
        elif (mode == "keep-symbols"):
            self.inst["words"] = num_remove(self.inst["words"])
            self.inst["words"] = stopWords_remove(self.inst["words"])
        elif (mode == "keep-stops"):
            self.inst["words"] = symb_remove(self.inst["words"])
            self.inst["words"] = num_remove(self.inst["words"])
        else:
            print("ERROR: Error in command line")
            print("PROPER USAGE: python3 preprocess.py <mode>")
            print("< mode > must be one of these: ")
            print("'keep-digits', 'keep-stops', 'keep-symbols'")
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)


class TrainingSet(C274):
    def __init__(self):
        super().__init__()      # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=''):
        """ Invokes the method preprocessed_output to do
        preprocessing on the words in trainig set
        """

        training_instances = self.get_instances()
        for instance in training_instances:
            instance.preprocessed_output('')
        return

    def return_nfolds(self, num=3):
        """
        Returns "num" objects of class TrainingSet. Each of the objects
        returned contains a partition or fold of the original training dataset.
        Arguments:
            num: number of folds to make
        Returns:
            n_flop: "num" objects of class TrainingSet with partitions or
            folds of the original training dataset
        """
        instances = self.get_instances()
        lines = self.get_lines()
        n_flop = []

        number = len(instances)
        mod = number % num
        length = (number + (num - mod)//num)
        for i in range(num):
            tset = TrainingSet()
            for j in range(length):
                if (i + j*num) < number:
                    tset.inObjHash.append(copy.deepcopy(instances[i + j*num]))
                    tset.inObjList.append(copy.deepcopy(lines[i + j*num]))
                else:
                    break
            n_flop.append(copy.deepcopy(tset))
        return n_flop

    def copy(self):
        """ Creates a deepcopy of this training set.
        """
        return(copy.deepcopy(self))

    def add_training_set(self, tset):
        """ Adds all training instances of tset to this training set.
        Arguments:
            tset: training set
        Returns: None
        """
        for instance in tset.get_instances():
            self.inObjHash.append(copy.deepcopy(instance))
        self.inObjList += tset.get_lines()
        return


# Very basic test of functionality
def basemain():
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()
