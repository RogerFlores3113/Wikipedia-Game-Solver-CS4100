import random
from WordVecWrapper import find_path_to_target
import time
import pickle
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import wikipediaapi
def calc_page_similarity(page_1_text, page_2_text):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the text data
    tfidf_matrix = vectorizer.fit_transform([page_1_text, page_2_text])

    # Calculate the cosine similarity between the two text vectors
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    return similarity

def get_page_text(page_title):
        wiki_wiki = wikipediaapi.Wikipedia(user_agent="Wikipedia game solution grapher (lu.kev@northeastern.edu)",language="en")
        page = wiki_wiki.page(page_title)
        if not page.exists():
            return {"Error": "Page does not exist"}
        
        return page.text
#Mask to run wrappers with different parameters
def run_search_program(word_bag, num_runs):
    start_time = time.time()
    times = []
    priority_queue_sizes = []
    paths = []
    results = []
    print("--- %s seconds ---" % (time.time() - start_time))
    for i in range(num_runs):
        words = random.sample(word_bag, 2)
        for item in words:
            word_bag.remove(item)
        priority_queue, path = find_path_to_target(words[0], words[1])
        runtime = time.time() - start_time
        final_word = path[-1]
        similarity = calc_page_similarity(get_page_text(words[1]), get_page_text(final_word))
        start_time = time.time()
        times.append(runtime)
        paths.append(path)
        priority_queue_sizes.append(priority_queue)
        results.append(similarity)
        # Save variables to a file using pickle.dump
    with open('my_variables.pkl', 'wb') as file:
        pickle.dump((times, paths, priority_queue, results), file)
        print(paths)
        print(results)

#Creates bag of words
def get_words(file_path):
    # Specify the path to your text file

    # Read the titles from the text file into a list
    with open(file_path, 'r') as file:
        titles_list = [line.strip() for line in file]
    return titles_list

if (__name__ == "__main__"):
    file_path = 'wikipedia_articles.txt'
    word_bag = get_words(file_path)
    run_search_program(word_bag, 5)


    
    