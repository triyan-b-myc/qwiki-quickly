import json
from functools import cmp_to_key
import locale

def load_tree():
    with open("data/qwiki.json", encoding="utf8") as f:
        data = json.load(f)
        return convert_to_tree(data)
    

def convert_to_tree(graph):
    root_url = next(iter(graph.keys()))
    visited = set()

    def sort_cmp(a, b):
        if (len(a["children"]) == 0) ^ (len(b["children"]) == 0): # If only one has children
            return 1 if len(a["children"]) == 0 else -1
        return locale.strcoll(a["title"], b["title"])

    def _convert_to_tree(url):
        if url in visited or url not in graph:
            return None
        visited.add(url)
        children = list(
            filter(
                lambda n: n is not None, 
                (_convert_to_tree(child) for child in graph[url].get("children", []))
            )
        )
        children.sort(key=cmp_to_key(sort_cmp))

        return {
            "title": graph[url]["title"],
            "url": url,
            "expanded": url == root_url,
            "children": children
        }
    
    return _convert_to_tree(root_url)


def filter_tree(tree, q):
    filtered = []

    for node in tree:
        filtered_children = filter_tree(node.get("children", []), q)

        if q.lower() in node["title"].lower() or q.lower() in node["title"].lower() or filtered_children:
            filtered.append({
                "title": node["title"],
                "url": node["url"],
                "expanded": True,
                "children": filtered_children
            })
    return filtered