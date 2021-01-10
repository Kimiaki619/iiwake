import tkinter
import random

def click_btn():
    label["text"] = random.choice(["弟が","父が","母が","朝起きたら","妹が","兄が","姉が"])
    label.update()
    kimi["text"] = random.choice(["毒虫になっていたので","誤認逮捕されたので",
    "金縛りにかかったので","パンダのケンカに巻き込まれたので"])
    kimi.update()

root = tkinter.Tk()
root.title("仕事休み言い訳ソフト")
root.resizable(False,False)

canvas = tkinter.Canvas(root,width=757, height=666)
canvas.pack()

gazou = tkinter.PhotoImage(file="omi.png")
canvas.create_image(400, 300, image=gazou)

label = tkinter.Label(root, text="??", font=("Times New Roman", 40), bg="white")
label.place(x=30, y=40)
kimi = tkinter.Label(root, text="??", font=("Times New Roman", 30), bg="white")
kimi.place(x=30, y=130)

button = tkinter.Button(root, text="言い訳を考える", font=("Times New Roman", 36),command=click_btn, fg="skyblue")
button.place(x=360,y=400)
root.mainloop()
