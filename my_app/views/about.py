import streamlit as st
import os

def show_about_page():
    st.markdown(
        """
        <h1 style='text-align:center;'>GROUP 5 - Machine Problem #3</h1>
        <h3 style='text-align:center;'>Implementation of Decrease and Conquer Algorithms</h3>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()

    st.markdown("## Meet the Team")

    # Get the directory of this script file
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build absolute paths for local images
    local_image_path = os.path.join(base_dir, "..", "static", "images", "jen.jpg")
    local_image_path = os.path.normpath(local_image_path)

    image_paths = [
        local_image_path,
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",
        "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ=",

    ]

    names = [
        "Jen Patrick Nataba",
        "Member 2",
        "Member 3",
        "Member 4",
        "Member 5",
        "Member 6",
        "Member 7",
        "Member 8",
        "Member 9"
    ]

    def display_row(start, end):
        cols = st.columns(end - start)
        for col, img_path, name in zip(cols, image_paths[start:end], names[start:end]):
            with col:
                st.image(img_path, use_container_width=True)
                st.write(f"**{name}**")

    display_row(0, 5)
    display_row(5, 9)

    st.divider()

    st.markdown(
        """
            <h2>
            This project showcases the implementation of three decrease and conquer algorithms (Insertion Sort, Binaray Search, and Russian Multiplication Method).
            This was made possible using Streamlit and python 3.12.
            </h2>
            <h3>
            <ul style='display: inline-block; text-align: left;'>
                <li><b>Insertion Sort</b>: Learn how insertion sort works step by step</li>
                <li><b>Binary Search</b>: Understand the binary search algorithm</li>
                <li><b>Russian Multiplication Method</b>: Explore the RMM algorithm implementation</li>
            </ul>
            </h3>
        """,
        unsafe_allow_html=True
    )
