#Mask to run wrappers with different parameters

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
    print(word_bag)
    