import shuntingre
import thompson

L = ["Geeks\n", "for\n", "Geeks\n"]

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

tests = [["(a.b|b*)", ["ab", "b", "bb", "a"]],
         ["a.(b.b)*.a", ["aa", "abba", "aba"]],
         ["1.(0.0)*.1", ["11", "100001", "11001"]]]

for test in tests:
    infix = test[0]
    print(f"infix:    {infix}")
    postfix = shuntingre.shunt(infix)
    print(f"postfix:  {postfix}")
    nfa = thompson.re_to_nfa(postfix)
    print(f"thompson:  {nfa}")
    for s in test[1]:
        match = nfa.match(s)
        print(f"Match: '{s}': {match}")
    print()
