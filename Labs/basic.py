# Python basic 16/02/2021

#print("Hello  world")

a = 1
b = 1.0
s = "Hello using String"
t = 'Hello different  String'

#print(a, b, s, t)
# print(s[3:10:2])

x = [1, 2, 3, "Hello", 4, 5, 6]
# print(x)
# print(x[0])
# print(x[2])
# print(x[-1])

for i in x[::2]:
    print(i)
    #print(i + i)


for i in range(10):
    print(i)

d = {"no_wheels": 4, "make": "Skoda"}

print(d["no_wheels"])

d["model"] = "Superb"

print(d["model"])

r = [1, 2, 3, 4]

print(r)

s = [i*i for i in r]

print(s)
