import plotly.express as px
from pandas import DataFrame

from .base_chart import BaseChart


class HeatmapChart(BaseChart):
    name = "Heatmap Chart"
    prompt = """
    Generate a heatmap using geographical coordinates:
    - The second column should contain latitude values.
    - The third column should contain longitude values.
    - The fourth column (optional) should contain intensity values.

    The map should visualize data density or intensity using a heatmap overlay.
    """

    def generate(self, df: DataFrame):
        if len(df.columns) >= 3:
            label, lat, lon = df.columns[0], df.columns[1], df.columns[2]
            intensity = df.columns[3] if len(df.columns) > 3 else None

            heatmap = px.density_map(
                df,
                lat=lat,
                lon=lon,
                z=intensity,
                radius=10,
                hover_name=label,
                hover_data=(
                    {lat: True, lon: True, intensity: True}
                    if intensity
                    else {lat: True, lon: True}
                ),
                title="Geographical Heatmap",
                height=600,
                width=800,
                center=dict(lat=df[lat].mean(), lon=df[lon].mean()),
                color_continuous_scale="Viridis",
            )

            return heatmap
        else:
            raise ValueError(
                "The DataFrame must have at least three columns: label, latitude, and longitude."
            )
