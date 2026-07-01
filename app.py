import streamlit as st
import pickle

st.title("🎬 Movie Recommendation System")

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

new_df = movies

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(new_df.iloc[i[0]].title)

    return recommended_movies

selected_movie = st.selectbox(
    "Select a movie",
    new_df['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)
