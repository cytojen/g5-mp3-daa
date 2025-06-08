import streamlit as st
from PIL import Image
import os

# Path to images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "static", "images"))

def about_page():
    """About the Algorithms"""

    st.title("About the Algorithms")
    st.subheader("Learn the people who were behind the three core algorithms in this project: Insertion Sort, Binary Search, and the Russian Peasant Multiplication Method.")

    st.divider()
    
    # Insertion Sort Section
    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("Insertion Sort")
            st.markdown("""
                <div style='font-size:24px; text-align: justify;'>
                Insertion sort is a straightforward sorting method that sorts an unsorted list by progressively placing each element into its appropriate position within a sorted section of the list. It constructs the completed sorted array one element at a time.<br><br>

                The origin of insertion sort is hard to determine since it existed before computing. However, its first use in a computation context traces back to 1945 when Konrad Zuse defined it as a primitive for the first high-level programming language, Plankalkül.
                </div>
            """, unsafe_allow_html=True)

        with col2:
            image_path = os.path.join(IMAGE_DIR, "konrad.jpg")
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = Image.open(image_path).resize((604, 400))
                st.image(image, use_container_width=True)
                st.markdown(
                    "<p style='text-align:center; font-size:16px;'>"
                    "<a href='https://www.google.com/url?sa=i&url=https%3A%2F%2Finterestingengineering.com%2Fengineers-directory%2Fkonrad-zuse&psig=AOvVaw1iG5TM4IpjCaqPdKlELBkF&ust=1749461071074000&source=images&cd=vfe&opi=89978449&ved=0CAMQjB1qFwoTCMC0hL_A4Y0DFQAAAAAdAAAAABAE' target='_blank' style='text-decoration: none;'>Konrad Zuse - Learn More</a>"
                    "</p>",
                    unsafe_allow_html=True)

    st.divider()

    # Binary Search Section
    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("Binary Search")
            st.markdown("""
                <div style='font-size:24px; text-align: justify;'>
                Binary search is an extremely effective algorithm for locating a specific element within a sorted array or list. It operates by continuously halving the search interval.<br><br>

                The first time binary search was described as an algorithm was in 1946 by American computer scientist John Mauchly, who also invented the first general purpose computer ENIAC.
                </div>
            """, unsafe_allow_html=True)

        with col2:
            image_path = os.path.join(IMAGE_DIR, "mauchly.jpg")
            if os.path.exists(image_path):
                image = Image.open(image_path)
                st.image(image, use_container_width=True)
                st.markdown(
                    "<p style='text-align:center; font-size:16px;'>"
                    "<a href='https://www.computerhistory.org/revolution/birth-of-the-computer/4/80/2256' target='_blank' style='text-decoration: none;'>John Mauchly - Learn More</a>"
                    "</p>",
                    unsafe_allow_html=True)
    st.divider()

    # Russian Peasant Multiplication Method Section
    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("Russian Peasant Multiplication Method")
            st.markdown("""
                <div style='font-size:24px; text-align: justify'>
                Despite its name, the Russian Peasant Multiplication Method has little to do with Russian peasants. In fact, scholars have struggled to find solid links to Russia at all. The technique actually traces back to ancient Egypt—specifically a mathematical document called the Rhind Papyrus, dating over 4,000 years ago.<br><br>

                This method allows two numbers to be multiplied using only doubling, halving, and addition, no need for memorizing multiplication tables. One number is repeatedly halved (ignoring fractions), the other is doubled. Rows with even numbers in the halved column are crossed out, and the remaining numbers in the doubled column are summed to get the final product. Often called Egyptian multiplication, Ethiopian multiplication, or binary multiplication.
                </div>
            """, unsafe_allow_html=True)


        with col2:
            image_path = os.path.join(IMAGE_DIR, "rp.jpg")
            if os.path.exists(image_path):
                st.markdown("<div style='margin-top: 20px;'>", unsafe_allow_html=True)
                image = Image.open(image_path)
                st.image(image, use_container_width=True)
                st.markdown(
                "<p style='text-align:center; font-size:16px;'>"
                "<a href='https://thekidshouldseethis.com/post/russian-multiplication-egyptian-math-doubling-and-halving' target='_blank' style='text-decoration: none;'>Russian Peasant - Learn More</a>"
                "</p>",
                unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    ### References:
    - [Insertion Sort - Hideous Humpback Freak](https://hideoushumpbackfreak.com/algorithms/sorting-insertion.html)
    - [Binary Search - Efficient Programming with Components](https://www.jmeiners.com/efficient-programming-with-components/13_searching.html#:~:text=The%20first%20time%20binary%20search,t%20remember%20people%20like%20that.)
    - [Russian Peasant Multiplication - Craft of Coding](https://craftofcoding.wordpress.com/tag/russian-peasant-multiplication/)
    - [Russian Peasant Origins](https://dev.to/geauxweisbeck4/cool-algorithms-pt-1-russian-peasant-multiplication-66a)
    """)
