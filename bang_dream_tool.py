import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def get_id_pass():
    no_training_text_get = []
    for i in range(8):
        no_training_text_get.append(no_training_text[i].get())

    unread_ep_text_get = []
    for i in range(16):
        unread_ep_text_get.append(unread_ep_text[i].get())

    unread_mem_ep_text_get = []
    for i in range(16):
        unread_mem_ep_text_get.append(unread_mem_ep_text[i].get())
    
    possession_text_get = []
    for i in range(12):
        possession_text_get.append(possession_text[i].get())

    numbers_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    crystal_text_get = crystal_text.get()
    num = 0

    for i in range(8):
        if no_training_text_get[i] == "":
            no_training_text_get[i] = 0

    for i in range(16):
        if unread_ep_text_get[i] == "":
            unread_ep_text_get[i] = 0
        if unread_mem_ep_text_get[i] == "":
            unread_mem_ep_text_get[i] = 0
    
    for i in range(12):
        if possession_text_get[i] == "":
            possession_text_get[i] = 0
    
    for i in range(8):
        if i % 2 == 0:
            numbers_3[(i // 2) * 3] += int(no_training_text_get[i]) * 1000
            numbers_3[(i // 2) * 3 + 1] += int(no_training_text_get[i]) * 300
        if i % 2 == 1:
            numbers_3[(i // 2) * 3 + 1] += int(no_training_text_get[i]) * 500
            numbers_3[(i // 2) * 3 + 2] += int(no_training_text_get[i]) * 50
            num += (int(no_training_text_get[i]) * 10)
    
    for i in range(16):
        if i % 4 == 0:
            numbers_3[(3 * i + 1) // 4] += int(unread_ep_text_get[i]) * 10
            numbers_3[(3 * i + 1) // 4] += int(unread_mem_ep_text_get[i]) * 50
            numbers_3[(3 * i + 1) // 4 + 1] += int(unread_mem_ep_text_get[i]) * 25
        elif i % 4 == 1:
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_ep_text_get[i]) * 100
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_mem_ep_text_get[i]) * 400
            numbers_3[(3 * i + 1) // 4] += int(unread_mem_ep_text_get[i]) * 150
        elif i % 4 == 2:
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_ep_text_get[i]) * 300
            numbers_3[(3 * i + 1) // 4] += int(unread_ep_text_get[i]) * 100
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_mem_ep_text_get[i]) * 1800
            numbers_3[(3 * i + 1) // 4] += int(unread_mem_ep_text_get[i]) * 1200
            numbers_3[(3 * i + 1) // 4 + 1] += int(unread_mem_ep_text_get[i]) * 300
        elif i % 4 == 3:
            numbers_3[(3 * i + 1) // 4 - 2] += int(unread_ep_text_get[i]) * 500
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_ep_text_get[i]) * 300
            numbers_3[(3 * i + 1) // 4 - 2] += int(unread_mem_ep_text_get[i]) * 2400
            numbers_3[(3 * i + 1) // 4 - 1] += int(unread_mem_ep_text_get[i]) * 1600
            numbers_3[(3 * i + 1) // 4] += int(unread_mem_ep_text_get[i]) * 400
    
    for i in range(12):
        numbers_3[i] = max(0, numbers_3[i] - int(possession_text_get[i]))
    
    if crystal_text_get == "":
        crystal_text_get = 0
    
    num = max(0, num - int(crystal_text_get))
    
    for i in range(12):
        needs[i]["text"] = str(numbers_3[i])
    
    crystal_needs["text"] = str(num)


def set_clear():
    if not messagebox.askokcancel(title="確認", message="クリアしてよろしいですか？"):
        return

    for i in range(8):
        no_training_text[i].set("")

    for i in range(16):
        unread_ep_text[i].set("")

    for i in range(16):
        unread_mem_ep_text[i].set("")

    for i in range(12):
        possession_text[i].set("")

    crystal_text.set("")

    for i in range(12):
        needs[i]["text"] = "0"
    
    crystal_needs["text"] = "0"


def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("BDTファイル", "*.bdt")], initialdir=doc_path)

    with open(file_name) as f:
        data_file = f.readlines()

    data_list = []
    for data in data_file:
        data = data.rstrip("\n")
        if data == "0":
            data = ""
        data_list.append(data)
    
    for i in range(8):
        no_training_text[i].set(data_list[i])

    for i in range(16):
        unread_ep_text[i].set(data_list[i + 8])
    
    for i in range(16):
        unread_mem_ep_text[i].set(data_list[i + 24])
    
    for i in range(12):
        possession_text[i].set(data_list[i + 40])
    
    crystal_text.set(data_list[52])


def save_file():
    data_list = []
    for i in range(8):
        data_list.append(no_training_text[i].get())

    for i in range(16):
        data_list.append(unread_ep_text[i].get())

    for i in range(16):
        data_list.append(unread_mem_ep_text[i].get())
    
    for i in range(12):
        data_list.append(possession_text[i].get())
    
    data_list.append(crystal_text.get())

    data_file = ""
    for data in data_list:
        if data == "":
            data = "0"
        data_file += data + "\n"

    file_name = ""

    file_name = filedialog.asksaveasfilename(filetypes=[("BDTファイル", "*.bdt")], initialdir=doc_path, initialfile=".bdt")
    if os.path.basename(file_name) == ".bdt" or os.path.splitext(file_name)[1] != ".bdt":
        messagebox.showerror(title="エラー", message="やり直してください")
    else:
        with open(file_name, "w") as f:
            f.write(data_file)
        messagebox.showinfo(title="情報", message="保存しました")


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap(default=os.path.join(sys._MEIPASS, "bang_dream_tool.ico"))
    root.title("Bang Dream! Tool")
    root.resizable(False, False)

    doc_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents"
    print(doc_path)

    no_training_label = [ttk.Label(root, text="未特訓キャラ数"),
                        ttk.Label(root, text="パワフル"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="クール"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ピュア"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ハッピー"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4")]

    unread_ep_label = [ttk.Label(root, text="エピソード未読キャラ数"),
                    ttk.Label(root, text="パワフル"),
                    ttk.Label(root, text="★1"),
                    ttk.Label(root, text="★2"),
                    ttk.Label(root, text="★3"),
                    ttk.Label(root, text="★4"),
                    ttk.Label(root, text=""),
                    ttk.Label(root, text="クール"),
                    ttk.Label(root, text="★1"),
                    ttk.Label(root, text="★2"),
                    ttk.Label(root, text="★3"),
                    ttk.Label(root, text="★4"),
                    ttk.Label(root, text=""),
                    ttk.Label(root, text="ピュア"),
                    ttk.Label(root, text="★1"),
                    ttk.Label(root, text="★2"),
                    ttk.Label(root, text="★3"),
                    ttk.Label(root, text="★4"),
                    ttk.Label(root, text=""),
                    ttk.Label(root, text="ハッピー"),
                    ttk.Label(root, text="★1"),
                    ttk.Label(root, text="★2"),
                    ttk.Label(root, text="★3"),
                    ttk.Label(root, text="★4")]

    unread_mem_ep_label = [ttk.Label(root, text="メモリアルエピソード未読キャラ数"),
                        ttk.Label(root, text="パワフル"),
                        ttk.Label(root, text="★1"),
                        ttk.Label(root, text="★2"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="クール"),
                        ttk.Label(root, text="★1"),
                        ttk.Label(root, text="★2"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ピュア"),
                        ttk.Label(root, text="★1"),
                        ttk.Label(root, text="★2"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ハッピー"),
                        ttk.Label(root, text="★1"),
                        ttk.Label(root, text="★2"),
                        ttk.Label(root, text="★3"),
                        ttk.Label(root, text="★4")]

    possession_label = [ttk.Label(root, text="アイテムの現在所持数"),
                        ttk.Label(root, text="パワフルのかけら"),
                        ttk.Label(root, text="小"),
                        ttk.Label(root, text="中"),
                        ttk.Label(root, text="大"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="クールのかけら"),
                        ttk.Label(root, text="小"),
                        ttk.Label(root, text="中"),
                        ttk.Label(root, text="大"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ピュアのかけら"),
                        ttk.Label(root, text="小"),
                        ttk.Label(root, text="中"),
                        ttk.Label(root, text="大"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="ハッピーのかけら"),
                        ttk.Label(root, text="小"),
                        ttk.Label(root, text="中"),
                        ttk.Label(root, text="大"),
                        ttk.Label(root, text=""),
                        ttk.Label(root, text="奇跡のクリスタル")]

    needs_label = [ttk.Label(root, text="アイテムの不足数"),
                ttk.Label(root, text="パワフルのかけら"),
                ttk.Label(root, text="小"),
                ttk.Label(root, text="中"),
                ttk.Label(root, text="大"),
                ttk.Label(root, text=""),
                ttk.Label(root, text="クールのかけら"),
                ttk.Label(root, text="小"),
                ttk.Label(root, text="中"),
                ttk.Label(root, text="大"),
                ttk.Label(root, text=""),
                ttk.Label(root, text="ピュアのかけら"),
                ttk.Label(root, text="小"),
                ttk.Label(root, text="中"),
                ttk.Label(root, text="大"),
                ttk.Label(root, text=""),
                ttk.Label(root, text="ハッピーのかけら"),
                ttk.Label(root, text="小"),
                ttk.Label(root, text="中"),
                ttk.Label(root, text="大"),
                ttk.Label(root, text=""),
                ttk.Label(root, text="奇跡のクリスタル"),
                ttk.Label(root, text="")]

    needs = [ttk.Label(root, text="0"), ttk.Label(root, text="0"),
            ttk.Label(root, text="0"), ttk.Label(root, text="0"),
            ttk.Label(root, text="0"), ttk.Label(root, text="0"),
            ttk.Label(root, text="0"), ttk.Label(root, text="0"),
            ttk.Label(root, text="0"), ttk.Label(root, text="0"),
            ttk.Label(root, text="0"), ttk.Label(root, text="0")]

    span_label = ttk.Label(root, text="")

    crystal_needs = ttk.Label(root, text="0")

    no_training_text = [StringVar(), StringVar(), StringVar(), StringVar(),
                        StringVar(), StringVar(), StringVar(), StringVar()]

    unread_ep_text = [StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), StringVar()]

    unread_mem_ep_text = [StringVar(), StringVar(), StringVar(), StringVar(),
                        StringVar(), StringVar(), StringVar(), StringVar(),
                        StringVar(), StringVar(), StringVar(), StringVar(),
                        StringVar(), StringVar(), StringVar(), StringVar()]

    possession_text = [StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), StringVar()]

    crystal_text = StringVar()

    no_training_entry = []
    for i in range(8):
        no_training_entry.append(ttk.Entry(root, textvariable=no_training_text[i], width=10))

    unread_ep_entry = []
    for i in range(16):
        unread_ep_entry.append(ttk.Entry(root, textvariable=unread_ep_text[i], width=10))

    unread_mem_ep_entry = []
    for i in range(16):
        unread_mem_ep_entry.append(ttk.Entry(root, textvariable=unread_mem_ep_text[i], width=10))

    possession_entry = []
    for i in range(12):
        possession_entry.append(ttk.Entry(root, textvariable=possession_text[i], width=10))

    crystal_entry = ttk.Entry(root, textvariable=crystal_text, width=10)

    button_1 = ttk.Button(root, text='計算', command=lambda:get_id_pass())
    button_2 = ttk.Button(root, text='クリア', command=lambda:set_clear())
    button_3 = ttk.Button(root, text='開く', command=lambda:open_file())
    button_4 = ttk.Button(root, text='保存', command=lambda:save_file())

    no_training_label[0].grid(row=0, column=0, columnspan=3, pady=10)
    no_training_label[1].grid(row=1, column=0, rowspan=2, padx=10, sticky=NW)
    no_training_label[2].grid(row=1, column=1)
    no_training_label[3].grid(row=2, column=1)
    no_training_label[4].grid(row=3, column=1)
    no_training_label[5].grid(row=4, column=0, rowspan=2, padx=10, sticky=NW)
    no_training_label[6].grid(row=4, column=1)
    no_training_label[7].grid(row=5, column=1)
    no_training_label[8].grid(row=6, column=1)
    no_training_label[9].grid(row=7, column=0, rowspan=2, padx=10, sticky=NW)
    no_training_label[10].grid(row=7, column=1)
    no_training_label[11].grid(row=8, column=1)
    no_training_label[12].grid(row=9, column=1)
    no_training_label[13].grid(row=10, column=0, rowspan=2, padx=10, sticky=NW)
    no_training_label[14].grid(row=10, column=1)
    no_training_label[15].grid(row=11, column=1)

    unread_ep_label[0].grid(row=0, column=3, columnspan=3)
    unread_ep_label[1].grid(row=1, column=3, rowspan=2, padx=10, sticky=NW)
    unread_ep_label[2].grid(row=1, column=4)
    unread_ep_label[3].grid(row=2, column=4)
    unread_ep_label[4].grid(row=3, column=4)
    unread_ep_label[5].grid(row=4, column=4)
    unread_ep_label[6].grid(row=5, column=4)
    unread_ep_label[7].grid(row=6, column=3, rowspan=2, padx=10, sticky=NW)
    unread_ep_label[8].grid(row=6, column=4)
    unread_ep_label[9].grid(row=7, column=4)
    unread_ep_label[10].grid(row=8, column=4)
    unread_ep_label[11].grid(row=9, column=4)
    unread_ep_label[12].grid(row=10, column=4)
    unread_ep_label[13].grid(row=11, column=3, rowspan=2, padx=10, sticky=NW)
    unread_ep_label[14].grid(row=11, column=4)
    unread_ep_label[15].grid(row=12, column=4)
    unread_ep_label[16].grid(row=13, column=4)
    unread_ep_label[17].grid(row=14, column=4)
    unread_ep_label[18].grid(row=15, column=4)
    unread_ep_label[19].grid(row=16, column=3, rowspan=2, padx=10, sticky=NW)
    unread_ep_label[20].grid(row=16, column=4)
    unread_ep_label[21].grid(row=17, column=4)
    unread_ep_label[22].grid(row=18, column=4)
    unread_ep_label[23].grid(row=19, column=4)

    unread_mem_ep_label[0].grid(row=0, column=6, columnspan=3)
    unread_mem_ep_label[1].grid(row=1, column=6, rowspan=2, padx=10, sticky=NW)
    unread_mem_ep_label[2].grid(row=1, column=7)
    unread_mem_ep_label[3].grid(row=2, column=7)
    unread_mem_ep_label[4].grid(row=3, column=7)
    unread_mem_ep_label[5].grid(row=4, column=7)
    unread_mem_ep_label[6].grid(row=5, column=7)
    unread_mem_ep_label[7].grid(row=6, column=6, rowspan=2, padx=10, sticky=NW)
    unread_mem_ep_label[8].grid(row=6, column=7)
    unread_mem_ep_label[9].grid(row=7, column=7)
    unread_mem_ep_label[10].grid(row=8, column=7)
    unread_mem_ep_label[11].grid(row=9, column=7)
    unread_mem_ep_label[12].grid(row=10, column=7)
    unread_mem_ep_label[13].grid(row=11, column=6, rowspan=2, padx=10, sticky=NW)
    unread_mem_ep_label[14].grid(row=11, column=7)
    unread_mem_ep_label[15].grid(row=12, column=7)
    unread_mem_ep_label[16].grid(row=13, column=7)
    unread_mem_ep_label[17].grid(row=14, column=7)
    unread_mem_ep_label[18].grid(row=15, column=7)
    unread_mem_ep_label[19].grid(row=16, column=6, rowspan=2, padx=10, sticky=NW)
    unread_mem_ep_label[20].grid(row=16, column=7)
    unread_mem_ep_label[21].grid(row=17, column=7)
    unread_mem_ep_label[22].grid(row=18, column=7)
    unread_mem_ep_label[23].grid(row=19, column=7)

    possession_label[0].grid(row=0, column=9, columnspan=3)
    possession_label[1].grid(row=1, column=9, rowspan=2, padx=10, sticky=NW)
    possession_label[2].grid(row=1, column=10)
    possession_label[3].grid(row=2, column=10)
    possession_label[4].grid(row=3, column=10)
    possession_label[5].grid(row=4, column=10)
    possession_label[6].grid(row=5, column=9, rowspan=2, padx=10, sticky=NW)
    possession_label[7].grid(row=5, column=10)
    possession_label[8].grid(row=6, column=10)
    possession_label[9].grid(row=7, column=10)
    possession_label[10].grid(row=8, column=10)
    possession_label[11].grid(row=9, column=9, rowspan=2, padx=10, sticky=NW)
    possession_label[12].grid(row=9, column=10)
    possession_label[13].grid(row=10, column=10)
    possession_label[14].grid(row=11, column=10)
    possession_label[15].grid(row=12, column=10)
    possession_label[16].grid(row=13, column=9, rowspan=2, padx=10, sticky=NW)
    possession_label[17].grid(row=13, column=10)
    possession_label[18].grid(row=14, column=10)
    possession_label[19].grid(row=15, column=10)
    possession_label[20].grid(row=16, column=10)
    possession_label[21].grid(row=17, column=9, columnspan=2, padx=10, sticky=NW)

    needs_label[0].grid(row=0, column=12, columnspan=3)
    needs_label[1].grid(row=1, column=12, rowspan=2, padx=10, sticky=NW)
    needs_label[2].grid(row=1, column=13)
    needs_label[3].grid(row=2, column=13)
    needs_label[4].grid(row=3, column=13)
    needs_label[5].grid(row=4, column=13)
    needs_label[6].grid(row=5, column=12, rowspan=2, padx=10, sticky=NW)
    needs_label[7].grid(row=5, column=13)
    needs_label[8].grid(row=6, column=13)
    needs_label[9].grid(row=7, column=13)
    needs_label[10].grid(row=8, column=13)
    needs_label[11].grid(row=9, column=12, rowspan=2, padx=10, sticky=NW)
    needs_label[12].grid(row=9, column=13)
    needs_label[13].grid(row=10, column=13)
    needs_label[14].grid(row=11, column=13)
    needs_label[15].grid(row=12, column=13)
    needs_label[16].grid(row=13, column=12, rowspan=2, padx=10, sticky=NW)
    needs_label[17].grid(row=13, column=13)
    needs_label[18].grid(row=14, column=13)
    needs_label[19].grid(row=15, column=13)
    needs_label[20].grid(row=16, column=12)
    needs_label[21].grid(row=17, column=12, columnspan=2, padx=10, sticky=NW)

    needs[0].grid(row=1, column=14, padx=10, sticky=W)
    needs[1].grid(row=2, column=14, padx=10, sticky=W)
    needs[2].grid(row=3, column=14, padx=10, sticky=W)
    needs[3].grid(row=5, column=14, padx=10, sticky=W)
    needs[4].grid(row=6, column=14, padx=10, sticky=W)
    needs[5].grid(row=7, column=14, padx=10, sticky=W)
    needs[6].grid(row=9, column=14, padx=10, sticky=W)
    needs[7].grid(row=10, column=14, padx=10, sticky=W)
    needs[8].grid(row=11, column=14, padx=10, sticky=W)
    needs[9].grid(row=13, column=14, padx=10, sticky=W)
    needs[10].grid(row=14, column=14, padx=10, sticky=W)
    needs[11].grid(row=15, column=14, padx=10, sticky=W)

    crystal_needs.grid(row=17, column=14, padx=10, sticky=W)

    no_training_entry[0].grid(row=1, column=2, padx=10)
    no_training_entry[1].grid(row=2, column=2)
    no_training_entry[2].grid(row=4, column=2)
    no_training_entry[3].grid(row=5, column=2)
    no_training_entry[4].grid(row=7, column=2)
    no_training_entry[5].grid(row=8, column=2)
    no_training_entry[6].grid(row=10, column=2)
    no_training_entry[7].grid(row=11, column=2)

    unread_ep_entry[0].grid(row=1, column=5, padx=10)
    unread_ep_entry[1].grid(row=2, column=5)
    unread_ep_entry[2].grid(row=3, column=5)
    unread_ep_entry[3].grid(row=4, column=5)
    unread_ep_entry[4].grid(row=6, column=5)
    unread_ep_entry[5].grid(row=7, column=5)
    unread_ep_entry[6].grid(row=8, column=5)
    unread_ep_entry[7].grid(row=9, column=5)
    unread_ep_entry[8].grid(row=11, column=5)
    unread_ep_entry[9].grid(row=12, column=5)
    unread_ep_entry[10].grid(row=13, column=5)
    unread_ep_entry[11].grid(row=14, column=5)
    unread_ep_entry[12].grid(row=16, column=5)
    unread_ep_entry[13].grid(row=17, column=5)
    unread_ep_entry[14].grid(row=18, column=5)
    unread_ep_entry[15].grid(row=19, column=5)

    unread_mem_ep_entry[0].grid(row=1, column=8, padx=10)
    unread_mem_ep_entry[1].grid(row=2, column=8)
    unread_mem_ep_entry[2].grid(row=3, column=8)
    unread_mem_ep_entry[3].grid(row=4, column=8)
    unread_mem_ep_entry[4].grid(row=6, column=8)
    unread_mem_ep_entry[5].grid(row=7, column=8)
    unread_mem_ep_entry[6].grid(row=8, column=8)
    unread_mem_ep_entry[7].grid(row=9, column=8)
    unread_mem_ep_entry[8].grid(row=11, column=8)
    unread_mem_ep_entry[9].grid(row=12, column=8)
    unread_mem_ep_entry[10].grid(row=13, column=8)
    unread_mem_ep_entry[11].grid(row=14, column=8)
    unread_mem_ep_entry[12].grid(row=16, column=8)
    unread_mem_ep_entry[13].grid(row=17, column=8)
    unread_mem_ep_entry[14].grid(row=18, column=8)
    unread_mem_ep_entry[15].grid(row=19, column=8)

    possession_entry[0].grid(row=1, column=11, padx=10)
    possession_entry[1].grid(row=2, column=11)
    possession_entry[2].grid(row=3, column=11)
    possession_entry[3].grid(row=5, column=11)
    possession_entry[4].grid(row=6, column=11)
    possession_entry[5].grid(row=7, column=11)
    possession_entry[6].grid(row=9, column=11)
    possession_entry[7].grid(row=10, column=11)
    possession_entry[8].grid(row=11, column=11)
    possession_entry[9].grid(row=13, column=11)
    possession_entry[10].grid(row=14, column=11)
    possession_entry[11].grid(row=15, column=11)

    crystal_entry.grid(row=17, column=11)

    button_1.grid(row=20, column=12, columnspan=2, sticky=E)
    button_2.grid(row=21, column=12, columnspan=2, sticky=E)
    button_3.grid(row=20, column=14)
    button_4.grid(row=21, column=14)

    root.mainloop()
