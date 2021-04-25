# kekesuke-Graph-Theory-Project

# A description of your repository and its contents pitched at a knowledgeable outsider.
Project Statement

This project is about a program  which is written in the Python 3. The program  is with functionality to search in a text file using a regular expression. The program has few algorithms which are adapted from psudo code from wiki. The two of the algirthms used in this program are: 
-Shunting Yard Algorithm is used to converts an Infix Expression to a Postfix Expression using a stack that holds operators.
-Thompson's Construction is used to convert a Postfix Expression into a Non-deterministic Finite Automata. These NFAs can be used to match strings against Regular Expressions.

# Instructions stating how to run and test your program. How to Run the Project:

Requirements needed to run the project:
-Git
-Python 3

To clone the Repository:
Open a directory of your choice in Command-Line and enter:

$ git clone https://github.com/kekesuke/kekesuke-Graph-Theory-Project

Open the directory in the Command-Line and enter :
$ python3 RegEx.py


# An explanation of your algorithm.


1. What is a regular expression?
A regular expression is a string which contain a sequence of characters, some of which may have a special meaning. A good examples are the three characters ., |, and * which have the special meanings concatenate using dot '.', OR using the double '||', and Kleene star using '*'. For example the regular expression for concatinating 0.1 means a 0 followed by a 1, the regular expression OR 0|1 means a 0 or a 1, and Kleene star which is * for example 1* means any number of 1’s.
When we want to perform string matching operations that are more complex than the operations, we must use regular expressions.

https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html#:~:text=Special%20Regex%20Characters%3A%20These%20characters,E.g.%2C%20%5C.
https://en.wikipedia.org/wiki/Regular_expression
Special Characters
., *, |, ?, +, (), $, ^

. concatenates two characters. So, a.b means an a followed by a b

* (Kleene Star)  
0* means a character appears 0 or more times

1* means a character appears 1 or more times

| means OR . So, a|b means an a or a b

? means a character appears 0 or 1 time

() are used to group characters

$ matches end of the input

^ matches the start of the input

2. How do regular expressions differ across implementations?
3. Can all formal languages be encoded as regular expressions?