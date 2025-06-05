import streamlit as st
import random
from src.utils.insertion_sort import *

def insertion_page():
    """Insertion Sort page content"""
    st.title("Insertion Sort Visualizer")
    st.write("Visualize how insertion sort works step by step.")

    # Input mode selection
    input_mode = st.radio(
        "Choose input method:",
        ("Random Number/Letter Generator", "Input your own values")
    )

    arr = []
    value_type = "Numbers"

    # Handle random input
    if input_mode == "Random Number/Letter Generator":
        n = st.number_input("Number of elements", min_value=2, max_value=20, value=5)
        value_type = st.radio("Data type", ("Numbers", "Letters"))

        if value_type == "Numbers":
            min_val = st.number_input("Minimum value", value=0)
            max_val = st.number_input("Maximum value", value=100)
        else:
            min_val = ord('A')
            max_val = ord('Z')

    # Handle manual input
    else:
        user_input = st.text_input("Enter comma-separated values (e.g. 5, 3, 9, 1 or a, b, c):")

    # Sorting direction
    ascending = st.checkbox("Sort in ascending order?", value=True)

    # Generate button
    generate = st.button("Generate Output")

    if generate:
        # Build the array
        if input_mode == "Random Number/Letter Generator":
            if value_type == "Numbers":
                arr = [random.randint(int(min_val), int(max_val)) for _ in range(int(n))]
            else:
                arr = [chr(random.randint(min_val, max_val)) for _ in range(int(n))]
        else:
            raw_values = [x.strip() for x in user_input.split(",") if x.strip()]
            try:
                arr = [int(x) for x in raw_values]
                value_type = "Numbers"
            except ValueError:
                arr = raw_values
                value_type = "Letters"

        if not arr:
            st.warning("Please provide valid input.")
            return

        # Call the measure_runtime function from insertion_sort.py
        # This then calls the insertion_sort function as well as the print_passes function.
        runtime, passes, sorted_arr = measure_runtime(arr, ascending=ascending)

        # Show original array and sorting steps side-by-side
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🟦 Original Array")
            st.code(f"{arr}", language="python")

        with col2:
            st.subheader("🔄 Sorting Steps")
            for idx, state in enumerate(passes, 1):
                st.code(f"Pass {idx}: {state}")

        # Final result across full width
        st.divider()
        st.subheader("Final Result")
        st.success(f"✅ Sorted array: {sorted_arr}")
        st.info(f"⏱️ Runtime: {runtime:.8f} seconds")
