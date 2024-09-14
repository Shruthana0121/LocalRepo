import pandas as pd
import re
file_path = 'fictional_richest_people.xlsx'
df = pd.read_excel(file_path, sheet_name='fictional_richest_people')
df['Net Worth Cleaned'] = pd.to_numeric(df['Net Worth'].apply(lambda x: re.sub(r'[^\d.]', '', str(x))), errors='coerce')
df.dropna(subset=['Net Worth Cleaned'], inplace=True)
df_sorted = df.sort_values('Net Worth Cleaned', ascending=False)
third_richest = df_sorted.iloc[2]
richest_person = df.loc[df['Net Worth Cleaned'].idxmax()]
no_email_count = df['Email'].isna().sum()
no_phone_count = df['Phone Number'].isna().sum()
sum_net_worth = df['Net Worth Cleaned'].sum()
total_net_worth = df['Net Worth Cleaned'].sum()

print(f"The richest person is {richest_person['Name']} with a net worth of ${richest_person['Net Worth Cleaned']}billion .")
print(f"Number of people without an email: {no_email_count}")
print(f"Number of people without a phone number: {no_phone_count}")
print(f"Total net worth of all individuals: ${total_net_worth:.2f} billion")
print(f"The third richest person is {third_richest['Name']} with a net worth of ${third_richest['Net Worth Cleaned']:.2f} billion")
