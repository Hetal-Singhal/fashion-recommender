---

# Fashion Recommender App

A **Fashion and Makeup Recommendation System** that provides personalized suggestions based on a user's **skin tone**. Built using **Python** and **Streamlit**, this app helps users choose clothing colors, styles, and makeup that best suit their complexion.

---

## Features

* **Skin Tone Detection**: Detects skin tone from an uploaded image using a pre-trained ML model.
* **Fashion Suggestions**: Provides clothing color and style recommendations tailored to your skin tone.
* **Makeup Guidance**: Suggests makeup colors that complement your complexion.
* **Interactive UI**: Simple and user-friendly interface using Streamlit.

---

## Tech Stack

* **App Framework**: Streamlit
* **Backend & ML**: Python
* **Other Libraries**: OpenCV, PIL, NumPy, Pandas

---

## Usage

Run the Streamlit app:

```bash
streamlit run fashion_app.py
```

1. Open the local URL in your browser (usually `http://localhost:8501`).
2. Upload a clear face image. The app will:

   * Detect your skin tone
   * Recommend suitable clothing colors and styles
   * Suggest matching makeup shades

---

## Project Structure

```
fashion-recommender/
│
├── fashion_app.py       # Streamlit app
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Future Work

* Add **hairstyle recommendations**.
* Support **different lighting conditions**.
* Include **user preferences** for fashion style (casual, formal, ethnic, etc.).
* Deploy on **Streamlit Cloud** for online access.

---

