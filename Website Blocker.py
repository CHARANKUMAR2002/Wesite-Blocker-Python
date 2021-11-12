from tkinter import *

win = Tk()
win.update()
win.geometry('468x135')
win.resizable(0,0)
win.config(bg='cyan')
win.title('Block A Website')
Label(win, text='Block A Website', font='arial 15 bold', bg='cyan').pack()
host_path = 'C:\Windows\System32\drivers\etc\hosts'
local_host = '127.0.0.1'
Label(win, text='Enter the Website :', font='arial 12', bg='cyan').place(x=5, y=60)
websites = Text(win, font='arial 10', height='2', width='40')
websites.place(x=160, y=55)


def block():
    website_list = websites.get(1.0, END)
    website = list(website_list.split(','))
    with open(host_path, 'r+') as host:
        file_content = host.read()
        for web in website:
            if web in file_content:
                Label(win, text='Blocked Already!', font='arial 10 bold', bg='cyan').place(x=260, y=100)
                win.update()
                pass
            else:
                host.write('\n'+local_host + " " + web)
                Label(win, text='Blocked', font='arial 10 bold', bg='cyan').place(x=260, y=100)
                win.update()


blocker = Button(win, text='Block', font='arial 12 bold', pady=1, command= block, width=6, bg='red', activebackground='purple')
blocker.place(x=160, y=100)
win.mainloop()

