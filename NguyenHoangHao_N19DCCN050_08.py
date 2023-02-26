import copy
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

#thuat toan
def lru(capacity, s, check):
    f,st = [],[]
    count = 0
    rows, cols = (capacity, len(s))
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in s:
        if i not in f:
            if len(f)<capacity:
                f.append(i)
                st.append(len(f)-1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            check.append(True)
        else:
            st.append(st.pop(st.index(f.index(i))))
            check.append(False)
        for j in range(0,len(f)):
            arr[j][count] = copy.copy(f[j])

        count += 1

    for i in range(0,rows):
        for j in range(0,cols):
            print(arr[i][j], end=' ')
        print("")
    return arr


def handing(capacity, s, frame):
    class Table:

        def __init__(self, frame):
            for j in range(total_columns):
                self.e = tk.Label(frame, text=s[j], font=('Arial', 10, 'bold'), fg='blue')
                self.e.grid(row=0, column=j)
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(frame, width=7,
                                   font=('Arial', 10, 'bold'), justify='center')
                    self.e.grid(row=i+1, column=j)
                    if arr[i][j] != 0:
                        self.e.insert(tk.END, arr[i][j])
                    else:
                        self.e.insert(tk.END, '')

            for i in range(total_columns):
                if check[i]:
                    self.e = tk.Label(frame, text='*', font=('Arial', 15, 'bold'), fg='red')
                    self.e.grid(row=total_rows+2, column=i)
                else:
                    self.e = tk.Label(frame, text='', font=('Arial', 10, 'bold'), fg='red')
                    self.e.grid(row=total_rows + 2, column=i)

    check = []
    arr = lru(capacity, s, check)
    total_rows = capacity
    total_columns = len(s)
    t = Table(frame)
    for t in check:
        print(t)



#graphics
window = tk.Tk()
window.title("LRU")
window.geometry('1050x450')
frame1 = Frame(window, width=1050, heigh=150)
frame1.pack()
frame2 = Frame(window, width=1050, heigh=300)
frame2.pack()

txt_1 = Entry(frame1, width=10)
txt_1.place(x=140, y=20)

txt_2 = Entry(frame1, width=40)
txt_2.place(x=140, y=80)

txt1 = Label(frame1, text='Number of frames:', font=('Arial', 10, 'bold')).place(x=10, y=20)
txt2 = Label(frame1, text='Reference string:', font=('Arial', 10, 'bold')).place(x=10, y=80)

txt3 = tk.Label(frame1, text='Giải thuật thay thế trang theo thuật toán LRU', font=('Arial', 15, 'bold'), fg='blue').place(x=450, y=20)
txt4 = tk.Label(frame1, text='Nguyễn Hoàng Hảo - N19DCCN050', font=('Arial', 15, 'bold'), fg='blue').place(x=450, y=60)

def clicked():
    text1 = txt_1.get()
    text2 = txt_2.get()
    if text1=='' or text2=='':
        return messagebox.showinfo('Lỗi!', 'Bạn chưa nhập')
    capacity = int(text1)
    s = list(map(int, text2.strip().split()))

    for widgets in frame2.winfo_children():
        widgets.destroy()
    return handing(capacity, s, frame2)

btn = Button(frame1, text="Run!", command=clicked)
btn.place(x=130, y=110)

window.mainloop()