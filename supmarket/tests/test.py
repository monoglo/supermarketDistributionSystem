from tkinter import *
'''
为Listbox添加滚动条。
滚动条是独立的组件。
为了在某个足尖上安装垂直滚动条，你需要做两件事：
1、设置该组件的yscrollbarcommand选项为Scrollbar组件的set()方法
2、设置Scrollbar组件的command选项为该组件的yview()方法
'''
root = Tk()
sb = Scrollbar(root)  #垂直滚动条组件
sb.pack(side=RIGHT, fill=Y)  #设置垂直滚动条显示的位置
lb = Listbox(root, yscrollcommand=sb.set)  #Listbox组件添加Scrollbar组件的set()方法
for i in range(1000):
    lb.insert(END, i)
lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)  #设置Scrollbar组件的command选项为该组件的yview()方法

mainloop()
