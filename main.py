import langchain_helper as lch
import streamlit as st

st.title("Pets Name Generator")

animal_type = st.sidebar.selectbox("What kind of animal is your pet?", ("Dog", "Cat", "Wolf", "Bear"))

if animal_type == "Dog":
  pet_color = st.sidebar.text_input(label="What color is your dog?", max_chars=15)

if animal_type == "Cat":
  pet_color = st.sidebar.text_input(label="What color is your cat?", max_chars=15)

if animal_type == "Wolf":
  pet_color = st.sidebar.text_input(label="What color is your wolf?", max_chars=15)

if animal_type == "Bear":
  pet_color = st.sidebar.text_input(label="What color is your bear?", max_chars=15)

if pet_color: 
  response = lch.generate_pet_name(animal_type, pet_color)
  st.text(response["pet_name"])