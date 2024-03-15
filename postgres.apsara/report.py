
# to_install: pip3 install pandas,matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_data.csv' with the path to your actual CSV file
csv_file = 'tps.csv'

# Reading the CSV file
data = pd.read_csv(csv_file)

# Extracting threads and TPS values
threads = data['threads']
tps = data['tps']
# Finding the maximum TPS value and its corresponding thread count
max_tps = tps.max()
max_thread = threads[tps.idxmax()]

# Creating the bar chart
plt.figure(figsize=(10, 6))
# plt.bar(threads, tps, color='skyblue')
plt.plot(threads, tps, marker='o', linestyle='-', color='skyblue')  # Line graph



plt.xlabel('Number of Threads')
plt.ylabel('Transactions Per Second (TPS)')
plt.title('TPS by Number of Threads')
plt.xticks(threads)


# Annotating the maximum value
plt.annotate(f'Max TPS: {max_tps} @ {max_thread} TPS',  # Text to display
             (max_thread, max_tps),  # Point to annotate
             textcoords="offset points",  # Positioning the text
             xytext=(0,10),  # Distance from the text to the point
             ha='center',  # Center the text horizontally
             arrowprops=dict(arrowstyle="->", color='black'))  # Arrow pointing to the point


# Save the figure or display it
plt.savefig('tps_graph.png')  # Save the graph as an image file
#plt.show()  # Use this instead if you want to display the graph interactivel