import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"])

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

