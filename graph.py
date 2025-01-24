import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_graph(path, attribute, output ):
    data = pd.read_csv(path, sep = ';')
    row = data[(data['method'] == 'mondrian') & (data['protected_attribute'] == attribute)]
    row2 = data[(data['method'] == 'modified_mondrian') & (data['protected_attribute'] == attribute)]
    metrics = ['accuracy', 'f1', 'dp', 'spd', 'eod']
    for metric in metrics:
        y_label = attribute + '_' + metric
        y = row[metric].values
        y2 = row2[metric].values
        x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
        x_even = np.linspace(1, len(x), len(x))
# Create a figure and an axis
        fig, ax = plt.subplots()

# Plot data
        ax.plot(x_even, y, label='Line with Dots', marker='o', linestyle='--')
        ax.plot(x_even, y2, label='Line 2', marker='x', linestyle=':')

# Add a title and labels
        ax.set_title('Simple Line Graph')
        ax.set_xticks(x_even)
        ax.set_xticklabels(x)
        ax.set_xlabel('K Value')
        ax.set_ylabel(y_label)

# Add a legend
        ax.legend()
        write_to = output + '_' + attribute + '_' + metric + '.png'
# Save the figure
        fig.savefig(write_to)