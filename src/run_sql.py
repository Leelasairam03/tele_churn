import pandas as pd
from config import engine

with open("sql/queries.sql") as f:
    queries = [q.strip() for q in f.read().split(";") if q.strip()]

for i, query in enumerate(queries, 1):
    print(f"\n--- Query {i} ---")
    print(pd.read_sql(query, engine).to_string(index=False))