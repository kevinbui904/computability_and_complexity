# Written by Thien K. M. Bui <buik@carleton.edu>
# CS254, Spring 2023

import re

 
def get_all_emails(s):
    """
    Parse a string and return a list where each item is an email address in the string.
    
    :param str s: string being parsed
    :return: list where each item is an email address in the string
    :rtype: [str]

    example usage
    >>> import ps03_regex
    >>> ps03_regex.get_all_emails('eris@sleepycat,eris@sleepycat,all.done+YAY@compl3t3 oh and lawn#
    mower@g.a.r.d.e.n')
    ['eris@sleepycat', 'eris@sleepycat', 'all.done+YAY@compl3t3', 'lawn#mower@g.a.r.d.e.n']
    >>> ps03_regex.get_all_emails('.turtles@SEA-Turtle')
    ['turtles@SEA-Turtle']
    >>> ps03_regex.get_all_emails('.turtles@.SEA-Turtle')
    """


    #the local-part (before @) can consist of any upper or lowercase characters, any digits, and any of the following characters: !#$%&'*+-/=?ˆ_`{}|∼;. It can also have one or more periods (.) in it as long as it doesn’t start with the period

    #The domain can consist of upper or lower case letters, any digits, hyphens (-), and periods. Like the local-part, the domain cannot start with a period.
    return re.findall(r'(?!\.)[0-9a-zA-Z\!\#\$\%\'\*\+\-\/\=\?\^\_\`\{\}\|\~\;\.]{1,54}\@(?!\.)[0-9a-zA-Z\-\.]*',s)
    

def obfuscate(s):
    """
    Rewrites the email into the domain name, followed by the words “preceded by @ and then preceded by ”, and then followed by the local-part.

    :param str s: string being parsed
    :return: the string with any emails which has been modified
    :rtype: str

    EXAMPLE usage:
    >>> ps03_regex.obfuscate('Here is my email: turtles@SEA-Turtle')
    'Here is my email: SEA-Turtle preceded by @ and then preceded by turtles'
    >>> ps03_regex.obfuscate('eris email is eris@sleepycat, and YAY has email too: all.done+YAY@compl3t3')
    'eris email is sleepycat preceded by @ and then preceded by eris, and YAY has email too: compl3t3 preceded by @ and then preceded by all.done+YAY'

    """

    emails = get_all_emails(s)#reuse get_all_email to get the list of emails
    obfuscated = s
    for email in emails:
        addr_parts = email.split("@")
        repl = addr_parts[1] + " preceded by @ and ten preceded by " + addr_parts[0] 
        obfuscated = re.sub(re.escape(email), repl, obfuscated)
    
    return obfuscated