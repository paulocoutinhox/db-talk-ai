import plotly.express as px
from pandas import DataFrame

from .base_chart import BaseChart


class PieChart(BaseChart):
    name = "Pie Chart"
    prompt = """
    Generate a pie chart representing the distribution of categories:
    - The first column should contain category names (labels).
    - The second column should contain numerical values (sizes).

    The chart should clearly show the proportion of each category relative to the total.
    """

    def generate(self, df: DataFrame):
        if len(df.columns) >= 2:
            x, y = df.columns[0], df.columns[1]
            return px.pie(df, names=x, values=y, title=f"{y} Distribution by {x}")
        else:
            raise ValueError(
                "The DataFrame must have at least two columns for a pie chart."
            )
