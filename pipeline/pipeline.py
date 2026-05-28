import sys
import pandas as pd

print(f"Arguments: {sys.argv}")

month = sys.argv[1] if len(sys.argv) > 1 else "unknown" 

print(f"Hello, Pipeline! Month: {month}")

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(f"DataFrame:\n{df}")

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")