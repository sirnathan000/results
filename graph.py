import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np
from numpy.ma.core import minimum


def create_graph_combined(path, output ):
    #had to make minor changes so that combined was also processed as it doesn't have the protected_attribute (as again it is combined)
    data = pd.read_csv(path, sep = ';')
    row = data[(data['method'] == 'mondrian')]
    row2 = data[(data['method'] == 'modified_mondrian')]
    row3 = data[(data['method'] == 'original')]
    metrics = ['accuracy', 'f1', 'dp', 'spd', 'eod']
    metrics_complete = {
        'accuracy': 'Accuracy',
        'f1' : 'F1-score',
        'dp' : 'Disparate Impact',
        'spd' : 'Statistical Parity Difference',
        'eod' : 'Equal Opportunity Difference'
    }
    perfect_metrics = {
        'accuracy': 1.0,
        'f1': 1.0,
        'dp': 1.0,
        'spd': 0.0,
        'eod': 0.0
    }
    #creation of the graphs on a per metric basis.
    for metric in metrics:
        y = row[metric].values
        y2 = row2[metric].values
        y3 = row3[metric].values
        perfect = perfect_metrics.get(metric, 0)
        x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
        x_even = np.linspace(1, len(x), len(x))
        fig, ax = plt.subplots()

# Plot data
        ax.plot(x_even, y, color='blue', label='Mondrian', marker='o', linestyle='--')
        ax.plot(x_even, y2, color='green', label='Modified Mondrian', marker='x', linestyle='-.')
        ax.axhline(y=y3, color='black', label='Original data', marker='d', linestyle='-.')
        ax.axhline(y=perfect, color='red', linestyle=':', label='Perfect')

# All info for graphs
        title = metrics_complete[metric]
        ax.set_title(title)
        ax.legend()

#all mods for x
        ax.set_xticks(x_even)
        ax.set_xticklabels(x)
        ax.set_xlabel('K Value')
#        ax.set_xlim(left=0)

#all mods for y
        y_label = metrics_complete[metric]
        ax.set_ylabel(y_label)
        ax.yaxis.set_major_locator(MultipleLocator(0.1))
        ax.set_ylim(bottom=0.0)
        if min(y.min(), y2.min()) >= 0.0:
            ax.set_ylim(bottom=-0.1)
        else:
            minimum = min(y.min(), y2.min())
            if minimum < 0:
                minimum = minimum - 0.1
                ax.set_ylim(bottom=minimum)
        if max(y.max(), y2.max()) <= 1:
            ax.set_ylim(top=1.1)

        else:
            maximum = max(y.max(), y2.max()) + 0.1
            ax.set_ylim(top=maximum)


# Save the figure
        write_to = output + '_' + metric + '.png'
        fig.savefig(write_to)

def create_graph(path, attributes, output ):
    for attribute in attributes:
        data = pd.read_csv(path, sep = ';')
        row = data[(data['method'] == 'mondrian') & (data['protected_attribute'] == attribute)]
        row2 = data[(data['method'] == 'modified_mondrian') & (data['protected_attribute'] == attribute)]
        row3 = data[(data['method'] == 'original') & (data['protected_attribute'] == attribute)]
        metrics = ['accuracy', 'f1', 'dp', 'spd', 'eod']
        metrics_complete = {
            'accuracy': 'Accuracy',
            'f1': 'F1-score',
            'dp': 'Disparate Impact',
            'spd': 'Statistical Parity Difference',
            'eod': 'Equal Opportunity Difference'
        }
        perfect_metrics = {
            'accuracy': 1.0,
            'f1': 1.0,
            'dp': 1.0,
            'spd': 0.0,
            'eod': 0.0
        }
        #creation of the graphs on a per metric basis.
        for metric in metrics:
            y_label = attribute + '_' + metric
            y = row[metric].values
            y2 = row2[metric].values
            y3 = row3[metric].values
            perfect = perfect_metrics.get(metric, 0)
            x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
            x_even = np.linspace(1, len(x), len(x))
            fig, ax = plt.subplots()

# Plot data
            ax.plot(x_even, y, color='blue', label='Mondrian', marker='o', linestyle='--')
            ax.plot(x_even, y2, color='green', label='Modified Mondrian', marker='x', linestyle='-.')
            ax.axhline(y=y3, color='black', label='Original data', marker='d', linestyle='-.')
            ax.axhline(y=perfect, color='red', linestyle=':', label='Perfect')

# All info for graphs
            title = metrics_complete[metric]
            ax.set_title(title)
            ax.legend()

#all mods for x
            y_label = metrics_complete[metric]
            ax.set_xticks(x_even)
            ax.set_xticklabels(x)
            ax.set_xlabel('K Value')
#           ax.set_xlim(left=0)

#all mods for y
            ax.set_ylabel(y_label)
            ax.yaxis.set_major_locator(MultipleLocator(0.1))
            ax.set_ylim(bottom=-0.1)
            if min(np.nanmin(y), np.nanmin(y2)) >= 0.0:
                ax.set_ylim(bottom=-0.1)
            else:
                minimum = min(np.nanmin(y), np.nanmin(y2))
                if minimum < 0.0 :
                    minimum = minimum - 0.1
                    ax.set_ylim(bottom=minimum)
            if max(np.nanmax(y), np.nanmax(y2)) <= 1.0:
                ax.set_ylim(top=1.1)
            else:
                maximum = max(np.nanmax(y), np.nanmax(y2)) + 0.1
                ax.set_ylim(top=maximum)

# Save the figure
            write_to = output + '_' + attribute + '_' + metric + '.png'
            fig.savefig(write_to)


'''
#old setup
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
'''

create_graph_combined('Experiment_runs/results_folkstable_runs.csv', 'graphs_experiment/results_folkstable_allQI_runs')
create_graph_combined('Experiment_runs/results_student_runs.csv', 'graphs_experiment/results_student_allQI_runs')