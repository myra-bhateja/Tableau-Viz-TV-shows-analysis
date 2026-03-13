import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/tv_series_cleaned.csv')

engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/tvshows'
)

df.to_sql('tv_series', engine, if_exists='replace', index=False)
print("Done! Rows:", len(df))