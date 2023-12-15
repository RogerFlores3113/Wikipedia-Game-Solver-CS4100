import matplotlib.pyplot as plt
import numpy as np
import pickle
# Loading the data from the pickle file
with open("no_greedy_DLS.pkl", 'rb') as file:
    loaded_data = pickle.load(file)

with open('my_tfidf.pkl', 'rb') as file1:
    tfidf_data = pickle.load(file1)

time_taken_data, path_data, priority_queue_data, accuracy_data = loaded_data

tfidf_time, tfidf_path, tfidf_accuracy_data = tfidf_data


data = [loaded_data, tfidf_data]
print(data[1][0])