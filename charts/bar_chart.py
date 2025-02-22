import plotly.express as px
from pandas import DataFrame

from .base_chart import BaseChart


class BarChart(BaseChart):
    name = "Bar Chart"
    prompt = """
    Generate a bar chart using two columns:
    - One categorical column for the x-axis.
    - One numerical column for the y-axis.

    The output should clearly show the numerical values distributed across different categories.
    Ensure appropriate labels for clarity.
    """

    def generate(self, df: DataFrame):
        if len(df.columns) >= 2:
            x, y = df.columns[0], df.columns[1]
            return px.bar(df, x=x, y=y, title=f"{y} by {x}")
        else:
            raise ValueError(
                "The DataFrame must have at least two columns for a bar chart."
            )
