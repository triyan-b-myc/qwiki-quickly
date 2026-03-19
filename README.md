# Qwiki Quickly

A fast and intuitive search interface for browsing the myclimate Qwiki knowledge base. Qwiki Quickly presents hierarchical documentation in an expandable tree structure with powerful search capabilities.

## Features

- **Hierarchical Navigation**: Browse the Qwiki knowledge base as an expandable tree structure
- **Fast Search**: Filter the entire knowledge tree in real-time with minimum 3 character queries
- **Smart Sorting**: Results are automatically sorted with folders first, then alphabetically by title
- **Direct Links**: Quick access to documentation with clickable links to individual pages
- **Responsive Design**: Built with Streamlit for a clean, responsive web interface

## Requirements

- Python 3.8+
- Streamlit

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd qwiki-quickly
```

2. Install dependencies:
```bash
pip install streamlit
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

### How to Use

1. **Browse**: On initial load, the tree view shows the complete knowledge base hierarchy
2. **Search**: Type at least 3 characters in the search box to filter results
3. **Expand**: Click on folders (indicated by 📁) to expand/collapse sections
4. **Navigate**: Click on links (indicated by 🔗) to access the documentation pages

## Project Structure

```
qwiki-quickly/
├── app.py                 # Main Streamlit application
├── core/
│   ├── __init__.py
│   └── utils.py          # Tree conversion and filtering utilities
├── data/
│   └── qwiki.json        # Knowledge base data in graph format
├── assets/
│   └── logo.png          # myclimate logo
└── README.md             # This file
```

## Data Format

The application loads knowledge base data from `data/qwiki.json`, which contains:
- **graph**: Mapping of page URLs to their child page URLs
- **attr**: Page attributes including titles for each URL

The utility functions convert this graph representation into a hierarchical tree structure for display.

## How It Works

### Tree Conversion (`convert_to_tree`)
- Traverses the graph starting from the root URL
- Builds a tree structure with parent-child relationships
- Sorts children by: folders first, then alphabetically by title
- Tracks visited nodes to prevent cycles

### Search Filtering (`filter_tree`)
- Recursively filters the tree based on query string
- Returns nodes where the title matches the query OR contain matching children
- Expands all nodes in search results for visibility

## Features in Detail

### Smart Sorting
- **Folders first**: Pages with children appear above leaf pages
- **Alphabetical**: Within each category, pages are sorted alphabetically by title
- **Locale-aware**: Uses system locale for proper character sorting

### Search Behavior
- Requires minimum 3 characters for search activation
- Case-insensitive matching
- Preserves tree structure while filtering
- Automatically expands matching branches

## Development

### Key Functions

**`load_tree()`**
- Loads the JSON data from `data/qwiki.json`
- Returns the converted tree structure

**`convert_to_tree(data)`**
- Converts graph format to tree structure
- Takes data with "graph" and "attr" keys
- Returns hierarchical tree with expanded/collapsed states

**`filter_tree(tree, q)`**
- Filters tree based on query string
- Returns filtered nodes with matching content or children
- Expands all matching branches

**`render_tree(tree, parents, d)`**
- Renders the tree structure in Streamlit
- Shows breadcrumb navigation
- Handles expandable folders and links
