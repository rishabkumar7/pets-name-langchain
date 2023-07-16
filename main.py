import streamlit as st
import langchain_helper as lch

st.title("Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Rat", "Snake", "Lizard", "Cow"))

if animal_type == "Dog":
  pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=25)

if animal_type == "Cat":
  pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=25) 


if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.header(response['pet_name'])