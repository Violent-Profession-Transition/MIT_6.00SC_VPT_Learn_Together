"""
read your trigger configuration from a triggers.txt file, every time
your application starts, and use the triggers specified there.

Each line in the triggers.txt file:
1. Blank lines are ignored
2. comments #, also ignored
3. lines that DOES NOT start with ADD are named triggers
The first element in a trigger definition is the name of the trigger
The name can be any combination of letters without spaces, except for 'ADD'
The second element of a trigger definition is a keyword (e.g., TITLE, PHRASE, etc.)
that specifies the kind of trigger being defined
The remaining elements of the definition are the trigger arguments
# subject trigger named t1
t1 SUBJECT world
4. Trigger Addition
# the trigger set contains t1 and t4
ADD t1 t4
"""

from Problem_Set5_Triggers import *

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a list of triggers from it and
    # return the appropriate ones
    # t1 SUBJECT world
    # t2 TITLE Intel 
    # t4 AND t2 t3 
    # ADD t1 t4
    trigger_list = []
    # process the trigger_list and return trigger_set
    trigger_set = []
    for cmd in lines:
        cmd = cmd.split()
        # for trigger definitions
        if cmd[0] != "ADD":
            if cmd[1] == "SUBJECT":
                print("SUBJECT detected in trigger.txt")
                trigger = SubjectTrigger(cmd[2])
            elif cmd[1] == "TITLE":
                print("TITLE detected in trigger.txt")
                trigger = TitleTrigger(cmd[2])
            elif cmd[1] == "SUMMARY":
                print("SUMMARY detected in trigger.txt")
                trigger = SummaryTrigger(cmd[2])
            elif cmd[1] == "AND":
                print("AND detected in trigger.txt")
                trigger = AndTrigger(cmd[2], cmd[3])
            elif cmd[1] == "OR":
                print("OR detected in trigger.txt")
                trigger = OrTrigger(cmd[2], cmd[3])
            elif cmd[1] == "NOT":
                print("NOT detected in trigger.txt")
                trigger = NotTrigger(cmd[2])
            elif cmd[1] == "PHRASE":
                print("PHRASE detected in trigger.txt")
                # t3 PHRASE New York City
                trigger = PhraseTrigger(" ".join(cmd[2:]))
            trigger_list.append({cmd[0]:trigger})
            print(trigger_list)
        # for trigger addition
        else:
            print("trigger addition")
            # ADD t1 t4 
            for t in cmd[1:]:
                for trigger in trigger_list:
                    print("now trigger is: ", trigger)
                    print("trigger.keys()[0]",trigger.keys()[0])
                    if trigger.keys()[0] == t:
                        trigger_set.append(trigger.get(t))
            print(trigger_set)
    return trigger_set
