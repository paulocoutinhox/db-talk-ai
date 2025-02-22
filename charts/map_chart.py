import plotly.express as px
from pandas import DataFrame

from .base_chart import BaseChart


class MapChart(BaseChart):
    name = "Map Chart"
    prompt = """
    Generate a scatter map using geographical coordinates:
    - The second column should contain latitude values.
    - The third column should contain longitude values.

    The map should plot points based on the provided geographical coordinates.
    Additional columns can be used for hover information.
    """

    def generate(self, df: DataFrame):
        if len(df.columns) >= 3:
            label, lat, lon = df.columns[0], df.columns[1], df.columns[2]

            # Using scatter_mapbox with default layout
            map = px.scatter_map(
                df,
                lat=lat,
                lon=lon,
                text=label,
                hover_name=label,
                hover_data={lat: True, lon: True},
                title="Geographical Scatter Map",
                height=600,
                width=800,
            )

            # Customize marker appearance
            map.update_traces(
                marker=dict(
                    size=14,
                    symbol="marker",
                    color="red",
                    opacity=0.9,
                )
            )

            return map
        else:
            raise ValueError(
                "The DataFrame must have at least three columns: label, latitude, and longitude."
            )
