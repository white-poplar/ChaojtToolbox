#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import Global

def center_window(w = 300, h = 200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


print('start')

root = tkinter.Tk(className='python gui')
root.title("超级淘工具箱%s by 黑莓糖一生推" % Global.VERSION)
# root.geometry("100x100")
center_window(500, 300)
root.resizable(width=False, height=False)

label = tkinter.Label(root)
label['text'] = '\(^o^)/'
label.pack()


# var = tkinter.StringVar()
# lb = tkinter.Listbox(root, height=5, selectmode=tkinter.BROWSE, listvariable = var)
# lb.bind('<ButtonRelease-1>')


# list_item = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
# for item in list_item:
#     lb.insert(tkinter.END,item)
# scrl = tkinter.Scrollbar(root)
# scrl.pack(side=tkinter.RIGHT,fill=tkinter.Y)
# lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
# lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
# scrl['command'] = lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview


text = tkinter.Text(root)
text.state="disabled"
text.insert('1.0',"text1\n")   # 插入
text.insert(tkinter.END,"text2\n") # END:这个Textbuffer的最后一个字符
text.insert(tkinter.END,"text3\n") 
text.insert(tkinter.END,"text3\n") 
text.insert(tkinter.END,"aa\n") 
text.insert(tkinter.END,"bb\n") 
text.insert(tkinter.END,"cc\n") 
text.insert(tkinter.END,"dd\n") 
text.insert(tkinter.END,"ee\n") 
text.insert(tkinter.END,"ff\n") 
text.see(tkinter.END)
text.focus_force()
# text.update()

# text.insert('1.0',"text3\n") 
#text.delete('1.0','2.0')   # 删除
# text.insert('1.0',"text3\n") 
text.pack(fill=tkinter.X)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

root.mainloop() # 进入消息循环

print('end')