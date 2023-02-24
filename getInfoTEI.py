import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from lxml import etree
import glob
import requests
from pathlib import Path
import time

def get_file_names():
    file_list = glob.glob("./Files/PDFs/*.pdf")
    return file_list

def join_paragraphs(soup):
    p_elements = soup.find_all("p")

    unique_string=""

    for p in p_elements:
        unique_string+=" "+p.text

    if(unique_string==""):
        return "NONE"
    return unique_string

def plot_cloud(file, unique_string):
    wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.savefig("./Files/output/"+file+".png")
    plt.axis("off")
    plt.clf()

def count_figures(soup):
    figures = soup.find_all("figure")
    return len(figures)
    
def plot_number_figures_per_articule(files, figures_per_article):
    plt.bar(files, figures_per_article)
    plt.savefig("./Files/output/barChart.png")

def list_links(soup):
    with open("./Files/output/links.txt", "a") as f:
        links = soup.find_all("ptr")
        f.write("----------------------------------------------------------------\n")
        f.write(soup.title.text + "\n")
        f.write("----------------------------------------------------------------\n")
        for link in links:
            f.write(link['target'] + "\n")
        f.write("----------------------------------------------------------------\n")
        f.write("\n\n")

def handle_requests(f):
    try:
        response = requests.post('https://kermitt2-grobid.hf.space/api/processFulltextDocument', files=f)
        if response.status_code == 200:
            return response   
    except requests.exceptions.RequestException:
        try:
            print("Usando segundo contenedor")
            response = requests.post('http://localhost:8071/api/processFulltextDocument', files=f)#https://kermitt2-grobid.hf.space/
            if response.status_code == 200:
                print("respuesta 2do contenedor")
                return response
        except requests.exceptions.RequestException:
            print("ALERTA: Grobid no logró procesar el archivo")
            print('Esperando que el servidor reinicie...')
            time.sleep(30)
            return False

def main():
    files = get_file_names()
    files_names =[]
    figures_per_article = []
    flag = False
    for file in files:
        print("Procesando: "+file)
        f = {'input': open(file, 'rb')}
        
        response=handle_requests(f)
        if response:
            soup = BeautifulSoup(response.content, "xml")
            file_name=Path(file).stem
            print(soup.title.text)
            files_names.append(file_name)
            plot_cloud(file_name, join_paragraphs(soup))
            figures_per_article.append(count_figures(soup))
            list_links(soup)
        # except:
        #     print("ALERTA: Grobid no logró procesar el archivo")
        #     print('Esperando que el servidor reinicie...')
        #     time.sleep(30)
            
                
            
        # try:
        #     response = requests.post('http://localhost:8070/api/processFulltextDocument', files=f)
        #     soup = BeautifulSoup(response.content, "xml")
        #     print(soup.title.text)
        #     file_name=Path(file).stem
        #     files_names.append(file_name)
        #     plot_cloud(file_name, join_paragraphs(soup))
        #     figures_per_article.append(count_figures(soup))
        #     list_links(soup)
        # except requests.exceptions.ConnectionError as e:
        #     # manejar el error de conexión
        #     print("Ocurrió un error de conexión: ", e)
        
        
    plot_number_figures_per_articule(files_names, figures_per_article)

if __name__ == "__main__":
    main()
