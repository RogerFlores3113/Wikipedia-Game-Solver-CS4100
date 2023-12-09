import matplotlib.pyplot as plt
import numpy as np

# Sample data
approaches = ['Approach 1', 'Approach 2', 'Approach 3']  # Replace with your approach names
num_runs = 100

# Sample data for time taken, size of priority queue, and accuracy for each approach
time_taken_data = np.random.rand(num_runs, 3) * 10  # Replace with your actual time taken data
priority_queue_data = np.random.randint(1, 100, size=(num_runs, 3))  # Replace with your actual priority queue size data
accuracy_data = np.random.rand(num_runs, 3)  # Replace with your actual accuracy data
 
# Min-Max scaling function
def min_max_scaling(data):
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    return (data - min_val) / (max_val - min_val)

time_taken_data = min_max_scaling(time_taken_data)
priority_queue_data = min_max_scaling(priority_queue_data)
accuracy_data = min_max_scaling(accuracy_data)

# Plotting histograms
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

for i, metric in enumerate(['Time Taken', 'Priority Queue Size', 'Accuracy']):
    axes[i].bar(np.arange(len(approaches)) - 0.2, np.mean(time_taken_data, axis=0),
                width=0.2, label='Time Taken', align='center')
    axes[i].bar(np.arange(len(approaches)), np.mean(priority_queue_data, axis=0),
                width=0.2, label='Priority Queue Size', align='center')
    axes[i].bar(np.arange(len(approaches)) + 0.2, np.mean(accuracy_data, axis=0),
                width=0.2, label='Accuracy', align='center')

    axes[i].set_xticks(np.arange(len(approaches)))
    axes[i].set_xticklabels(approaches)
    axes[i].set_ylabel(metric)

axes[0].legend()
plt.tight_layout()
plt.show()