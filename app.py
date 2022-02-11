import pickle
import streamlit as st
import requests
import pandas as pd
import gzip, pickle


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e3a2c444f9664e7ae913b3a98a935c17".format(movie_id)
    data = requests.get(url)
    data = data.json()
    print(data)
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


movies = gzip.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies)

st.markdown("<h1 style='text-align: center; color: white;'>THE RECOMMENDER</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>BY ANKIT KORI</h4>", unsafe_allow_html=True)



st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://laptopstalk.com/wp-content/uploads/2020/04/apps.55787.9007199266246365.687a10a8-4c4a-4a47-8ec5-a95f70d8852d.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://laptopstalk.com/wp-content/uploads/2020/04/apps.55787.9007199266246365.687a10a8-4c4a-4a47-8ec5-a95f70d8852d.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)


if st.button('Show Recommendation'):
    st.write("<h4 style='text-align: center; color: White;'>MOVIES YOU MAY LIKE</h4>", unsafe_allow_html=True)
    st.write("##")
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
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
    
