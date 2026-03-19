import streamlit as st
from core import utils as ut

tree = ut.load_tree()
st.logo("assets/logo.png", size="large", link="https://www.myclimate.org")
st.set_page_config(
    layout="wide",
    page_title="Qwiki Quickly",
    page_icon=":material/search:"
)

st.title('Qwiki Quickly')
st.text_input("Search", help="Please enter at least 3 characters", width=300, key="query", icon=":material/search:")

node_counter = st.empty()
node_counter.info(" pages", icon="spinner", width=300)

def render_tree(tree, parents=None, d=1):
    if not isinstance(tree, list):
        tree = [tree]
    if parents is None: # Runs once, for root node
        if len(st.session_state.query) >= 3:
            tree = ut.filter_tree(tree, st.session_state.query) 
        parents = []

    node_count = 0
    for node in tree:
        title = node["title"]
        url = node["url"]
        has_children = len(node["children"]) > 0
        icon = ":material/folder:" if has_children else ":material/link:"
        path = parents + [node]
        if has_children:
            with st.expander(title, expanded=node["expanded"], icon=icon, key=url):
                st.caption(" -> ".join(f'[{n["title"]}]({n["url"]})' for n in path))
                node_count += 1 + render_tree(node["children"], path, d+1)
        else:
            st.markdown(f"{icon} [{title}]({url})")
            node_count += 1
    return node_count
    
node_count = render_tree(tree)
with node_counter:
    st.info(f"{node_count} pages", width=300)