class culc:
    def sum(self,x,y):
        #  هنا بنضيف سيلف كمتغير ثابت  في البرامتير للنداء
        #  علي اي متغير يتواصل مع الفنكشن وهذا يسي الانكبسوليشن
        return x+y

    def mul(self,x,y):
        return x*y

    def __init__(self,name):
        # __init__ هذا هوه الكونستركتور وهذا يتم تشغيلو
        # اوتوماتيك ويتم ارسال براميتر ايضا
        print(f"welcome {name}")


class Scalc(culc):

    def pow(self,x,y):
        return x**y


s = Scalc("Sherief Masood")
print(s.sum(10,20))
print(s.mul(10,20))
print(s.pow(2,3))








