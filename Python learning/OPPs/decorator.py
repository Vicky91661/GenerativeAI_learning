# def deco(fun):
#     def inner_fun():
#         print("start of the function")
#         fun(* args)
#         print("end of the function")
#     return inner_fun

# @deco
# def test1(name):
#     print("name is "+name)
#     print(4+7)
# test1("vicky")


import time

def timer_test(fun):
    def timer_test_inner():
        start = time.time()
        fun()
        end = time.time()
        print("time tken to run this function is ",end- start)
    return timer_test_inner

@timer_test
def test2():
    print(45+78)
test2()


@timer_test
def forloop():
    for i in range(100000):
        pass
forloop()