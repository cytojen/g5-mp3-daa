import streamlit as st
from src.utils.helper import measure_binary_search_runtime, generate_sorted_array

def binary_search_page():
    """Binary search page content"""
    st.title("Binary Search Visualizer")
    st.write("Search a sorted array using binary search.")
    
    # Let user choose the data type first\
    value_type = st.radio("Data type", ("Numbers", "Letters"))

    # Input method selection
    input_mode = st.radio("Choose input method:", ("Random Generator", "Input your own values"))

    arr = []

    # Handle random array generation
    if input_mode == "Random Generator":
        n = st.number_input("Number of elements", 2, 20, 5)

        # Set min and max values depending on data type
        if value_type == "Numbers":
            min_val = st.number_input("Min value", 0)
            max_val = st.number_input("Max value", 100)
        else:
            min_val, max_val = ord("A"), ord("Z")

        # Generate the array when button clicked and save in session state
        if st.button("Generate Array"):
            arr = generate_sorted_array(int(n), int(min_val), int(max_val), value_type)
            st.session_state["generated_array"] = arr

        # Retrieve array from session state after generation
        arr = st.session_state.get("generated_array", [])

    # Handle manual array input
    else:
        arr_input = st.text_input("Enter comma-separated values:")
        if arr_input:
            raw = [x.strip() for x in arr_input.split(",") if x.strip()]
            try:
                # Parse input to int or keep as string depending on data type
                arr = [int(x) for x in raw] if value_type == "Numbers" else raw
            except:
                st.warning("Invalid array input.")
                return
            # Check if array is sorted
            if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
                st.warning("Array must be sorted.")
                return

    # Display the array if available
    if arr:
        st.subheader("Array (Sorted)")
        st.code(arr)

   
    # Get target input and run binary search if array exists
    if input_mode == "Input your own values" or (input_mode == "Random Generator" and arr):
        target_input = st.text_input("Enter value to search for:")
        if st.button("Search"):
            if not arr:
                st.warning("Enter a sorted array first.")
                return
            try:
                # Convert target input according to data type
                target = int(target_input) if value_type == "Numbers" else target_input
                if value_type == "Letters" and len(target) != 1:
                    raise ValueError

                # Call the measure time function from the helper file 
                # which also calls the binary search algorithm
                runtime, passes, index, _ = measure_binary_search_runtime(arr, target)

                # Show original array and search results side-by-side
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Array")
                    st.code(arr)
                    if index != -1:
                        st.success(f"Found {target} at index {index}")
                    else:
                        st.error(f"{target} not found")
                with col2:
                    st.subheader("Search Steps")
                    for i, (l, m, r, mv) in enumerate(passes, 1):
                        st.code(f"Pass {i}: left={l} val={arr[l]}, mid={m} val={mv}, right={r} val={arr[r]}")

                # Final result
                st.divider()
                st.subheader("Performance")
                st.info(f"Runtime: {runtime:.8f} sec")

            # Catch an invalid search input
            except:
                st.warning("Invalid target input.")
