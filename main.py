from tkinter import *
from tkinter import filedialog
import PyPDF2
from gtts import gTTS
from io import BytesIO

window = Tk()
window.title('Pdf to Audiobook Converter')
window.geometry('800x800')
window.config(padx=50, pady=50)
mp3_fp = BytesIO()

def open_pdf_file():
    file_type = [('PDF FILE', '*.pdf'), ("All Files", '*.*')]
    file_path = filedialog.askopenfilenames(initialdir='/', title="Select Pdf", filetypes=file_type)
    for pdf_file in file_path:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text().replace(" ", "")
                print(text)
    text_box.delete("1.0", END)
    text_box.insert(END, text)

def convert_text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en',)
    tts.save(output_file)
    tts.write_to_fp(output_file)

def convert_to_audio():
    text = text_box.get("1.0", END)
    output_file = filedialog.asksaveasfilename(defaultextension="mp3", filetypes=[('MP3 FILES', "*.mp3")])
    if text and output_file:
        convert_text_to_speech(text, output_file)

title_label = Label(text="Convert your Pdf file to Audio Book", font=('Arial', 20, 'normal'), anchor='center')
title_label.grid(row=0, column=1, padx=20, pady=20)

choose_label = Label(text='Choose a File:', anchor='w')
choose_label.grid(row=1, column=0, padx=20, pady=20, sticky='w')

open_file = Button(text="Open", width=15, command=open_pdf_file)
open_file.grid(row=1, column=1, sticky='w', pady=10)

text_box = Text(window, height=20, width=60)
text_box.grid(row=2, column=1, columnspan=2, padx=20, pady=20, sticky='w')

play_btn = Button(text="⏯ Play Audio", width=15, command=convert_to_audio)
play_btn.grid(row=3, column=1, sticky='w', pady=10)

window.mainloop()