import matplotlib.pyplot as plt
import numpy as np
import pickle
# Sample data
approaches = ['No Epsilon WordVec', 'Epsilon WordVec', 'TFIDF Vectorizer', 'Combo Agent']  # Replace with your approach names
num_runs = 100
file_path = 'no_greedy_DLS.pkl'

# Loading the data from the pickle file
with open(file_path, 'rb') as file:
    loaded_data = pickle.load(file)

with open('greedy_DLS.pkl', 'rb') as file1:
    tfidf_data = pickle.load(file1)


with open('combo_agent.pkl', 'rb') as file2:
    combo_agent = pickle.load(file2)

time_taken_data, path_data, priority_queue_data, accuracy_data = loaded_data
print(type(loaded_data))
tfidf_time, tfidf_path_data, tfidf_priority_queue, tfidf_accuracy_data = tfidf_data

total_data = [time_taken_data, path_data]
print(total_data[0][0])
print(total_data[1][0])


print("path size DLS: " + str(np.mean(list(map(lambda x: len(x), path_data)))))
print("path size Combo: " + str(np.mean(list(map(lambda x: len(x), tfidf_path_data)))))


plotted_data = [[time_taken_data, priority_queue_data, accuracy_data], [tfidf_time, tfidf_priority_queue, tfidf_accuracy_data]]

# Plotting histograms
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

for i, metric in enumerate(['Time Taken(Seconds)', 'Priority Queue Size', 'Accuracy']):
    axes[i].bar(np.arange(len(approaches)), [np.mean(plotted_data[0][i]), np.mean(plotted_data[1][i])],
            width=0.5, label=metric, align='center', color=['blue', 'orange'])


    axes[i].set_xticks(np.arange(len(approaches)))
    axes[i].set_xticklabels(approaches)
    axes[i].set_ylabel(metric)

# Adding legend outside the loop

plt.tight_layout()
plt.show()
