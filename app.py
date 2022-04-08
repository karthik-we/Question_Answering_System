import streamlit as st
from transformers import pipeline
import streamlit.components.v1 as components

components.html(
    
    """
    <style>
    .display-4{
        text-align:center;
        font-weight:bold !important;
    }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <div class="jumbotron" style="background-color:cyan">
  <h1 class="display-4" >Q & A Model</h1>
  <p style="text-align:center">Find the answer for the questions of your articles. </p>
  
</div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    height=300,
)
@st.cache(allow_output_mutation=True)

def load_model():
    model=pipeline("question-answering")
    return model

qa = load_model()
st.title("Ask questions based on the article")

articles = st.text_area("Please enter your article")
quest = st.text_input("Ask questions in the article:")
button= st.button("Answer")
with st.spinner("Finding answers"):
    if button and articles:
        answers = qa(question=quest, context=articles)
        st.success(answers['answer'])