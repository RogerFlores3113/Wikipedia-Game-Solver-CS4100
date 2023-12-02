from Scraper import get_wikipedia_links_with_similarity
import wikipediaapi
import heapq


def find_path_to_target(start_title: str, target_title: str, max_iters=15, initial_similarity_bound=-0.3):
    """
    Find a path from a start Wikipedia page to a target page using cosine similarity.
    """

    wiki_wiki = wikipediaapi.Wikipedia(user_agent="Wikipedia game solution grapher (flores.r@northeastern.edu)", language="en")
    target_page = wiki_wiki.page(target_title)
    if not target_page.exists():
        return None

    priority_queue = [(-1, start_title, [])]  # Max heap
    visited = set()
    fifth_highest_similarity = initial_similarity_bound
    final_path = []  # Variable to store the final path

    for iteration in range(max_iters):
        if not priority_queue:
            print("Priority queue is empty before reaching max iterations.")
            break

        _, current_title, path = heapq.heappop(priority_queue)
        if current_title in visited:
            continue
        visited.add(current_title)

        # Update the path
        current_path = path + [current_title]

        print(f"Iteration: {iteration}, Current page: {current_title}")  
        if current_title == target_title:
            return current_path
            break

        current_page = wiki_wiki.page(current_title)
        if target_title in current_page.links:
            return current_path + [target_title]
            break

        links_with_similarity = get_wikipedia_links_with_similarity(current_page, target_page)

        for link_title, (similarity, _) in links_with_similarity.items():
            if link_title not in visited and -similarity > fifth_highest_similarity:
                new_path = current_path + [link_title]
                heapq.heappush(priority_queue, (-similarity, link_title, new_path))

        # Update the minimum similarity threshold
        if len(priority_queue) > :
            priority_queue = heapq.nlargest(5, priority_queue)
            heapq.heapify(priority_queue)
            fifth_highest_similarity = -priority_queue[-1][0]

    return current_path


 


if (__name__ == "__main__"):

    paths = find_path_to_target("Industrial Era", "Fruit")
    print("returned path:")
    for i, p in enumerate(paths):
        print(f"step {i}, page: {p}")
