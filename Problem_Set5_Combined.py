#!/usr/bin/python2

# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

# my solutions
from Problem_Set5_Intro_RSS import NewsStory
from Problem_Set5_Triggers import *
from Problem_Set5_Filtering import filter_stories
from Problem_Set5_UserTrigger_Config import readTriggerConfig


#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

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

# TODO: WordTrigger

# TODO: TitleTrigger
# TODO: SubjectTrigger
# TODO: SummaryTrigger


# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
# TODO: AndTrigger
# TODO: OrTrigger


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

# def filter_stories(stories, triggerlist):
#     """
#     Takes in a list of NewsStory-s.
#     Returns only those stories for whom
#     a trigger in triggerlist fires.
#     """
#     # TODO: Problem 10
#     # This is a placeholder (we're just returning all the stories, with no filtering)
#     # Feel free to change this line!
#     return stories

#======================
# Part 4
# User-Specified Triggers
#======================

# def readTriggerConfig(filename):
#     """
#     Returns a list of trigger objects
#     that correspond to the rules set
#     in the file filename
#     """
#     # Here's some code that we give you
#     # to read in the file and eliminate
#     # blank lines and comments
#     triggerfile = open(filename, "r")
#     all = [ line.rstrip() for line in triggerfile.readlines() ]
#     lines = []
#     for line in all:
#         if len(line) == 0 or line[0] == '#':
#             continue
#         lines.append(line)

#     # TODO: Problem 11
#     # 'lines' has a list of lines you need to parse
#     # Build a set of triggers from it and
#     # return the appropriate ones

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Johor")
    t2 = SummaryTrigger("Singapore")
    t3 = PhraseTrigger("R&F")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    print("triggerlist is: ", triggerlist)

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    #print("=====reading from triggers.txt config file=====")
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    while True:
        print("Polling...")

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)

        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print("Sleeping...")
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()
