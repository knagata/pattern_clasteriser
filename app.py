import Tkinter as tk
import tkFileDialog as tkfd
from Cluster import *
from compare import *

class app(tk.Frame):
    def __init__(self):
        self.clusters = []
        self.target_size = 4
        
        self.filename=""
        self.root = tk.Tk()
        self.root.title(u"pattern clusteriser")
        self.root.geometry("400x300")
        
        self.entr = tk.Entry(self.root)
        self.entr.config(width=400)
        self.entr.pack()
        self.text = tk.Text(self.root)
        #self.text.config(state='disabled')
        self.text.pack()
        
        tk.Frame.__init__(self, self.root)
        self.create_widgets()
        
        self.command = ""
        
    def create_widgets(self):
        #self.root.bind('<KeyPress>', self.onKeyPress)
        #self.root.bind('<BackSpace>', self.onBsPress)
        self.root.bind('<Return>', self.onReturnPress)
        
    def openfile(self):
        self.filename = tkfd.askopenfilename()
        file = open(self.filename, 'r')
        data = file.read().split("\n")
        for j,d in enumerate(data):
            strs = d.split(',')
            s = ""
            for i in range(1,len(strs)):
                s+=strs[i]
            self.clusters.append(Cluster(s,j))
        self.text.insert('1.0', " {0} genoms from the file\n".format(len(self.clusters)))
        
    def compute(self):
        for itr in range(len(self.clusters)-self.target_size):
            score = compare(self.clusters)
            self.clusters[score[0]].add(self.clusters.pop(score[1]))
            self.text.insert('1.0', " classified {0} time(s) now there are {1} clusters\n".format(itr+1,len(self.clusters)))
            self.root.update()
        self.text.insert('1.0', " classification finished\n")
        
    def export(self):
        self.text.insert('1.0', " preparing data...\n")
        result = ""
        for c in self.clusters:
            for g in c.genoms:
                result += str(g.id)+","
            result = result[0:len(result)-1]
            result += "\n"
        self.text.insert('1.0', " done preparation\n")
        filename = tkfd.asksaveasfilename(
        filetypes=[('CSV', '*.csv')],
        title='filename...')
        writer = open(filename+".csv", 'w')
        writer.write(result)
        writer.close()
        self.text.insert('1.0', " done saving\n")
        
    #def onKeyPress(self, event):
    #    self.command += event.char
        
    #def onBsPress(self, event):
    #    self.command = self.command[0:len(self.command)-1]

    def onReturnPress(self, event):
        #commands = self.command.split(" ")
        commands = self.entr.get().split(" ")
        self.entr.delete(0,'end')
        if commands[0] == "open":
            self.openfile()
        elif commands[0] == "calc":
            self.compute()
        elif commands[0] == "config":
            self.text.insert('1.0', " current parameters are\n  filename: {0}\n  target_size:{1}\n".format(self.filename, self.target_size))
        elif commands[0] == "set":
            if commands[1] == "target_size":
                self.target_size = int(commands[2])
        elif commands[0] == "save":
            self.export()
        elif commands[0] == "clear":
            self.clusters = []
        else:
            self.text.insert('1.0', " unavailable command <{0}>\n".format(commands[0]))
        self.command = ""
        
    def start(self):
        self.root.mainloop()

app().start()