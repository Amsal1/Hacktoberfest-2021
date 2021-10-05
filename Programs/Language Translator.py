from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
#import traceback

root = Tk()

root.geometry('450x350')
root.title("_MT_")
root.wm_iconbitmap("lang.ico")
root.config(bg="#FCD4B7")
root.resizable(False, False)
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
             'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
             'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
             'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da',
             'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
             'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
             'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi',
             'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga',
             'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
             'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
             'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
             'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
             'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
             'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
             'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd',
             'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
             'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
             'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
             'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def enter(event=None):
    try:
        word3 = TextBlob(var1.get())
        lan = word3.detect_language()
        lan_todict = lang.get()
        lan_to = lang_dict[lan_todict]
        word3 = word3.translate(from_lang=lan, to=lan_to)
        label3.configure(text=word3)
        var2.set(word3)
    except:
        var2.set('Try another language')



def EXIST():
    dis_msg = messagebox.askokcancel("Notification", "Do you want to exist", parent=root)
    if dis_msg:
        root.destroy()


def on_enterentry1(e):
    entry1['bg'] = '#1CD8D2'


def on_leaveentry1(e):
    entry1['bg'] = 'white'


def on_enterentry2(e):
    entry2['bg'] = '#1CD8D2'


def on_leaveentry2(e):
    entry2['bg'] = 'white'


def on_enterb1(e):
    b1['bg'] = '#3CD3AD'


def on_leaveb1(e):
    b1['bg'] = 'grey'


def on_enterb2(e):
    b2['bg'] = '#3CD3AD'


def on_leaveb2(e):
    b2['bg'] = 'grey'


# combobox
lang = StringVar()
lang_combo = Combobox(root, width=21, textvariabl=lang, state='readonly')
lang_combo['values'] = [e for e in lang_dict.keys()]
lang_combo.current(37)
lang_combo.place(x=300, y=0)
# 1st entry widget
var1 = StringVar()
entry1 = Entry(root, width=30, textvariable=var1, font=('times', 15, 'italic bold'))
entry1.place(x=120, y=70)

var2 = StringVar()
entry2 = Entry(root, width=30, textvariable=var2, font=('times', 15, 'italic bold'), relief=RIDGE)
entry2.place(x=120, y=170)

# labels
label1 = Label(root, text="Enter Words: ", font=('times', 12, 'italic bold'), bg='#FCD4B7')
label1.place(x=5, y=68)

label2 = Label(root, text="Output: ", font=('times', 12, 'italic bold'), bg='#FCD4B7')
label2.place(x=5, y=169)
label3 = Label(root, text='', font=('times', 12, 'italic bold'), bg='#FCD4B7')
label3.place(x=10, y=269)

# Buttons
b1 = Button(root, text='Enter', bd=7, bg='grey', fg='yellow', activebackground='red', width=8, relief=RAISED,
            command=enter)
b1.place(x=185, y=230)
b2 = Button(root, text='Exist', bd=7, bg='grey', fg='yellow', activebackground='red', width=8, relief=RAISED,
            command=EXIST)
b2.place(x=300, y=230)
root.bind('<Return>', enter)

# binding
entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

b1.bind('<Enter>', on_enterb1)
b1.bind('<Leave>', on_leaveb1)

b2.bind('<Enter>', on_enterb2)
b2.bind('<Leave>', on_leaveb2)

root.mainloop()
