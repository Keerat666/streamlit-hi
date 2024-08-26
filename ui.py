import streamlit as st
import pandas as pd
import numpy as np

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

st.write("### Heading")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

def hello():
    st.write("Hello, Streamlit!")

st.button("Submit", type="primary", on_click=hello)
