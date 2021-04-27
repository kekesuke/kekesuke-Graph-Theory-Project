L = ["Test1\n", "for\n", "Test2\n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

# Shunting yard algorithm for regular expressions


def shunt(infix):
    """Convert infix expressions to postfix  """
    # The eventual output
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # operator precedence
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input a character at a time
    for c in infix:
        # c is an operator
        if c in {'*', '.', '|'}:
            # check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # append operator at top  of stack  to output.
                postfix = postfix + stack[-1]
                # remove operator from stack
                stack = stack[:-1]
            # push c to stack
            stack = stack + c
        elif c == '(':
            # push c to stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                # append operator at top of stack to output
                postfix = postfix + stack[-1]
                # remove operator from stack
                stack = stack[:-1]
            # remove open bracket from stack
            stack = stack[:-1]
            # else its a non special character
        else:
            # push it to the output
            postfix = postfix + c
        # empty the operator stack
    while len(stack) != 0:
        # append operator at top of stack to output
        postfix = postfix + stack[-1]
        # remove operator from stack
        stack = stack[:-1]
    return postfix


# if __name__ == "__main___":
#     print("test")
#     for infix in ["3+4*(2-1)", "1+2+3+4+5*6", "(1+2)*(4*(6-7))"]:
#         print(f"infix:    {infix}")
#         print(f"postfix:  {shunt(infix)}")
#         print()

# for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:
#     print(f"infix:    {infix}")
#     print(f"postfix:  {shunt(infix)}")
#     print()
# Thompson's contruction

class State:
    """A state and its arrows in Thompson construction"""
    # A label is arrow labels. None if e.
    # next states after e.
    # Is it an acepting state?
    # constructor.

    def __init__(self, label, arrows, accept):
        self.label = label
        self.arrows = arrows
        self.accept = accept

    # a set of states that are gotten from following this state and all of its E arrows
    def followes(self):
        # include this state in the return set.
        states = {self}
        # if this state has E arrows, i.e label is None
        if self.label is None:
            # loop through this states arrows
            for state in self.arrows:
                # incorporate that state's e arrow state in states
                states = (states | state.followes())
        # return the set of states
        return states


class NFA():
    """None determenistic finite automaton."""
    # start state
    # end state

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """return true if s is accepted by this instance of NFA"""
        # a list if previous state
        previous = self.start.followes()
        # loop through each character in the string,
        for c in s:
            # start with empty set of current state
            current = set()
            # loop through the previous state
            for state in previous:
                # check if there is a c arrow from state
                if state.label == c:
                    # add followes for next state
                    current = (current | state.arrows[0].followes())
            # replace previous with current
            previous = current
        # if final states is in previous return true, False otherwise.

        return (self.end in previous)


def re_to_nfa(postfix):
    # A stack for NFA's
    stack = []
    # Loop Through postfix regular expressions left to right
    for c in postfix:
        # concatination
        if c == '.':
            # pop top NFA of the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop next NFA of stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept
            nfa1.end.accept = False
            # Make it point at start state of nfa2
            nfa1.end.arrows.append(nfa2.start)
            # make a new NFA with nfa1 start state and nfa2 end state
            nfa = NFA(nfa1.start, nfa2.end)
            # push to the stack
            stack.append(nfa)

        elif c == '|':
            # pop top NFA of the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop next NFA of stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # create new start and end state
            start = State(None, [], False)
            end = State(None, [], True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make the old accept state non-accept
            nfa1.end.accept = False
            nfa2.end.accept = False
            # point old end states to the new one
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # make a new NFA
            nfa = NFA(start, end)
            # push to the stack
            stack.append(nfa)
        elif c == '*':
            # pop one NFA of the stack from the top
            nfa1 = stack[-1]
            stack = stack[:-1]
            # create new start and end state
            start = State(None, [], False)
            end = State(None, [], True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            # and at the new end state
            start.arrows.append(end)
            # Make old end state non-accept
            nfa1.end.accept = False
            # make old end state point to new end state
            nfa1.end.arrows.append(end)
            # make old end state point to old start state
            nfa1.end.arrows.append(nfa1.start)
            # make a new NFA
            nfa = NFA(start, end)
            # push to the stack
            stack.append(nfa)
        else:
            # create nfa for non-special character c
            # create end state
            end = State(None, [], True)
            # create start state
            start = State(c, [], False)
            # pont new start state at new end state
            start.arrows.append(end)
            # create NFA with start and end state
            nfa = NFA(start, end)
            # Append the NFA to NFA stack
            stack.append(nfa)
    # there should be only one NFA on the stack in the end
    if len(stack) != 1:
        return None
    else:
        return stack[0]


# for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
#     print(f"postfix:    {postfix}")
#     print(f"NFA:  {re_to_nfa(postfix)}")
#     print()


tests = [["(a.b|b*)", ["ab", "b", "bb", "a"]],
         ["a.(b.b)*.a", ["aa", "abba", "aba"]],
         ["1.(0.0)*.1", ["11", "100001", "11001"]]]

for test in tests:
    infix = test[0]
    print(f"infix:    {infix}")
    postfix = shunt(infix)
    print(f"postfix:  {postfix}")
    nfa = re_to_nfa(postfix)
    print(f"thompson:  {nfa}")
    for s in test[1]:
        match = nfa.match(s)
        print(f"Match: '{s}': {match}")
    print()
