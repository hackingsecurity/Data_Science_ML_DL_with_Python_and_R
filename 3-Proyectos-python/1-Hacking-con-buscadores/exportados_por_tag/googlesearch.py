# Instalación de librerias
import requests as rq


class GoogleSearch:
    def __init__(self, api_key, engine_id):
        """
            Inicializa una nueva instancia de GoogleSearch
            
            Esta clase permite realizar peticiones automatizadas a la api de Google.
            
            api_key (str) : Clave Api de Google
            engine_id (str) : Identificador del motor de búsqueda personalizada de Google.
            
        """
        
        self.api_key = api_key
        self.engine_id = engine_id
        
        
    def search(self, query, start_page=1, pages=1, lang="lang_es"):
        """
            Realiza una búsqueda en Google, utilizando su API.
            
            
        """
        
        final_result = []
        result_per_page = 10 # google muestra por defecto 10 resultados por página
        
        for page in range(pages):
            
            # Calculamos el resultado de comienzo de cada págnia
            start_index = (start_page - 1) * result_per_page + 1 + (page * result_per_page)
            
            urlTarget = f"https://www.googleapis.com/customsearch/v1?key={secret}&cx={cx}&q={query}&start={start_page}&lr={lang}"
    
            response = rq.get(urlTarget)
            
            if response.status_code == 200:
                data = response.json()
                result = data.get("items")
                cresults = self.custom_results(result)
                final_result.extend(cresults)
            else:
                print(f"Se ha producido un error")
                break
        
        return final_result

    def custom_results(self, results):

        """ 
            Filtra los resultado de la consulta
        """

        custom_results = []
        
        for r in results:
            cresult = {}
            cresult["title"] = r.get("title")
            cresult["descripcion"] = r.get("snippet")
            cresult["link"] = r.get("link")
            custom_results.append(cresult)   

        return custom_results
