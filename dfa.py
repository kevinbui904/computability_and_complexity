# Written by Thien K. M. Bui
# Apr 6th, 2023
# CS254 PSET_1, problem 6

def dfa(m, s):
    """
    Implementation of a DFA that reads string s
    :param m: DFA tuple that we will parse string s through
    :type m: (Q, Σ, δ, q0, F) 
        • Q: A tuple of arbitrary Python objects. These objects must be hashable (note: Strings and tuples are both
            hashable; lists are not).
        • Σ: A tuple of characters.
        • δ: A dictionary in Python. Each key is a 2-tuple of the form (q, a) where q ∈ Q and a ∈ Σ. Each value is an
            element of Q. If any tuple (q, a) ∈ Q × Σ is not a key in the dictionary, then it is understood that the DFA
            does not accept if it must transition out of state q via symbol a.
        • q0: A Python object, which must be an element in Q.
        • F: A tuple of Python objects, which must be a subset of Q.
    :return: true if s[-1] is in F, false otherwise
    :rtype: boolean
    
    :raises TypeError: if m is not of the correct form listed
    :raises TypeError: if s is not a string

    Example usage:
    import dfa
    delta = {("q0", "0"):"q0", ("q0", "1"):"q1",
    ("q1", "0"):"q1", ("q1", "1"):"q0"}
    m = (("q0", "q1"), ("0", "1"), delta, "q0", ("q1",))
    result = dfa.dfa(m, "1101")
    print(result) # prints True
    result = dfa.dfa(m, "")
    print(result) # prints False

    """