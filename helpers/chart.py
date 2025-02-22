from charts.bar_chart import BarChart
from charts.heatmap_chart import HeatmapChart
from charts.line_chart import LineChart
from charts.map_chart import MapChart
from charts.pie_chart import PieChart


def load_charts():
    # List of charts
    chart_classes = [
        BarChart,
        LineChart,
        PieChart,
        MapChart,
        HeatmapChart,
    ]

    # Sort charts alphabetically by name
    sorted_chart_classes = sorted(chart_classes, key=lambda c: c.name)

    return sorted_chart_classes
