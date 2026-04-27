import pandas as pd
df = pd.read_csv('continents_249.csv')
df2 = pd.read_csv('price_of_healthy_diet_clean.csv')

# Merge the two DataFrames on the 'country' column
merged_df = pd.merge(df, df2, on='country')
# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)

print(merged_df.head())