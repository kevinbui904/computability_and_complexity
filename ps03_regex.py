# Written by Thien K. M. Bui <buik@carleton.edu>
# CS254, Spring 2023

import re
# We talked a bit about Python regular expressions in class and in the reading handout. In this problem, you’ll
# practice using these regular expressions to both find information in a string and change a string. All of your
# answers to this problem should go in a single file named ps03_regex.py.


# 1 and we’ll limit the local-part to be 54 characters or fewer. The domain can consist of upper or lower
# case letters, any digits, hyphens (-), and periods. Like the local-part, the domain cannot start with a period.
# Both the local-part and the domain must contain at least one character.
# 
# 2 Write a function get_all_emails
# that takes a single string parameter and returns a list where each item is an email address in the string.
# Here’s an example of me using mine:



 
def get_all_emails(s):
    """
    
    Parse a string and return a list where each item is an email address in the string.
    
    :param str s: string being parsed
    :return: list where each item is an email address in the string
    :rtype: [str]
    
    :raises TypeError: if s is not a string

    example usage
    >>> import ps03_regex
    >>> ps03_regex.get_all_emails('eris@sleepycat,eris@sleepycat,all.done+YAY@compl3t3 oh and lawn#
    mower@g.a.r.d.e.n')
    ['eris@sleepycat', 'eris@sleepycat', 'all.done+YAY@compl3t3', 'lawn#mower@g.a.r.d.e.n']
    >>> ps03_regex.get_all_emails('.turtles@SEA-Turtle')
    ['turtles@SEA-Turtle']
    >>> ps03_regex.get_all_emails('.turtles@.SEA-Turtle')
    """
    
    
    # (a) First, you’ll write a regular expression that can find email addresses in a string. Email addresses have a
    # local-part and a domain. The local-part and the domain are separated by an @ symbol. For instance, in my
    # email address, arafferty is the local part and carleton.edu is the domain. According to Wikipedia, the
    # local-part can consist of any upper or lowercase characters, any digits, and any of the following characters:
    # !#$%&'*+-/=?ˆ_`{}|∼;. It can also have one or more periods (.) in it as long as it doesn’t start with the
    # period,
    # regex = r’\d{1,2}\\\d{1,2}\\\d{2,4}’
    print("hello world")
    