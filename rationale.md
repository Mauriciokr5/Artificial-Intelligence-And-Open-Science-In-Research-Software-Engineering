# Explanation
<br></br>
***
### Task: Draw a keyword cloud based on the abstract information

I join all texts in p tags into unique_string and then use it in the following function to create a word cloud from the most frequent words in it.
```
WordCloud(width = 1000, height = 500).generate(unique_string)
```
After that, just plot with the matplotlib library.
<br></br>
***
### Task: Create a visualization showing the number of figures per article.

I used BeautifulSoup (soup) to find all figure tags, this returns a list and I get the length of it.
```
def count_figures(soup):
    figures = soup.find_all("figure")
    return len(figures)
```
The, I save those numbers in an array to plot them with the respective file name on a bar chart.
```
def plot_number_figures_per_articule(files, figures_per_article):
    plt.bar(files, figures_per_article)
    plt.show()
```
<br></br>


***
### Task: Create a list of the links found in each paper

The same as figures task, I search all ptr tags and print target atribute that contains the URL.
```
def list_links(soup):
    links = soup.find_all("ptr")
    print("----------------------------------------------------------------")
    print(soup.title.text)
    print("----------------------------------------------------------------")
    for link in links:
        print(link['target'])
    print("----------------------------------------------------------------")
    print("\n\n")
```
<br></br>
***
