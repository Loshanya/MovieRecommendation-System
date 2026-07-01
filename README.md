# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Machine Learning**, **Natural Language Processing (NLP)**, and **Streamlit**. The application recommends movies similar to the one selected by the user based on movie metadata such as genres, keywords, cast, crew, and overview.

---

## 🚀 Features

- Recommend 5 similar movies based on user selection.
- Content-based recommendation using Cosine Similarity.
- Interactive web interface built with Streamlit.
- Fast recommendations using precomputed similarity matrix.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## 📂 Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

---

## ⚙️ Machine Learning Workflow

1. Load movie and credits datasets.
2. Merge both datasets.
3. Data preprocessing and cleaning.
4. Feature engineering using:
   - Genres
   - Keywords
   - Cast
   - Crew
   - Movie Overview
5. Create a combined **tags** column.
6. Text preprocessing:
   - Lowercasing
   - Stemming
7. Convert text into vectors using **CountVectorizer**.
8. Compute **Cosine Similarity**.
9. Build a recommendation function.
10. Deploy using Streamlit.

---

## 📸 Project Demo

### Home Page

*(Add a screenshot here after completing the UI.)*

### Recommendations

*(Add a screenshot showing the recommended movies.)*

---

## 📁 Project Structure

```
MovieRecommendation-System/
│
├── app.py
├── MovieRecommendation.ipynb
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/MovieRecommendation-System.git
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Add movie posters using the TMDB API.
- Display ratings and release dates.
- Improve UI with custom styling.
- Deploy the application online using Streamlit Cloud.

---

## 👩‍💻 Author

**Loshanya Sasapu**

B.Tech, Civil Engineering  
Indian Institute of Technology Guwahati


