

def mysum(x, y):
    return x + y


total = mysum(500,50)
print(total)




print("______________________________________________")
f = 0
print(f)


def do():
    global f
    f = 5
    print(f)


do()
print(f)




print("###################################################")
print("_____________انميوس فنكشن start___________________")


def mysum(x, y):
    return x+y


mysum2 = lambda x,y : x+y

print(mysum(5,50))
print(mysum2(50, 60))


x = (lambda x,y : x+y)(55,66)
print(x)

print("_____________انميوس فنكشن End___________________")
print("###################################################")
print("_____ابحث عن python string functions in w3school____")
print("_____ابحث عن python List functions in w3school____")
print("_____ابحث عن python Tuples functions in w3school____")

d = {"ahmed" : 999,"mahmuod" : 555 }
for k,v in d.items():
    print(f"{k}---------{v}")