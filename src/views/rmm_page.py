import streamlit as st
from src.utils.helper import gen_two_random_values, format_rmm_steps

def rmm_page():
    """Russian Multiplication Method page content"""
    st.title("Russian Multiplication Method")
    st.write("Multiply two non-negative integers using the Russian Peasant Algorithm.")

    input_mode = st.radio("Choose input method:", ("Random Values", "Manual Input"))

    a, b = None, None

    # Handle input depending on user selection
    if input_mode == "Manual Input":
        a = st.number_input("Enter first number (A)", value=0.0, format="%g")
        b = st.number_input("Enter second number (B)", value=0.0, format="%g")
    else:
        if st.button("Generate Values"):
            a, b = gen_two_random_values()
            st.session_state["rmm_vals"] = (a, b)
        a, b = st.session_state.get("rmm_vals", (None, None))

    # Proceed only if both inputs are available
    if a is not None and b is not None:
        st.write(f"Multiplying: **{a} × {b}**")

        # Prevent negative values from being computed
        if st.button("Compute"):
            try:
                result, steps, formatted_lines = format_rmm_steps(a, b)

                # Display each step in tabular format (trying to)
                st.subheader("Steps (Halve A, Double B)")
                st.code("   A   |   B   | Keep?")
                st.code("------------------------")
                for line in formatted_lines:
                    st.code(line)

                # Extract and show the values that were kept for the final sum
                kept_values = [b for _, b, keep in steps if keep]
                kept_str = " + ".join(str(v) for v in kept_values)

                # Results
                st.info(f"Kept values: {kept_str}")
                st.success(f"Result: {result}")

            # Catch and display any input validation errors from the helper
            except ValueError as e:
                st.error(f"{e}")