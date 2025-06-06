import streamlit as st
from src.utils.helper import gen_two_random_values, format_rmm_steps

def rmm_page():
    st.title("Russian Multiplication Method")
    st.write("Multiply two non-negative integers using the Russian Peasant Algorithm.")

    input_mode = st.radio("Choose input method:", ("Random Values", "Manual Input"))

    a, b = None, None

    if input_mode == "Manual Input":
        a = st.number_input("Enter first number (A)", step=1, format="%d")
        b = st.number_input("Enter second number (B)", step=1, format="%d")
    else:
        if st.button("Generate Values"):
            a, b = gen_two_random_values()
            st.session_state["rmm_vals"] = (a, b)
        a, b = st.session_state.get("rmm_vals", (None, None))

    if a is not None and b is not None:
        st.write(f"Multiplying: **{a} × {b}**")

        # Prevent negative values from being computed
        if st.button("Compute"):
            try:
                result, steps, formatted_lines = format_rmm_steps(a, b)

                st.subheader("Steps (Halve A, Double B)")
                st.code("   A   |   B   | Keep?")
                st.code("------------------------")
                for line in formatted_lines:
                    st.code(line)

                kept_values = [b for _, b, keep in steps if keep]
                kept_str = " + ".join(str(v) for v in kept_values)

                st.info(f"Kept values: {kept_str}")
                st.success(f"✅ Result: {result}")

            except ValueError as e:
                st.error(f"{e}")