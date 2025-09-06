import speech_recognition as sr#імпортуємо бібліотеку
import subprocess
import webbrowser
import pyowm
owm = pyowm.OWM('5817d6a145c443107efc34417e35c2ac')
raspoznovatel = sr.Recognizer()#створюємо об'єкт який відповідає за розпізнавання мови
def vvod_golosa():#запис аудио
    with sr.Microphone() as source:# используем микрофон как источник звука
        print("слухаю")
        audio = raspoznovatel.listen(source)#слушаем звук с микро
    return audio#возвращаем аудио запись
def iz_golosa_v_tekst(audio):#розпізнаввая мови
    try:
        #преобразуем речь в текст с помощью google speach recognition language какой язик будет розпозновать
        text = raspoznovatel.recognize_google(audio,language = 'uk-UK')
        print("Ви сказали" + text)
    except:
        text = ""
        print("моя твоя не понимать")
    return text#возвращаем текст
def golosova_comanda(text):
    if "привіт" in text.lower():
        print("хелоу")
    elif "как дела" in text.lower():
        print("cупер")
    elif "калькулятор" in text.lower():
        subprocess.call(['calc'])
    elif "roblox" in text.lower() or "роблокс" in text.lower():
        subprocess.call(["C:/Users/LOGIKA/AppData/Local/Roblox/Versions/version-65664807ac1d4e85/RobloxPlayerBeta.exe"])
    elif "дизайнер" in text.lower():
        subprocess.call(["C:\Program Files (x86)\Qt Designer\designer.exe"])
    elif "youtube" in text.lower():
        webbrowser.open(f"https://www.youtube.com/results?search_query={text.lower()[7:]}")
    elif "погода" in text.lower():
        place = text.lower()[7:]
        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather = "Температура" + str(int(weather.temperature('celsius')['temp']))
        print(weather)
    else:
        print("моя втоя не понимать")
def main():#функція main, щоб запустити створені раніше функції.
    end_program = False
    while not end_program:
        audio = vvod_golosa()
        text = iz_golosa_v_tekst(audio)
        text = golosova_comanda(text)
if __name__ == "__main__":#точка входа в програму
    main()