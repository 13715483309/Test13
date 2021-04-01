# 类属性和类方法可以由类对象或者实例对象访问，但是实例属性和实例方法只能有实例对象访问
class Dog():
    __tooth = 10

    @classmethod
    def oo(self):
        print('one')

obj = Dog()
print(obj._Dog__tooth)#命名重装，可以访问私用方法
obj.oo()
Dog.oo()
