import streamlit as st

def video_page():
    """Video documentation page"""

    st.title("Video Documentation")

    st.write(
        """
        Welcome to the video documentation section. Below you'll find a comprehensive demo showcasing 
        how this web app works. This video walks through both randomly generated and manually entered arrays 
        to illustrate the algorithm's behavior in different scenarios.
        """
    )

    # Custom HTML to center and expand the iframe to full width
    st.markdown(
        """
        <div style="display: flex; justify-content: center; padding: 0; margin: 0;">
          <iframe 
            src="https://drive.google.com/file/d/1pOxoCK4OSRfY13PMpStJeGXCOAU-6686/preview"
            style="border: none; width: 100%; max-width: 1200px; height: 675px; margin: 0; padding: 0;"
            allow="autoplay"
          ></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
