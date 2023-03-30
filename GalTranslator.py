import easyocr
from PIL import ImageGrab
import openai
import time
import threading
import tkinter


openai.api_key = "" # 填你自己的API_key，B站有申请教程
model_engine = "gpt-3.5-turbo"
output = '翻译中....'


def getScreen(x1, y1, x2, y2):
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screen.save("jptr.jpg")
    # record = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(record, x, y, w, h).toImage()
    # img.save("D:\\pythonProject1\\" + "jptr.jpg")


def translate(inputs):
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": "请将我下面一句英文话直接翻译成中文，这句话出自一款galgame，翻译时请不要添加任何修饰和多余的描述，也不要出现任何与翻译结果无关的内容：" + inputs}
        ],
        max_tokens=1500
    )
    return response['choices'][0]['message']['content']


def gettext(path):
    reader = easyocr.Reader(['ja'])
    result = reader.readtext(image=path, detail=0, paragraph=True)
    return result


def form():
    wins = tkinter.Tk()
    wins.title("Translator")
    wins.geometry('400x200')
    l1 = tkinter.Label(wins, text='', width=400).place(x=1, y=1)
    wins.mainloop()
    l1.config(text=output)


def trans():
    while True:
        time.sleep(5)
        getScreen(532, 712, 1381, 804) # 翻译区域，前两个参数是区域左上坐标后两个是右下坐标
        text = gettext('jptr.jpg')
        print(text)
        output = translate(text[0])
        print(output)


if __name__ == '__main__':
    # t1 = threading.Thread(target=form)
    t2 = threading.Thread(target=trans)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # t1.start()
    t2.start()

