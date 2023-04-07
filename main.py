import dfa
# delta = {("q0", "0"):"q0", ("q0", "1"):"q1", ("q1", "0"):"q1", ("q1", "1"):"q0"}
# m = (("q0", "q1"), ("0", "1"), delta, "q0", ("q1",))
# result = dfa.dfa(m, "1101")
# print(result) # prints True
# result = dfa.dfa(m, "")
# print(result) # prints False

import ps03_regex

print(ps03_regex.get_all_emails("eris@sleepycat,eris@sleepycat,all.done+YAY@compl3t3 oh and lawn#mower@g.a.r.d.e.n,"))

print(ps03_regex.get_all_emails('.turtles@SEA-Turtle'))

print(ps03_regex.get_all_emails('.turtles@.SEA-Turtle'))



print(ps03_regex.obfuscate('Here is my email: turtles@SEA-Turtle'))
    # 'Here is my email: SEA-Turtle preceded by @ and then preceded by turtles'
print(ps03_regex.obfuscate('eris email is eris@sleepycat, and YAY has email too: all.done+YAY@compl3t3'))
    # 'eris email is sleepycat preceded by @ and then preceded by eris, and YAY has email too: compl3t3
    # preceded by @ and then preceded by all.done+YAY'
