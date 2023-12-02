import wikipediaapi
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm











def get_wikipedia_links_with_similarity(input_data, reference_page : wikipediaapi.WikipediaPage):
    """
    Get Wikipedia page links with cosine similarity to a reference page.

    :param input_data: URL, title of the Wikipedia page, or WikipediaPage object
    :param reference_page: WikipediaPage object to compare with
    :return: Dictionary with link text as keys and a list [cosine_similarity, wikipedia_page] as values
    """
    wiki_wiki = wikipediaapi.Wikipedia(user_agent="Wikipedia game solution grapher (flores.r@northeastern.edu)",language="en")

    # Determine the type of input_data and get the page
    if isinstance(input_data, wikipediaapi.WikipediaPage):
        page = input_data
    else:
        if input_data.startswith("https://") or input_data.startswith("http://"):
            match = re.search(r"/wiki/(.+)", input_data)
            if match:
                page_title = match.group(1).replace("_", " ")
            else:
                return {"Error": "Invalid Wikipedia URL"}
        else:
            page_title = input_data

        page = wiki_wiki.page(page_title)
        if not page.exists():
            return {"Error": "Page does not exist"}

    # Collect all the pages, making the server requests. This is the most time-intensive part
    # it runs slightly above 12 requests per second
    texts = [reference_page.text]
    offshoot_pages = []
    valid_links = [l for l in page.links.values() if l.namespace == 0 and l.exists]
    for link in tqdm(valid_links, desc="Collecting links..."):
        offshoot_page = wiki_wiki.page(link.title)
        texts.append(offshoot_page.text)
        offshoot_pages.append(offshoot_page)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Calculate cosine similarities
    similarities = {}
    ref_vector = tfidf_matrix[0]
    for i, offshoot_page in enumerate(tqdm(offshoot_pages, desc="calculating cosine similarities..."), start=1):
        similarity = cosine_similarity(ref_vector, tfidf_matrix[i])[0][0]
        similarities[offshoot_page.title] = [similarity, offshoot_page]

    return similarities


vectorizer = TfidfVectorizer()

def text_to_tfidf(text):
    tfidf_vector = vectorizer.fit_transform([text])
    return tfidf_vector



def calculate_cosine_similarity(tfidf_vector1, tfidf_vector2):
    similarity = cosine_similarity(tfidf_vector1, tfidf_vector2)
    return similarity[0][0]




# Test case
if (__name__ == "__main__"):
    w = wikipediaapi.Wikipedia(user_agent="Wikipedia game solution grapher (flores.r@northeastern.edu)",language="en")
    target = w.page("Storm")
    links = get_wikipedia_links_with_similarity("2005_Azores_subtropical_storm", target)
    print(links)
