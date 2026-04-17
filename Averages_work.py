import pandas as pd

df = pd.read_csv("data.csv")

df.head()

df.describe()

# Let's see what the average value is for everyone
df["value"].mean()

