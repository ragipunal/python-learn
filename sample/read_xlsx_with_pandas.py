import datetime

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

# df = pd.read_excel("sales_data.xlsx")
# display(df)

# df = pd.read_excel("sales_data.xlsx", nrows=5)
# display(df)

#df = pd.read_excel("sales_data.xlsx", skiprows=5)
#display(df)


# df = pd.read_excel("sales_data.xlsx", skiprows=[1,4,7,10])
# display(df)

# df = pd.read_excel("sales_data.xlsx", usecols='A:C,G')
# display(df)

# df = pd.read_excel("sales_data.xlsx", usecols=['OrderDate', 'Region', 'Rep', 'Total'])
# display(df)

# df = pd.read_excel("sales_data.xlsx", usecols=[0,1,2,6])
# display(df)

#df = pd.read_excel("sales_data.xlsx", sheet_name='2021')
#display(df)

all_sheets = pd.read_excel("sales_data.xlsx", sheet_name=None)
print(type(all_sheets))

for key, value in all_sheets.items():
    print(key, type(value))


#for key, value in all_sheets.items():
#    print(key)
#    display(value)

combined_df = pd.concat(all_sheets.values(), ignore_index=True)
#display(combined_df)

ragip = pd.DataFrame(
    {
        'OrderDate': datetime.datetime.today(),
        'Region': 'East',
        'Rep': 'Ragıp',
        'Item': 'Mask',
        'Units': 1000,
        'Unit Cost': float(4.99),
        'Total': float(125.06),
        'Shipped': True,
    }, index=[0]
)
combined_df_two = pd.concat([combined_df, ragip], ignore_index=True)
dropped_df = combined_df_two.drop(index=[21])
dropped_df = dropped_df.rename(columns={'OrderDate': 'Sipariş Tarihi'})

display(dropped_df)

total_sales_amount = dropped_df.groupby('Rep').Total.sum()
total_sales_amount.plot.bar(figsize=(10,6))

plt.show()