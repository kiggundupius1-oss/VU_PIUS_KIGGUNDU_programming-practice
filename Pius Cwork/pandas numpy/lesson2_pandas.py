import pandas as pd
data = {
    "Name": ["Pius", "Mary", "Dorothy", "Cathy"],
    "Age":[28, 24, 19, 23],
    "Marks":[75, 84, 78, 95]
}
df = pd.DataFrame(data)
print(df)
print(f"Average mark (mean): {df['Marks'].mean():.2f}")
print(f"Highest mark: {df['Marks'].max()}")
print(f"Lowest mark: {df['Marks'].min()}")