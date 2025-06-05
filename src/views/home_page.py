import streamlit as st
import os

def home_page():
    """Home page content"""
    st.markdown(
        """
        <h1 style='text-align:center;'>GROUP 5 - Machine Problem #3</h1>
        <h3 style='text-align:center;'>Implementation of Decrease and Conquer Algorithms</h3>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.markdown("## Meet the Team")

    # Directory where local images are stored
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.normpath(os.path.join(base_dir, "..", "static", "images"))

    # List of image filenames
    image_filenames = [
        "jen.jpg",
        "princess.jpg",
        "luis.jpg",
        "shikina.jpg",
        "matan.jpg",
        "jyesh.png",
        "member7.png",
        "member8.jpg",
        "member9.jpeg"
    ]

    # Fallback image (if an image is missing)
    fallback_url = "https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ="

    # Construct image paths (check if file exists, else use fallback)
    image_paths = []
    for filename in image_filenames:
        full_path = os.path.join(image_dir, filename)
        if os.path.exists(full_path):
            image_paths.append(full_path)
        else:
            image_paths.append(fallback_url)

    # Names must match order of images
    names = [
        "Jen Patrick Nataba",
        "Princess Padauan",
        "Luis Miguel Dela Cruz",
        "Shikina Cabral",
        "Matan John Exconde",
        "Jyeshua Rey Velasco",
        "Member 7",
        "Member 8",
        "Member 9"
    ]

    def display_row(start, end):
        cols = st.columns(end - start)
        for col, img_path, name in zip(cols, image_paths[start:end], names[start:end]):
            with col:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<p style='text-align:center; font-weight:bold;'>{name}</p>", unsafe_allow_html=True)

    # Display members in rows of 5 and then remaining
    display_row(0, 5)

    # hindi ko mafix, ginawa ko na lang 10 displays para same sizes, pa-try nga itroubleshoot sa inspect element (change to 9)
    display_row(5, 10)

    st.divider()

    st.markdown(
        """
        <h2>
        This project showcases the implementation of three decrease and conquer algorithms (Insertion Sort, Binary Search, and Russian Multiplication Method).
        </h2>
        <h3>
        <ul style='display: inline-block; text-align: left;'>
            <li><b>Insertion Sort</b>: Show the state of the array at each pass</li>
            <li><b>Binary Search</b>: Understand the binary search algorithm</li>
            <li><b>Russian Multiplication Method</b>: Explore the RMM algorithm implementation</li>
        </ul>
        </h3>
        """,
        unsafe_allow_html=True
    )
