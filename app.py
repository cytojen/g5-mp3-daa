import streamlit as st
import importlib.util
import os

# Set base directory (G5-MP2-DAA)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to views inside src/
VIEWS_DIR = os.path.join(BASE_DIR, "src", "views")

# Page configuration dictionary
PAGES = {
    "home_page": {"label": "Home"},
    "about_page": {"label": "About"},
    "insertion_page": {"label": "Insertion Sort"},
    "binary_search_page": {"label": "Binary Search"},
    "rmm_page": {"label": "Russian Multiplication"},
    "video_page": {"label": "Video Demo"}   
}

def main():
    st.set_page_config(page_title="Group 5 - Machine Problem #3", page_icon="🟩", layout="wide")

    # Initialize default page
    if "page" not in st.session_state:
        st.session_state.page = "home_page"

    # Show navbar
    create_navbar()

    # Load selected module dynamically
    page_name = st.session_state.page
    module_path = os.path.join(VIEWS_DIR, f"{page_name}.py")

    spec = importlib.util.spec_from_file_location(page_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Call the correct show_*_page() function
    getattr(module, f"{page_name}")()

def create_navbar():
    """Nav bar for home, about, insertion, binary, and rmm"""
    cols = st.columns(len(PAGES))
    for col, (key, page) in zip(cols, PAGES.items()):
        with col:
            if st.button(page["label"], use_container_width=True):
                st.session_state.page = key
    st.divider()

if __name__ == "__main__":
    main()
