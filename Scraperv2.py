import requests
import re

def get_wikipedia_links(input_data):
    if input_data.startswith("https://") or input_data.startswith("http://"):
        match = re.search(r"/wiki/(.+)", input_data)
        if match:
            page_title = match.group(1).replace("_", " ")
        else:
            return {"Error": "Invalid Wikipedia URL"}
    else:
        page_title = input_data

    ENDPOINT = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "links",
        "pllimit": "max"
    }

    try:
        response = requests.get(ENDPOINT, params=params)
        data = response.json()

        if 'error' in data:
            return {"Error": "Page does not exist"}


        links = {}
        for link in data['parse']['links']:
            if link.get('ns') == 0 and 'exists' in link:
                link_title = link['*']
                link_url = "https://en.wikipedia.org/wiki/" + link_title.replace(' ', '_')
                links[link_title] = link_url

        return links
    except Exception as e:
        return {"error occured": str(e)}


# Test case
input_data = "https://en.wikipedia.org/wiki/2005_Azores_subtropical_storm"
links = get_wikipedia_links(input_data)
print(links)
