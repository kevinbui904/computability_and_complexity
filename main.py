import dfa
delta = {("q0", "0"):"q0", ("q0", "1"):"q1", ("q1", "0"):"q1", ("q1", "1"):"q0"}
m = (("q0", "q1"), ("0", "1"), delta, "q0", ("q1",))
result = dfa.dfa(m, "1101")
print(result) # prints True
result = dfa.dfa(m, "")
print(result) # prints False