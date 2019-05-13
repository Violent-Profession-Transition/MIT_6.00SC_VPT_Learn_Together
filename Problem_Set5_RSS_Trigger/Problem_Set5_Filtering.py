#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    triggered_stories = []
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                triggered_stories.append(story)
    return triggered_stories