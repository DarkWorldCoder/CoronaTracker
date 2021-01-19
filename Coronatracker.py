import requests
from bs4 import BeautifulSoup
from tkinter import *
import random
tk = Tk()
tk.geometry("800x400")
tk.title("CoronaVirus Update")
op = "WORLD"
tk = Frame(tk)
tk.pack()
def refresh():
    global r
    r = requests.get("https://www.worldometers.info/coronavirus/").content
def show():
    global op


    try:
        op = m.get().upper()
        m.delete(0,"end")
        index = a.index(op)
        i = index
        run(i)

    except ValueError:
        m.insert(0,"COUNTRY NOT FOUND")


def run(o):
    draw(a, b, c, d, e, f, g, h, o)
def det(list):

    for i in range(0,7):
        list.pop(0)
        list.pop(-1)
    return list
    return f
def draw(a,b,c,d,e,f,g,h,i):
    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh



    aa.config(text=f"{a[i]}")
    bb.config(text=f"Total Case:{b[i]}")
    cc.config(text=f"New case:{c[i]}")
    dd.config(text=f"Total Death:{d[i]}")
    ee.config(text=f"New Death:{e[i]}")
    ff.config(text=f"New Recover:{f[i]}")
    gg.config(text=f"Total Recovered:{g[i]}")
    hh.config(text=f"Active Case:{h[i]}")








i = 0

r = requests.get("https://www.worldometers.info/coronavirus/").content

soup = BeautifulSoup(r,"html.parser")


table = soup.find("table")

dr = []
tot = []
newc = []
totd=[]
newd = []
totr=[]
newr=[]
actc=[]
for row in table.find_all("tr"):
    cells = row.find_all("td")

    if len(cells) == 19 :

        country = cells[1].find(text=True)

        total_case = cells[2].find(text=True)

        new_case = cells[3].find(text=True)
        total_death = cells[4].find(text=True)
        new_death = cells[5].find(text=True)
        total_rec = cells[6].find(text=True)
        new_rec = cells[7].find(text=True)
        active_case=cells[8].find(text=True)
        dr.append(country.upper())
        tot.append(total_case)
        newc.append(new_case)
        totd.append(total_death)
        totr.append(total_rec)
        newd.append(new_death)
        newr.append(new_rec)
        actc.append(active_case)



a = det(dr)
b=det(tot)
c=det(newc)
d=det(totd)
e=det(newd)
f=det(newr)
g=det(totr)
h=det(actc)

m = Entry(tk, width=50, text="Search")
m.grid(row=0, column=0)

but = Button(tk, text="Search", command=show).grid(row=0, column=1)

aa = Label(tk, text=f"{a[i]}", font=("Helvetica", 20))
bb= Label(tk, text=f"Total Case:{b[i]}", font=("Helvetica", 20))
cc = Label(tk, text=f"New case:{c[i]}",  font=("Helvetica", 20))
dd = Label(tk, text=f"Total Death:{d[i]}", font=("Helvetica", 20))
ee = Label(tk, text=f"New Death:{e[i]}", font=("Helvetica", 20))
ff = Label(tk, text=f"New Recover:{f[i]}", font=("Helvetica", 20))
gg = Label(tk, text=f"Total Recovered:{g[i]}", font=("Helvetica", 20))
hh= Label(tk, text=f"Active Case:{h[i]}",font=("Helvetica", 20))
aa.grid(row=1,column=0)
bb.grid(row=2,column=0)
cc.grid(row=3,column=0)
dd.grid(row=4,column=0)
ee.grid(row=5,column=0)
ff.grid(row=6,column=0)
gg.grid(row=7,column=0)
hh.grid(row=8,column=0)
lot = Button(tk, text="Quit", command=tk.quit,width=20).grid(row=9, column=0,sticky="w",padx=40,pady=40)
notm = Button(tk, text="Refresh", command=refresh,width=20).grid(row=9, column=1,sticky="e",padx=40,pady=40)
tk.mainloop()