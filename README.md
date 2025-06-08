<h1 align="center">Divide and Conquer Algorithms Visualizer</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python Badge" height="40"/>
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-1.45.0-red?logo=streamlit&logoColor=white" alt="Streamlit Badge" height="40"/>
  </a>
</p>

<h1 align="center">
  🔗 <strong>Live App:</strong> <a href="https://dncalgo.streamlit.app/" target="_blank" rel="noopener noreferrer" >dncalgo.streamlit.app</a>
</h1>

---

## Overview

This project is a **visualization tool** for learning and understanding *Divide and Conquer* algorithms step-by-step made by Group 6. This is built using **Streamlit** and it allows users to explore the inner workings of classic D&C algorithms step-by-step in an intuitive web interface.

---

## Features

- ✅ Select from multiple Decrease and Conquer algorithms  
- ✅ Input custom data arrays  
- ✅ View algorithm step-by-step visualization  
- ✅ Check the runtime of the algorithm

---

## Tech Stack

- **Language:** Python 3.12
- **Framework:** Streamlit 1.45.0
- **Deployment:** Streamlit Community Cloud

---

## Installation & Setup

1. Clone the repo  
  ```
   git clone https://github.com/cytojen/g5-mp3-daa.git
   cd g5-mp3-daa
  ```

2. Create a virtual environment
  ```
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # or venv\Scripts\activate  on Windows
  ```

3. Install dependencies
  ```
    pip install -r requirements.txt
  ```

5. Run the Streamlit app locally
  ```
    streamlit run app.py
  ```

---


```
cytojen-g5-mp3-daa/
├── app.py
├── requirements.txt
├── src/
│   ├── static/
│   │   └── images/
│   ├── utils/
│   │   ├── helper.py
│   │   └── algorithms/
│   │       ├── binary_search.py
│   │       ├── insertion_sort.py
│   │       └── rmm.py
│   └── views/
│       ├── about_page.py
│       ├── binary_search_page.py
│       ├── home_page.py
│       ├── insertion_page.py
│       ├── rmm_page.py
│       ├── video_page.py
│       └── __pycache__/
├── .devcontainer/
│   └── devcontainer.json
└── .streamlit/
    └── config.toml
```

---

# Contributions are always welcome!
1. Fork the repo
2. Create a feature branch (git checkout -b feature/your-feature)
3. Commit your changes
4. Push the branch (git push origin feature/your-feature)
5. Open a Pull Request

---

### Developed by Group 6

