import tkinter as tk

class GeneralCanvasApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.data = []
        self.pack()

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="top")
        self.canvas.bind("<Button-1>", self.on_click)

        self.CLEAR = tk.Button(self, text="CLEAR", fg="red",command=self.clear)
        self.CLEAR.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",command=master.destroy)
        self.QUIT.pack(side="bottom")

    def on_click(self, event):
        #print("click", event.x, event.y)
        self.canvas.create_oval(event.x, event.y,event.x, event.y)
        self.append_data(event.x, event.y)

    def clear(self):
        self.canvas.delete("all")
        self.data = []

    def append_data(self, x, y):pass


class RunableApp(GeneralCanvasApp):
    def __init__(self, run, master=None, autorun=True):
        super(RunableApp,self).__init__(master=master)
        self.run = run
        self.RUN = tk.Button(self, text="RUN", fg="red",command=self.run_callback)
        self.RUN.pack(side="bottom")
        if autorun:
            self._autorun = tk.BooleanVar()
            self.AUTORUN = tk.Checkbutton(self, text='autorun',variable=self._autorun)
            self.AUTORUN.pack(side="bottom")

    def run_callback(self):
        self.run(self.data, self.canvas)

    def append_data(self, x, y):
        self.data.append((x,y))
        if self._autorun.get():
            self.run_callback()


def App(run = None, lable_type=None, autorun=True):    #Factory
    root = tk.Tk()
    if run == None:
        app = GeneralCanvasApp(master=root)
    elif lable_type == None:
        app = RunableApp(master=root, run=run, autorun=autorun)
    elif type(lable_type) == int and lable_type > 0:
        pass
    elif lable_type == Ellipsis:
        pass
    else:
        print('Wrong Type')
        return
    app.mainloop()
