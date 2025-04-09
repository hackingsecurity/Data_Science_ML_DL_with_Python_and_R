import requests as rq
import dotenv
import os


dotenv_path = os.path.expanduser("~/.env/.env")
dotenv.load_dotenv(dotenv_path)


start_page = 1
query = "Hacking Etico"
lang = "lang_es"  # lang_en
secret = os.getenv("API_GOOGLE")
cx = os.getenv("API_CS")

urlTarget = f"https://www.googleapis.com/customsearch/v1?key={secret}&cx={cx}&q={query}&start={start_page}&lr={lang}"
data = rq.get(urlTarget).json() # lo parseamos a un Json

print(data)
#print(dir(data))

#ver las claves del diccionario
print(dir(data))

print(data.get("items"))


result = data.get("items")

for r in result:
    print("-----Nuevo resultado-----")
    print(r.get("title")) # titulo
    print(r.get("snippet")) # descripción
    print(r.get("link")) # Enlance

