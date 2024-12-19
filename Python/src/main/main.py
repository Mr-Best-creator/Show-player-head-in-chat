import os
import tkinter as tk
import tkinter.filedialog as tkf

from PIL import Image


root = tk.Tk()
root.title("Show Player head in Chat (1.16 ~ ?)")
root.geometry("500x100")

button1 = tk.Button(master=root, text="ファイルを選択して生成する")
button1.pack()

label1 = tk.Label(master=root, text="↓生成されたコマンド(1.16+)")

string_ver1 = tk.StringVar(master=root)
text1 = tk.Entry(master=root, textvariable=string_ver1)
text1.pack()

def open_and_convert():
    player_skin_file_path = tkf.askopenfilename(filetypes=[(".png", "*.png")], initialdir=os.path.abspath(os.path.dirname(__file__)), title="プレイヤースキン(.pngファイル)を選択してコマンドを生成する")
    
    if os.path.isfile(player_skin_file_path):
        if os.path.splitext(player_skin_file_path)[1] == ".png":
            open_skin = Image.open(fp=player_skin_file_path, mode="r")
            open_skin = open_skin.convert("RGB")
            width, height = open_skin.size
            skin_data = list(open_skin.getdata())
            skin = [[f"#{r:02X}{g:02X}{b:02X}" for r, g, b in skin_data[i * width:(i + 1) * width]]for i in range(height)]
            
            command = '/tellraw @a [\"\"'
            head_start_x = 8
            head_start_y = 8
            head_end_x = head_start_x + 8
            head_end_y = head_start_y + 8
            
            head = [row[head_start_x:head_end_x] for row in skin[head_start_y:head_end_y]]
            
            for data_list in head:
                for data in data_list:
                    command += ',{\"text\":\"█\",\"color\":\"' + data + '\"}'
                command += ',\"\\n\"'
            command += ',{\"text\":\"' + os.path.splitext(os.path.basename(player_skin_file_path))[0] + '\",\"color\":\"#FFFFFF\"}]'
            
            
            string_ver1.set(command)
            

button1.config(command=open_and_convert)

root.mainloop()