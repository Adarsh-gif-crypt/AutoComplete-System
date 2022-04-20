import pickle
import streamlit as st
from utils import *

@st.cache
def get_predictions(input_tokens, starts, k = 1.0):
    n_gram_counts_list = pickle.load(open('data/en_counts.txt', 'rb'))
    vocabulary = pickle.load(open('data/vocab.txt', 'rb'))
    suggestion = get_suggestions(input_tokens, n_gram_counts_list, vocabulary, k=k, start_with = starts)
    return suggestion

st.set_page_config(layout = 'wide')
st.title("Auto Complete System")
st.markdown("---")


st.markdown("""#### This AutoComplete System is a word Suggestion Webapp which suggests the next word on the basis of current Input. Just input your sentence, and select the smoothening factor and you're done. You can also use the optional Input for more accuracy.""")
st.markdown('---')
sentence = st.text_input("Enter a sentence")
st.subheader("Optional Inputs")
starts = st.text_input("The starting letter of the expected next word")
k = st.number_input("Enter smoothing factor k")

tokenized = sentence.split()

if st.button("Predict"):
    suggestion = get_predictions(tokenized, starts, k)
    
    st.markdown(f'The suggested word is {suggestion[0]}')
