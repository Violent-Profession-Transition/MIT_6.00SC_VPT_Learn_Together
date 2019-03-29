"""
Parsing and Triggers
parsing is the process of turning a data stream into a structured
format that is more convenient to work with

Trigger will be used to generate alerts
trigger = alerting rules
"""

"""
Trigger interface will contain "evaluate" method
any subclass that inherits from Trigger will have an evaluate method
by default, they will use the evaluate method in Trigger
"""

"""
string.punctuation
Out[3]: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
"""
import string

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# WordTrigger
class WordTrigger(Trigger):
    """trigger about specific word"""
    def __init__(self, word):
        """takes in word for constructor
        not case sensitive"""
        # convert word to lower case
        word = word.lower()
        self.word = word
    def is_word_in(self, text):
        """takes in text argument
        returns True if whole word is present in text"""
        # should not be case-sensitive
        text = text.lower()
        # sanitize the punctuations with space
        for punc in string.punctuation:
            text = text.replace(punc, " ")
        # split by white space
        text_list = text.split()
        for w in text_list:
            if self.word == w:
                return True
        return False

t1 = WordTrigger('soft')
assert(t1.is_word_in("Soft drinks are great.") == True)
assert(t1.is_word_in("Soft's the new pink!") == True)
assert(t1.is_word_in("Microsoft announced today") == False)

# TitleTrigger
class TitleTrigger(WordTrigger):
    """fires when a news item's TITLE contains a given word"""
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        fire alert when text contains given word"""
        return self.is_word_in(story.get_title())

# SubjectTrigger
class SubjectTrigger(WordTrigger):
    """fires when a news subject contains a given word"""
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        fire alert when text contains given word"""
        return self.is_word_in(story.get_subject())


# SummaryTrigger
class SummaryTrigger(WordTrigger):
    """fires when a news subject contains a given word"""
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        fire alert when text contains given word"""
        return self.is_word_in(story.get_summary())

# Composite Triggers
# Problems 6-8

# NotTrigger
class NotTrigger(Trigger):
    """NOTtrigger produce its output by inverting the output of another trigger"""
    def __init__(self, trigger):
        """take other trigger as argument"""
        self.trigger = trigger
    def evaluate(self, story):
        """ invert the other trigger's evaluate()"""
        return not self.trigger.evaluate(story)

# AndTrigger
class AndTrigger(Trigger):
    """take two triggers as arguments to its constructor,
    and should fire on a news story only if
    both of the inputted triggers would fire on that item"""
    def __init__(self, trigger_1, trigger_2):
        """takes two triggers as arguments"""
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    def evaluate(self, story):
        """only evaluates to be true
        if both trigger_1 and trigger_2 returns T
        to that story"""
        return self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story)


# OrTrigger
class OrTrigger(Trigger):
    """take two triggers as arguments to its constructor,
    and should fire on a news story if
    either one or both of the inputted triggers would fire on that item"""
    def __init__(self, trigger_1, trigger_2):
        """takes two triggers as arguments"""
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    def evaluate(self, story):
        """only evaluates to be true
        if either/both trigger_1 and trigger_2 returns T
        to that story"""
        return self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story)


# Phrase Trigger
# Question 9

# PhraseTrigger
class PhraseTrigger(Trigger):
    """
     fires when a given phrase is in any of the
    subject, title, or summary,
    case MUST match
     “New York City” will match:
     In the heart of New York City’s famous cafe
     New York Cityrandomtexttoproveapointhere 
    but not:
    I love new york city
    HINT: use in
    """
    def __init__(self, phrase):
        """takes in the phrase as argument"""
        self.phrase = phrase
    def evaluate(self, story):
        if self.phrase in story.get_subject():
            return True
        elif self.phrase in story.get_title():
            return True
        elif self.phrase in story.get_summary():
            return True
        else:
            return False


