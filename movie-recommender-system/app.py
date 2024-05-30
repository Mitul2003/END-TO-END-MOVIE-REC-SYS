import streamlit as st
import pickle
import pandas as pd
import requests

print("hello")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# to fetch the detail of ipynb file
movie_dict = pickle.load(open('movie_dic.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# to fetch the detail of ipynb filename
similarity_dict = pickle.load(open('similarity.pkl', 'rb'))
similarity = pd.DataFrame(similarity_dict)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie, recommended_movie_poster


st.title('Movi Recommender System')
# to make select text box
select_movie = st.selectbox('How would you like to be contacted?', movies['title'].values)

# to make button
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(select_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

