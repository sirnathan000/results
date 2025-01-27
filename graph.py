import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_graph_combined(path, output ):
    #had to make minor changes so that combined was also processed as it doesn't have the protected_attribute (as again it is combined)
    data = pd.read_csv(path, sep = ';')
    row = data[(data['method'] == 'mondrian')]
    row2 = data[(data['method'] == 'modified_mondrian')]
    metrics = ['accuracy', 'f1', 'dp', 'spd', 'eod']
    #creation of the graphs on a per metric basis.
    for metric in metrics:
        y_label = metric
        y = row[metric].values
        y2 = row2[metric].values
        x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
        x_even = np.linspace(1, len(x), len(x))
        fig, ax = plt.subplots()

# Plot data
        ax.plot(x_even, y, label='Mondrian', marker='o', linestyle='--')
        ax.plot(x_even, y2, label='Modified Mondrian', marker='x', linestyle=':')

# Add a title and labels
        title = metric
        ax.set_title(title)
        ax.set_xticks(x_even)
        ax.set_xticklabels(x)
        ax.set_xlabel('K Value')
        ax.set_ylabel(y_label)
        ax.legend()
        write_to = output + '_' + metric + '.png'
# Save the figure
        fig.savefig(write_to)

def create_graph(path, attributes, output ):
    for attribute in attributes:
        data = pd.read_csv(path, sep = ';')
        row = data[(data['method'] == 'Mondrian') & (data['protected_attribute'] == attribute)]
        row2 = data[(data['method'] == 'Modified Mondrian') & (data['protected_attribute'] == attribute)]
        metrics = ['accuracy', 'f1', 'dp', 'spd', 'eod']
        #creation of the graphs on a per metric basis.
        for metric in metrics:
            y_label = attribute + '_' + metric
            y = row[metric].values
            y2 = row2[metric].values
            x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
            x_even = np.linspace(1, len(x), len(x))
            fig, ax = plt.subplots()

# Plot data
            ax.plot(x_even, y, label='Mondrian', marker='o', linestyle='--')
            ax.plot(x_even, y2, label='Modified Mondrian', marker='x', linestyle=':')

# Add a title and labels
            title = attribute+ ' ' + metric
            ax.set_title(title)
            ax.set_xticks(x_even)
            ax.set_xticklabels(x)
            ax.set_xlabel('K Value')
            ax.set_ylabel(y_label)
            ax.legend()
            write_to = output + '_' + attribute + '_' + metric + '.png'
# Save the figure
            fig.savefig(write_to)

create_graph('Processed/results_folkstable_combined.csv', ['SEX', 'RAC1P'], 'graphs_v2/results_folkstable_combined')
create_graph_combined('Processed/results_folkstable_combined_avg_allQI.csv', 'graphs_v2/results_folkstable_combined_avg_allQI')
create_graph_combined('Processed/results_folkstable_combined_avg_just_sex_rac1p.csv', 'graphs_v2/results_folkstable_combined_avg_just_sex_rac1p')
create_graph('Processed/results_folkstable_RAC1P_new.csv', ['SEX', 'RAC1P'], 'graphs_v2/results_folkstable_RAC1P_att_')
create_graph('Processed/results_folkstable_sex_new.csv', ['SEX', 'RAC1P'], 'graphs_v2/results_folkstable_SEX_att_')
create_graph('Processed/results_student_age_new.csv', ['sex', 'age'], 'graphs_v2/results_student_age_att_')
create_graph('Processed/results_student_sex_new.csv', ['sex', 'age'], 'graphs_v2/results_student_sex_att_')
create_graph('Processed/results_student_combined.csv', ['sex', 'age'], 'graphs_v2/results_student_combined_')
create_graph_combined('Processed/results_student_combined_avg_allQI.csv', 'graphs_v2/results_studentcombined_avg_allQI_')
create_graph_combined('Processed/results_student_combined_avg_just_sex_and_age.csv', 'graphs_v2/results_student_avg_just_sex_and_age_att')