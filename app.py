import streamlit as st
import importlib.util
import os

# Set base directory (G5-MP2-DAA)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to views inside my_app/
VIEWS_DIR = os.path.join(BASE_DIR, "my_app", "views")

# Page configuration dictionary
PAGES = {
    "about": {"label": "About"},
    "insertion_sort": {"label": "Insertion Sort"},
    "binary_search": {"label": "Binary Search"},
    "rmm": {"label": "RMM"}
}

def main():
    st.set_page_config(page_title="Group 5 - Machine Problem #3", page_icon="🟩", layout="wide")

    # Initialize default page
    if "page" not in st.session_state:
        st.session_state.page = "about"

    # Show navbar
    create_navbar()

    # Load selected module dynamically
    page_name = st.session_state.page
    module_path = os.path.join(VIEWS_DIR, f"{page_name}.py")

    spec = importlib.util.spec_from_file_location(page_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Call the correct show_*_page() function
    getattr(module, f"show_{page_name}_page")()

def create_navbar():
    cols = st.columns(len(PAGES))
    for col, (key, page) in zip(cols, PAGES.items()):
        with col:
            if st.button(page["label"], use_container_width=True):
                st.session_state.page = key
    st.divider()

if __name__ == "__main__":
    main()
