from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD, Font, ITALIC
import time
import subprocess
from threading import Thread
import os
import argparse

def dir_path(path):
    if os.path.isdir(path):
        if path == ".":
            return os.getcwd()
        return path
    else:
        raise argparse.ArgumentTypeError("readable_dir: "+path+" is not a valid path")

def update():
    logbox.delete(1.0,END)
    
    saveinformations()
    try:
        upd_worker = Thread(target=update_worker,args=[username.get(),password.get(),PATH.get()])
        upd_worker.start()
    except:
         messagebox.showerror(title="Error",
                              message="Restart Repman Updator")

def saveinformations(): 
    if(not(save.get())):
        return 0
    data = username.get()+ "\r" +password.get()+ "\r" +PATH.get()
    f = open(os.path.expanduser('~')+"/.rep-updator/.datarp", "w")
    f.write(data)
    f.close()
    logbox.insert(END, "Informations saved\n")


def getinformations():
    try:
        f = open(os.path.expanduser('~')+"/.rep-updator/.datarp", "r")
        u = f.readline()
        if (len(u)<2):
            messagebox.showerror(title="Empty",
                                message="Refill your informations")
            return 0

        p = f.readline()
        usr.set(u[0:len(u)-1])
        psw.set(p[0:len(p)-1])
        if (args.path == None):
            pth.set(f.readline())
        f.close()
        logbox.insert(END, "Informations filled\n")
    except:
        messagebox.showerror(title="No Data",
                                message="Refill your informations")
        return 0

def update_worker(us,ps,pt):
    with subprocess.Popen("./ans.sh "+us+" "+ps+" "+pt, shell=True, stdout=subprocess.PIPE,cwd = os.path.expanduser('~')+"/.rep-updator/", bufsize=1, universal_newlines=True) as p:
                for line in p.stdout:
                    logbox.insert(END, line)
                    logbox.see(END)

                    

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", type=dir_path, help="path of trunk directory")
args = parser.parse_args()

frame = Tk()
frame.title('Repman Updator')

icon = PhotoImage(file=os.path.expanduser('~')+"/.rep-updator/rep-logo.png")
frame.iconphoto(False,icon)

usr = StringVar()
psw = StringVar()
pth = StringVar()
if(args.path != None):
    pth.set(args.path)

Label(text = 'username').pack()
username = Entry(width=20,textvariable=usr)
username.pack()

Label(text = 'password').pack()
password = Entry(frame, show="*", width=20,textvariable=psw)
password.pack()

Label(text = 'PATH of trunk directory').pack()
PATH = Entry(width=40,textvariable=pth)
PATH.pack()

cpright = Label(frame, text="adinar production for ST",font=Font(size=10, weight=BOLD,slant=ITALIC))
cpright.pack(side=BOTTOM)

Button(text='Update',command=update).pack()
Button(text='Fill with saved informations',command=getinformations).pack(side = BOTTOM)

save = IntVar()
save.set(1)
Checkbutton(frame, text="Save informations", variable=save).pack(side=BOTTOM)

logbox = Text(frame, borderwidth=3, relief="sunken",background="black",foreground="white")
logbox.pack()

frame.mainloop()