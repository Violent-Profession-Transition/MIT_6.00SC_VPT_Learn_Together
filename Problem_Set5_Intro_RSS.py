"""
a program to monitor news feeds over the internet
1.the program will filter the news,
2.alert the user when it notices a news story
3.the news story should match the user's interests
for example: a user may be interested in a notification
whenever a story related to NBA is posted

the solutions for each problem should stay under 20 lines of code
"""

"""
RSS Overview:
many websites have contents that update on an unpredictable schedule
RSS can be used to keep track of this changing content.
streamlined and automated by connecting to website's RSS feed
RSS feed reader will periodically collect and draw your attention
to updated content
RSS stands for "Really Simple Syndication"
An RSS feed consists of periodically changing data stored in
an XML-format residing on a web-server
for this project, you do not need to what XML is or how to access XML files over the network

We will use a special Python module to deal with these low-level details
high-level details on the structure of the Google News RSS feed should be enough for our purposes
"""

"""
Part 1 Data Structure Design
RSS Feed structure Google News
http://news.google.com/?output=rss
Google News RSS feed is a list of items.
each entry has:
1. global unique id (guid)
2. title, subject, summary, link ...

The problem: because each RSS feed is structured a little bit differently
our goal in Part 1 is to unify and standardize the data structure

Goal:
an application that collects several RSS feeds from various sources
and act on all of them in the exact same way
we should be able to read all NYT,Google,blogs RSS feeds all in one place
"""

# Problem 1
# pretend someone has done the parsing of the RSS feeds
# store the variables about a news story in an object

class NewsStory(object):
    """an object that takes
    guid, title, subject, summary, link as args
    and store them"""
    def __init__(self, guid, title,
                subject, summary, link):
        """
        globally unique identifier (GUID) – a string that serves as a unique name for this entry
        title – a string
        subject – a string
        summary – a string
        link to more content – a string
        """
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        """getter for guid attribute"""
        return self.guid
    def get_title(self):
        """getter for title attribute"""
        return self.title
    def get_subject(self):
        """getter for subject attribute"""
        return self.subject
    def get_summary(self):
        """getter for summary attribute"""
        return self.summary
    def get_link(self):
        """getter for link attribute"""
        return self.link
