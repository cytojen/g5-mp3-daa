import streamlit as st
from src.utils.helper import measure_insertion_runtime, generate_random_array

def insertion_page():
    """Insertion Sort page content"""
    st.title("Insertion Sort Visualizer")
    st.write("Visualize how insertion sort works step by step.")

    # Let user choose the data type first
    value_type = st.radio("Data type", ("Numbers", "Letters"))

    # Input mode selection
    input_mode = st.radio(
        "Choose input method:",
        ("Random Value Generator", "Input your own values")
    )

    arr = []

    # Handle random input
    if input_mode == "Random Value Generator":
        n = st.number_input("Number of elements", min_value=2, max_value=20, value=5)

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
    generate = st.button("Sort")

    if generate:
        # Build the array
        if input_mode == "Random Value Generator":
            arr = generate_random_array(int(n), int(min_val), int(max_val), value_type)
        else:
            raw_values = [x.strip() for x in user_input.split(",") if x.strip()]
            try:
                arr = [int(x) for x in raw_values]
            except ValueError:
                arr = raw_values

        if not arr:
            st.warning("Please provide valid input.")
            return

        # Call the measure_insertion_runtime function
        runtime, passes, sorted_arr = measure_insertion_runtime(arr, ascending=ascending)

        # Show original array and sorting steps side-by-side
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Array")
            st.code(f"{arr}", language="python")
            st.success(f"Sorted array: {sorted_arr}")

        with col2:
            st.subheader("Sorting Steps")
            for idx, state in enumerate(passes, 1):
                st.code(f"Pass {idx}: {state}")

        # Final result
        st.divider()
        st.subheader("Performance")
        st.info(f"⏱️ Runtime: {runtime:.8f} seconds")
