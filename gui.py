import tkinter as tk
window = tk.Tk()
frm1 = tk.Frame(master = window)
frm2 = tk.Frame(master = window)
score = tk.Label(text="score\n0", master=frm1, fg="grey", bg="brown", width=10, height=4)

def setup(arr):
    window.title="game"
    frm1.pack()
    label = tk.Label(text="2048", master = frm1, foreground = "white", bg = "orange",width = 10, height = 4)
    label.pack(side=tk.LEFT, padx=5, pady=5)
    score.pack(side = tk.RIGHT)
    draw_grid(arr,0)

def draw_grid(arr,scr):
    frm2.pack()
    score.config(text="score\n%s" %scr)
    for i in range(4):
        frm2.columnconfigure(i, weight=1, minsize=60)
        frm2.rowconfigure(i, weight=1, minsize=50)
        for j in range(4):
            frame = tk.Frame(
                master=frm2,
                relief=tk.RAISED,
                borderwidth=20,
                bd=5
            )
            frame.grid(row=i, column=j)
            if arr[i][j]==0:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="burlywood2", bg="burlywood2")
            elif arr[i][j]==2:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray44", bg="ivory2")
            elif arr[i][j]==4:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray44", bg="bisque")
            elif arr[i][j]==8:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="tan2")
            elif arr[i][j]==16:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="chocolate2")
            elif arr[i][j] == 32:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="tomato2")
            elif arr[i][j] == 64:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="firebrick1")
            elif arr[i][j] == 128:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="yellow3")
            elif arr[i][j] == 256:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="gold2")
            elif arr[i][j] == 512:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="goldenrod2")
            elif arr[i][j] == 1024:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="DarkGoldenrod1")
            elif arr[i][j] == 2048:
                label = tk.Label(master=frame, text=arr[i][j], width=10, height=5, fg="gray90", bg="orange2")
            label.pack()

def refresh(arr,scr):
    frm2.pack_forget()
    draw_grid(arr,scr)
