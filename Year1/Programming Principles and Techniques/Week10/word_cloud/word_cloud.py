import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def get_data():
    with open("sample_text.txt", 'r') as file:
        data = file.read()
        return data


def run():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(get_data())
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    run()