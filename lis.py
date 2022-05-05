l=[10,20,30,50,60]

# for a in range(l):
#     print(l[a])
for a in l:
    print(l)

print('='*50)

t=len(l)
for n in range(t):
    print(l[n])

# for a in l:
#     print(l[a])

print('='*50)
for a in l:
    print(a)

print('='*50)

# for reverse order of a list
for n in range(t-1,-1,-1):
    print(l[n])
print('='*50)

print(l[-1: :-1])

# p=[]
# for a in p:
#     eval(input("enter:".p[a]))
#     print(a)

print(max(l))
