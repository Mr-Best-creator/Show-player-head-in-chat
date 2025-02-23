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
label1.pack()

string_ver1 = tk.StringVar(master=root)
text1 = tk.Entry(master=root, textvariable=string_ver1, width=75)
text1.pack()


def copy_to_clipboard():
    copy_text = text1.get()
    root.clipboard_clear()
    root.clipboard_append(copy_text)
    root.update()


copy_button = tk.Button(master=root, text="クリップボードにコピー", command=copy_to_clipboard)
copy_button.pack()


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
            temp_head_list = []
            for a in head:
                for b in a:
                    temp_head_list.append(b)
                temp_head_list.append(r"\n")
            
            temp_text = ""
            last_color = ""
            for i in range(len(temp_head_list)):
                if temp_head_list[i] == r"\n":
                    temp_text += r"\n"
                else:
                    if last_color == "":
                        temp_text += "█"
                        last_color = temp_head_list[i]
                    elif last_color == temp_head_list[i]:
                        temp_text += "█"
                    else:
                        command += ',{\"text\":\"' + temp_text + '\",\"color\":\"' + last_color + '\"}'
                        temp_text = ""
                        last_color = temp_head_list[i]
                        temp_text += "█"
            
            
    command += ',{\"text\":\"' + temp_text + '\",\"color\":\"' + last_color + '\"}'
    command += ',{\"text\":\"' + os.path.splitext(os.path.basename(player_skin_file_path))[0] + '\",\"color\":\"#FFFFFF\"}]'

    string_ver1.set(command)
            

button1.config(command=open_and_convert)

root.mainloop()