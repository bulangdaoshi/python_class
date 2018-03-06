#线程事件

import threading

def do(event):
    print('start')
    # wait（）有一个可选参数 timeout过时时间
    event.wait()#线程堵塞，知道event对象内置标识符被设置为True或超时，就会向下执行

    print('end')

event_obj = threading.Event()#实例化线程事件创建标识符

for i in range(10):
    t = threading.Thread(target=do,args=(event_obj,))#将线程事件实例穿进去必须以元祖的形式或时列表
    t.start()

event_obj.clear()#将事件标识符设置为false遇到wait函数等待不能向下执行

inp = input('input:')

if inp == "true":
    event_obj.set()#解锁标识符设置为TRue向下执行操作

