import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import glob

def get_file_names():
    file_list = glob.glob("./xmls/*.xml")
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
    # plt.savefig("wordcloud-"+file+".png")
    plt.axis("off")
    plt.show()
    plt.close()

def count_figures(soup):
    figures = soup.find_all("figure")
    return len(figures)
    
def plot_number_figures_per_articule(files, figures_per_article):
    plt.bar(files, figures_per_article)
    plt.show()

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
    figures_per_article = []
    for file in files:
        
        with open(file) as f:
            soup = BeautifulSoup(f, "xml")
        
        plot_cloud(file, join_paragraphs(soup))
        figures_per_article.append(count_figures(soup))
        list_links(soup)
        
    plot_number_figures_per_articule(files, figures_per_article)

if __name__ == "__main__":
    main()
