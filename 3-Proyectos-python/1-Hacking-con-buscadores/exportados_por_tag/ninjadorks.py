# Librerias
import dotenv
import os
#Cargamos variable de entorno
dotenv_path = os.path.expanduser("~/.env/.env")
dotenv.load_dotenv(dotenv_path)
# Parámetro para consulta
start_page = 1
query = "Hacking Etico"
lang = "lang_es"  # lang_en
secret = os.getenv("API_GOOGLE")
cx = os.getenv("API_CS")
