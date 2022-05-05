l = [10, 20, 30, 40, 50]
l1 = [60, 70, 80, 90, 100]

for a, b in zip(l, l1):      # METHOD -> 1
    print(a, b)
print("")

t = len(l)                   # METHOD -> 2
for h in range(t):
    print(l[h], l1[h])
print("")

for c in range(5):         # METHOD -> 3
    print(l[c], l1[c])
print("")

p = []                       # TAKING INPUT FROM THE USER FOR THE LIST
n = eval(input("Enter the number of items:-"))
for u in range(n):
    num = eval(input("enter the values for the list:-"))
    p.append(num)
    print(p[u])
print("")
print("The list is as follows...")
print(p)

print("")

p = []                       # TAKING INPUT FROM THE USER FOR THE LIST WITH DEFINITE CONDITION
#n = eval(input("Enter the number of items:-"))
for u in range(7):
    num = eval(input("enter the values for the list:-"))
    p.append(num)
    print(p[u])
print("")
print("The list is as follows...")
print(p)