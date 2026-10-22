"""Practical 9.1 - Plotly interactive scatter plot (iris dataset)."""
import plotly.express as px


def main():
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title="Iris: sepal width vs sepal length",
    )
    # Original built `fig` but never displayed it.
    fig.show()


if __name__ == "__main__":
    main()
