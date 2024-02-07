# Tomas Farias
# Importar los módulos necesarios para web scraping.
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# URL del feed RSS de noticias para Chile
news_url_chile = "https://news.google.com/rss?hl=es-419&gl=CL&ceid=CL:es-419"

# Abrir la URL utilizando 'urlopen' y leer el contenido de la página web.
with urlopen(news_url_chile) as client:
    xml_page = client.read()

# Crear un objeto BeautifulSoup para analizar el contenido XML de la página web.
soup_page = soup(xml_page, "xml")

# Encontrar todas las etiquetas XML con el nombre "item" para extraer las noticias.
news_list = soup_page.findAll("item")

# Imprimir el título, la URL y la fecha de publicación para cada noticia.
for news in news_list:
    print("Título:", news.title.text)
    print("URL:", news.link.text)
    print("Fecha de Publicación:", news.pubDate.text)
    print("-" * 60)
