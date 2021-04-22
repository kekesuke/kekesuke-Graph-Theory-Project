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

for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:
    print(f"infix:    {infix}")
    print(f"postfix:  {shunt(infix)}")
    print()
