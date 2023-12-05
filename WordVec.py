from gensim.models import KeyedVectors
import gensim.downloader
import numpy as np
import re
# Load the pre-trained Word2Vec model
model_path = '/Users/KevinLu/Downloads/wikipedia/model.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
word_vector = model['dog_NOUN']

model_file_path = "model.bin"  # Specify the desired file path

wiki_vectors = KeyedVectors.load(model_file_path)
# Preprocess titles
def preprocess_title(title):
    title = title.lower()
    title = re.sub(r'[()]', '', title)
    tokens = title.split()
        
    return tokens

# Calculate title vectors
def calculate_title_vector(title, model):
    tokens = preprocess_title(title)
    vectors = [model[word] for word in tokens if word in model]
    
    if vectors:
        return sum(vectors) / len(vectors)
    else:
        return None

# Calculate cosine similarity between two title vectors
def calculate_similarity(vector1, vector2):
    if vector1 is not None and vector2 is not None:
        return vector1.dot(vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    else:
        return 0.0
    

vector1 = calculate_title_vector("(Apple)", wiki_vectors)
vector2 = calculate_title_vector("Apple", wiki_vectors)
print(calculate_similarity(vector1, vector2))

# print(wiki_vectors.most_similar('dog'))
# print(wiki_vectors.similarity('dog', 'hello'))
