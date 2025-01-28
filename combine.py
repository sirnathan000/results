import pandas as pd
import csv
import os

# List of file paths
file_paths = [
    'Experiment_runs/results_student_combined_avg_allQI_run_1.csv',
    'Experiment_runs/results_student_combined_avg_allQI_run_2.csv',
    'Experiment_runs/results_student_combined_avg_allQI_run_3.csv',
    'Experiment_runs/results_student_combined_avg_allQI_run_4.csv',
    'Experiment_runs/results_student_combined_avg_allQI_run_5.csv'
]

# Read and concatenate all CSV files
data = [pd.read_csv(file, sep=';') for file in file_paths]
combined_data = pd.concat(data)




# Function to calculate the average for a column based on method and K values
def calculate_average(method, k, column):
#    print(combined_data)
    filtered_data = combined_data[(combined_data['method'] == method) & (combined_data['k'] == int(k))]
#    print(method, k, column, filtered_data)
    return round(filtered_data[column].mean(),2)


headers = ['method','k', 'f1', 'accuracy', 'dp', 'spd', 'eod']
k_values = [ '0', '2', '3', '4', '5', '6', '7', '8', '9', '10', '25', '50', '75', '100']
methods = ['mondrian', 'modified_mondrian', 'original']
columns = ['f1', 'accuracy', 'dp', 'spd', 'eod']

#print(combined_data)
file_path = 'Experiment_runs/results_student_runs.csv'
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
for method in methods:
    for k in k_values:
#        print(combined_data)
        if any((combined_data['method'] == method) & (combined_data['k'] == int(k))):
            row = [method, k]
            for column_name in columns:
                value = calculate_average(method, k, column_name)
                row.append(value)
#                print(value)
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(row)