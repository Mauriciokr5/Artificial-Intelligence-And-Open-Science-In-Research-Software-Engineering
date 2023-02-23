import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import glob
import requests
from pathlib import Path

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
    links = soup.find_all("ptr")
    print("----------------------------------------------------------------")
    print(soup.title.text)
    print("----------------------------------------------------------------")
    for link in links:
        print(link['target'])
    print("----------------------------------------------------------------")
    print("\n\n")


def main():
    files = get_file_names()
    files_names =[]
    figures_per_article = []
    for file in files:
        print("")
        f = {'input': open(file, 'rb')}
        response = requests.post('http://localhost:8070/api/processFulltextDocument', files=f)
        soup = BeautifulSoup(response.content, "xml")
        file_name=Path(file).stem
        files_names.append(file_name)
        plot_cloud(file_name, join_paragraphs(soup))
        figures_per_article.append(count_figures(soup))
        list_links(soup)
        
    plot_number_figures_per_articule(files_names, figures_per_article)

if __name__ == "__main__":
    main()
