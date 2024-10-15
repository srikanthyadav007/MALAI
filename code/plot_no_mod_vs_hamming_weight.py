import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/Varun Geddam/Desktop/LWE/verde/n0_mod_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Inspect the columns
print(df.columns)

# Assuming 'hwt' is the column name for Hamming weights and other columns are the data
# Set the correct column name as the index (replace 'hwt' with the actual column name if different)
df.set_index('hwt', inplace=True)

# Define the interval for sampling
interval = 5 # Change this to the desired interval

# Filter the DataFrame to take values at the specified interval
df_filtered = df[df.index % interval == 0]

# Calculate the average for each row in the filtered DataFrame
df_filtered['average'] = df_filtered.mean(axis=1)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
x = df_filtered.index
y = df_filtered['average']

# Adjusting marker size and line style
ax.plot(x, y, marker='o', markersize=5, linestyle='-', linewidth=1, color='b')
ax.set_xlabel('Hamming weight', fontsize = 20)
ax.set_ylabel('Percentage(%) of noMod data', fontsize = 20)
#ax.set_title('Percentage of No Mod data vs Hamming weights', fontsize = 20)

# Smaller grid lines
ax.grid(which='both', linestyle='--', linewidth=0.3)

# Adding x-axis ticks at the interval
plt.xticks(np.arange(min(x), max(x)+interval, interval))

plt.show()
