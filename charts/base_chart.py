import streamlit as st
from pandas import DataFrame


class BaseChart:
    name = "Base Chart"
    prompt = "Generate a simple chart."

    def generate(self, df: DataFrame):
        raise NotImplementedError("You must implement the generate method.")

    def render(self, df: DataFrame):
        chart = self.generate(df)

        if chart:
            st.plotly_chart(chart)
