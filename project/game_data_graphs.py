"""CSC110 Fall 2021 Final Assignment: Game Data Graphs

===============================
This file contains just one function which displays the 3 distinct, interactive graphs of the games
data. It will be imported into main.py.

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jeanine Colleen Ohene-Agyei, Luke Ham, Chelsea Wang, and Bolin Shen.
"""
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def all_graphs(time: list, essential: list, nonessential: list, stress: list) -> None:
    """Displays all the graphs of the users data on one browser.
     Each graph is separate from the others so it is easier to read."""
    fig = make_subplots(rows=3, cols=1, subplot_titles=("Change Average Essential Spending",
                        "Change Average Non-Essential Spending", "Change in Stress Percentage"))

    fig.append_trace(go.Scatter(x=time, y=essential, name='Essential'), row=1, col=1)
    fig.append_trace(go.Scatter(x=time, y=nonessential, name='Non-Essential'), row=2, col=1)
    fig.append_trace(go.Scatter(x=time, y=stress, name='Stress'), row=3, col=1)

    fig.update_yaxes(title_text="Change in Essential Spending ($)", row=1, col=1)
    fig.update_yaxes(title_text="Change in Non-Essential Spending ($)", row=2, col=1)
    fig.update_yaxes(title_text="Change in Stress (%)", row=3, col=1)

    fig.update_xaxes(title_text="Months", row=1, col=1)
    fig.update_xaxes(title_text="Months", row=2, col=1)
    fig.update_xaxes(title_text="Months", row=3, col=1)

    fig.update_layout(height=1700, width=1300, title_text="Game Data Results (BACK TO GAME FOR"
                                                          " ANALYSIS)")
    fig.show()


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['make_subplots', 'plotly.subplots', 'plotly.graph_objects',
                          'python_ta.contracts', 'python_ta'],
        'allowed-io': ['all_graphs'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
