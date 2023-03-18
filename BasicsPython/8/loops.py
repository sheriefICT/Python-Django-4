'''
x = 0
while x <= 10:
    print(x)
    x += 1
print("################################")
y = 0
while y <= 10 :print(y) ; y += 1
print("################################")

for i in range(1,6):
    for j in range(1,4):
        print(i,j)

print("################################")
for s in range(11):
    if s == 6:
        continue
    print(s)
print("################################")
for h in range(11):
    if h == 6:
        break
    print(h)
print("################################")
start = int(input(" Enter Start Number: "))
end = int(input(" Enter End Number: "))

print("number \t square")
print('----------------')
for e in range(start,end+1):
    print(e,'\t',e*e)

'''
print("################################")
'''
rows = int(input(" Enter Rows: "))
cols = int(input(" Enter Cols: "))

for f in range(rows):
    for g in range(cols):
        print('*', end='')
    print(' ')
    '''
print("################################")
'''
rows = int(input(" Enter Rows: "))
for o in range(1, rows+2):
    print('*'*o)
    '''
print("################################")
from_n = int(input(" Enter from_n : "))
to_n = int(input(" Enter to_n : "))

start = int(input(" Enter Start Number: "))
end = int(input(" Enter End Number: "))

for m in range(from_n,to_n+1):
    for d in range(start,end+1):
        print(f"{m} x {d} = {m*d}")
    print("__________________________")