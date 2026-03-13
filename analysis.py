import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. LOAD ────────────────────────────────────────────
df = pd.read_csv('data/TV Series.csv', encoding='latin-1')
print("Shape:", df.shape)

# ── 2. CLEAN ───────────────────────────────────────────
df.replace('****', np.nan, inplace=True)
df['Runtime'] = df['Runtime'].str.extract(r'(\d+)').astype(float)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Start Year'] = df['Release Year'].str.extract(r'(\d{4})').astype(float)
df['Primary Genre'] = df['Genre'].str.split(',').str[0].str.strip()

print("Missing values:\n", df.isnull().sum())
print("Cleaned shape:", df.shape)

# ── 3. ANALYZE ─────────────────────────────────────────
print("\nTop 10 rated shows:")
print(df[['Series Title','Rating','Primary Genre']]
    .dropna(subset=['Rating'])
    .sort_values('Rating', ascending=False)
    .head(10))

print("\nAvg rating by genre:")
print(df.groupby('Primary Genre')['Rating']
    .mean().sort_values(ascending=False).head(10))

# ── 4. VISUALIZE ───────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('TV Series Analysis', fontsize=18, fontweight='bold')

# Genre count
genre_counts = df['Primary Genre'].value_counts().head(10)
genre_counts.plot(kind='barh', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('Top 10 Genres by Show Count')

# Avg rating by genre
genre_ratings = df.groupby('Primary Genre')['Rating'].mean().sort_values(ascending=False).head(10)
genre_ratings.plot(kind='bar', ax=axes[0,1], color='coral')
axes[0,1].set_title('Avg Rating by Genre')
axes[0,1].tick_params(axis='x', rotation=45)

# Yearly trend
yearly = df[df['Start Year'] >= 2000].groupby('Start Year')['Series Title'].count()
axes[1,0].plot(yearly.index, yearly.values, marker='o', color='green')
axes[1,0].set_title('Shows Released per Year (2000+)')

# Rating distribution
df['Rating'].dropna().plot(kind='hist', bins=20, ax=axes[1,1], 
                            color='purple', edgecolor='white')
axes[1,1].set_title('Rating Distribution')

plt.tight_layout()
plt.savefig('data/analysis_charts.png', dpi=150)
plt.show()
print("Charts saved!")


