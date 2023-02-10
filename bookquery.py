# import streamlit as st
# from pysentimiento import create_analyzer

# analyzer = create_analyzer(task="sentiment", lang="en")


# def sentiment_analysis(text):
#     return analyzer.predict(text)


# st.title("Intervention Qualitative Analysis")

# text_input = st.text_area("Enter a statement:")

# if st.button("Analyze"):
#     score = sentiment_analysis(text_input)
#     st.write("Sentiment score:", score)

import streamlit as st
from pysentimiento import create_analyzer

analyzer = create_analyzer(task="sentiment", lang="en")


def sentiment_analysis(text):
    return analyzer.predict(text)


st.title("Intervention Qualitative Analysis")

text_input = st.text_area("Enter a statement:")

if st.button("Analyze"):
    score = sentiment_analysis(text_input)
    # make text bigger and easier colour to read
    st.markdown(
        f'<p style="font-size: 30px; color: red;">Sentiment score: {score}</p>',
        unsafe_allow_html=True,
    )
    # st.write("Sentiment score:", score)
