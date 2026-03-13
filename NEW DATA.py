import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# ── 1. READ ───────────────────────────────────────────
df = pd.read_csv(r'c:\Users\myrab\OneDrive\Desktop\TV Show Analysis\data\TV Series.csv', encoding='latin-1')
print("Raw rows:", len(df))

# ── 2. CLEAN ──────────────────────────────────────────
df.replace('****', np.nan, inplace=True)
df['Runtime'] = df['Runtime'].str.extract(r'(\d+)').astype(float)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Start Year'] = df['Release Year'].str.extract(r'(\d{4})').astype(float)
df['Primary Genre'] = df['Genre'].str.split(',').str[0].str.strip()
print("Cleaned rows:", len(df))

# ── 3. SAVE ───────────────────────────────────────────
df.to_csv(r'c:\Users\myrab\OneDrive\Desktop\TV Show Analysis\data\tv_series_cleaned.csv', index=False)
print("CSV saved!")

# ── 4. LOAD TO POSTGRESQL ─────────────────────────────
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/tvshows'
)
df.to_sql('tv_series', engine, if_exists='replace', index=False)
print("Loaded! Rows:", len(df))