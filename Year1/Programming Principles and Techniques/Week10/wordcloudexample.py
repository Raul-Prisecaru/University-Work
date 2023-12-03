from wordcloud import WordCloud
import matplotlib.pyplot as plt
data = ("This is some text. This text has repeated words. Text is cool.")

wc = WordCloud().generate(text=data)

plt.figure(figsize=(10, 5))
plt.imshow(wc)
plt.axis("off")
plt.show()