# 本身是一个函数
# 视频位置：day5 homework
# 定义装饰器函数
def logger(func):
    def wrapper(*args,**kw):
        print("进入装饰器函数")

        func(*args,**kw)

        print("装饰器功能执行完毕")

    return wrapper

@logger
def add(x,y):
    print('进入被修饰的函数')
    print(f'{x}+{y}={x+y}')

add(1,2)

# 带参数装饰器
def say_hello(contry):
    def wapper(func):
        def swcond(*args,**kw):
            if contry == 'china':
                print('来之装饰器的我来之中国')

            elif contry == 'ameriacan':
                print('来之美国的hello')
            else:
                return
            func(*args,**kw)
        return wapper
def american():
    print('i an from ameraican')

def china():
    print('我来之中国')

