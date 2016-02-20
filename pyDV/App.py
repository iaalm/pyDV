import tkinter as tk

class Application(tk.Frame):
    def __init__(self, run=None, lable_type=None, master=None):
        tk.Frame.__init__(self, master)
        self.run = run
        self.data = []
        if type(lable_type) == int:
            pass
        elif lable_type == Ellipsis:
            pass
        elif lable_type == None:
            self.lable = None
        else:
            return

        self.pack()

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="top")
        self.canvas.bind("<Button-1>", self.on_click)
        if run:
            self.RUN = tk.Button(self, text="RUN", fg="red",command=self.run_callback)
            self.RUN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",command=master.destroy)
        self.QUIT.pack(side="bottom")

    def on_click(self, event):
        #print("click", event.x, event.y)
        if self.lable:
            self.data.append((event.x, event.y, self.lable))
        else:
            self.data.append((event.x, event.y))

        self.canvas.create_oval(event.x, event.y,event.x, event.y)

    def run_callback(self):
        self.run(self.data, self.canvas)

def App(run = None):
    root = tk.Tk()
    app = Application(master=root,run=run)
    app.mainloop()
