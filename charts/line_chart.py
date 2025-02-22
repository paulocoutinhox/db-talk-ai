import plotly.express as px
from pandas import DataFrame

from .base_chart import BaseChart


class LineChart(BaseChart):
    name = "Line Chart"
    prompt = """
    Generate a line chart using time-series or ordered numerical data:
    - The x-axis should contain time-related or sequential data.
    - The y-axis should contain numerical values.

    The line should smoothly connect the points in order, representing the progression over time or sequence.
    """

    def generate(self, df: DataFrame):
        if len(df.columns) >= 2:
            x, y = df.columns[0], df.columns[1]
            return px.line(df, x=x, y=y, title=f"{y} over {x}")
        else:
            raise ValueError(
                "The DataFrame must have at least two columns for a line chart."
            )
