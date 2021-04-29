# kekesuke-Graph-Theory-Project
G00375200

# Project description
This project is about a program  which is written in the Python 3. The program has the functionality to search in a text file using a regular expression. The program has few algorithms which are adapted from pseudo code based off wikipediea. The two of the algirthms used in this program are: 
-Shunting Yard Algorithm is used to converts an Infix Expression to a Postfix Expression using a stack that holds operators.
-Thompson's Construction is used to convert a Postfix Expression into a Non-deterministic Finite Automata. These NFAs can be used to match strings against Regular Expressions.

# How to Run and test the Project:

Requirements needed to run the project:
-Git
-Python 3

To clone the Repository:
Open a directory of your choice in Command-Line and enter:

$ git clone https://github.com/kekesuke/kekesuke-Graph-Theory-Project

Open the directory in the Command-Line and enter :
$ python3 RegEx.py

To test it using hard coded values:
 Press 2 in the console and hit enter.

To test it using your own file and manuel selected regex:
 1. Inert 1 into the console and press enter.
 2. Insert file directory link for e.g  'C:\Users\test1\repo\project\regexfile.txt' or regexfile.txt if the file is in the same folder as RegEx.py file.
 3. insert your regular expression for eg (a.b|b*).
 4. Check out the result.


# An explanation of the algorithm used for the program.
1. Ask user to insert value from 1 to 2. 1 For manual "1" or "2" for automatic test using hard coded values.
2. if 1 is selected the user will be promted to insert file directory.
3. If file is not found the program will end.
3. If file exists user will be asked to insert regular expression
4. File is opened and begins to loop through each line and each word in the line
5. Regular expression from the user and is converted from infix to postfix using [shunting yard algorithm](https://web.microsoftstream.com/video/9ddadf79-1e30-46d9-b1b5-63070e6d7a10)
6. Creating NFA from postfix regex using [tompson construction](https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32).
7. Checks if every character passes through the states of the NFA and prints it to the screen.
8. IF 2 is selected list is being created with infix expression and strings to be tested against each other.
9. The infix Regular expression from the list is converted from infix to postfix using [shunting yard algorithm](https://web.microsoftstream.com/video/9ddadf79-1e30-46d9-b1b5-63070e6d7a10)
10. Nfa are created from postfix regex using [tompson construction](https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32).
11. Check if every character passes [match](https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54) the states in the NFA and printing it to the screen.


1. What is a regular expression?
As described in [wiki](https://en.wikipedia.org/wiki/Regular_expression) A regular expression is a string which contain a sequence of characters, some of which may have a special meaning. A good examples are the three characters ., |, and * which have the special meanings concatenate using dot '.', OR using the double '||', and Kleene star using '*'. For example the regular expression for concatinating 0.1 means a 0 followed by a 1, the regular expression OR 0|1 means a 0 or a 1, and Kleene star which is * for example 1* means any number of 1’s.
When we want to perform string matching operations that are more complex than the operations, we must use regular expressions.

As described in [www3.ntu.edu.sg](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html#:~:text=Special%20Regex%20Characters%3A%20These%20characters,E.g.%2C%20%5C.https://en.wikipedia.org/wiki/Regular_expression) I found useful information about those Special Characters and their meaning.

Special Characters
., *, |, ?, +, (), $, ^

. concatenates two characters. So, a.b means an a followed by a b

'*' (Kleene Star) 
0* means a character appears 0 or more times

1* means a character appears 1 or more times

| means OR . So, a|b means an a or a b

? means a character appears 0 or 1 time

() are used to group characters

$ matches end of the input

^ matches the start of the input

2. How do regular expressions differ across implementations?
As the answer given in stackoverflow[Differences in RegEx syntax between Python and Java](https://stackoverflow.com/questions/10492180/differences-in-regex-syntax-between-python-and-java#:~:text=The%20obvious%20difference%20b%2Fw,escape%20a%20lot%20of%20characters.&text=String%20regex%2C%20input%3B%20%2F%2F%20initialized,compile(%20regex%20).) The diffrence between the implementation  between Java and Python for example is that in Java we need to escape a lot of characters.Java doesn't parse Regular Expressions in the same way as Python for a small set of cases. In this particular case the nested ['s is causing problems. In Python you don't need to escape any nested [ but you do need to do that in Java. The example in Python is "/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/([gim]+\b|\B)"
and "/(\\.|[^\[/\\\n]|\[(\\.|[^\]\\\n])*\])+/([gim]+\b|\B)" work for both Java and Python.

3. Can all formal languages be encoded as regular expressions?
As described in [Wiki](https://en.wikipedia.org/wiki/Regular_expression) A regular expression is a string which contain a sequence of characters, some of which may have a special meaning.
As desribed in [Wiki](https://en.wikipedia.org/wiki/Formal_language) formal languages In computer science are used among others as the basis for defining the grammar of programming languages and formalized versions of subsets of natural languages in which the words of the language represent concepts that are associated with particular meanings or semantics. As described in [Sciencedirect](https://www.sciencedirect.com/topics/computer-science/formal-language): In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet. A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language. A formal machine takes strings of symbols as input and outputs either “yes” or “no.” A machine is said to accept a language if it says “yes” to all and only those strings that are in the language. Alternatively, a language can be defined as the set of strings for which a particular machine says “yes.”.
As stated above I think that most of the formal languages can be encoded as regular expression using NFAS. 