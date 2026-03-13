import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_csv(r'c:\Users\myrab\OneDrive\Desktop\TV Show Analysis\data\tv_series_cleaned.csv')

# Combine all synopsis text
text = ' '.join(df['Synopsis'].dropna().tolist())

# Custom stopwords — remove common words
stopwords = set(STOPWORDS)
stopwords.update(['one', 'two', 'new', 'set', 'also', 'get', 
                  'must', 'world', 'life', 'series', 'show'])

# Generate word cloud
wc = WordCloud(
    width=1200,
    height=600,
    background_color='white',
    stopwords=stopwords,
    max_words=100,
    colormap='viridis'
).generate(text)

# Save
plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig(r'c:\Users\myrab\OneDrive\Desktop\TV Show Analysis\data\synopsis_wordcloud.png', 
            dpi=150, bbox_inches='tight')
plt.show()
print("Word cloud saved!")