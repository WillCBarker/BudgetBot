# Balance over time
# Investments compounding over time
# Expenses over time
# Cashflow over time

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd

import datetime

import util as u
from financial_components import Expense



# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app_color = {"graph_bg": "#c2d1b4", "graph_line": "#a3b899"}

app.layout = html.Div(
    [
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.H4("MY VERSION STARTING", className="app__header__title"),
                        html.P(
                            "This app does some things",
                            className="app__header__title--grey",
                        ),
                    ],
                    className="app__header__desc",
                ),
            ],
            className="app__header",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [html.H6("EXPENSE OG", className="graph__title")]
                        ),
                        dcc.Graph(
                            id="expense-graph",
                            figure=dict(
                                layout=dict(
                                    plot_bgcolor=app_color["graph_bg"],
                                    paper_bgcolor=app_color["graph_bg"],
                                )
                            ),
                            config={"responsive": True}
                        ),
                    ],
                    className="two-thirds column expense_container",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "EXPENSE1",
                                            className="graph__title",
                                        )
                                    ]
                                ),
                                dcc.Graph(
                                    id="expense-graph1",
                                    figure=dict(
                                        layout=dict(
                                            plot_bgcolor=app_color["graph_bg"],
                                            paper_bgcolor=app_color["graph_bg"],
                                        )
                                    ),
                                ),
                            ],
                            className="graph__container first",
                        ),

                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "EXPENSE2", className="graph__title"
                                        )
                                    ]
                                ),
                                dcc.Graph(
                                    id="expense-graph2",
                                    figure=dict(
                                        layout=dict(
                                            plot_bgcolor=app_color["graph_bg"],
                                            paper_bgcolor=app_color["graph_bg"],
                                        )
                                    ),
                                ),
                            ],
                            className="graph__container second",
                        ),
                    ],
                    className="one-third column bottom_right_box",
                ),
            ],
            className="app__content",
        ),
    ],
    className="app__container",
)



@app.callback(
    Output("expense-graph", "figure"),
    [Input("start-date", "date"),
     Input("end-date", "date")]
)
def plot_expenses(start_date, end_date):
    """ Plots accrued expenses on line graph """
    # TODO: Plot all expenses on same chart, have option to seperate into seperate lines (1 for each expense)
    #       will need to group all expenses by some global frequency though

    # Create an Expense object
    expense = Expense(name="Electricity", amount=200, category="utilities", frequency="monthly")
    
    # REVISIT
    if not start_date:
        start_date="2023-01-01"
    if not end_date:
        end_date="2024-01-01"

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    day_count = u.get_time_difference(start_date, end_date)
    frequency_int_annual = u.convert_frequency_of_return(expense.frequency)
    occurences = u.get_occurences_in_time_interval(day_count, frequency_int_annual)
    expense_track = u.compound_occurences_in_list(expense.amount, occurences)

    df = pd.DataFrame({
        "Date": pd.date_range(start=start_date, end=end_date, periods=occurences),
        "Accrued Expense": expense_track,
    })

    # Create the line graph
    fig = {
        "data": [
            {
                "x": df["Date"],
                "y": df["Accrued Expense"],
                "type": "line",
                "name": "Accrued Expense",
            },
        ],
        "layout": {
            "title": "Accrued Expense Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Accrued Expense"},
        },
    }

    return fig


@app.callback(
    Output("expense-graph1", "figure"),
    [Input("start-date1", "date"),
     Input("end-date1", "date")]
)
def plot_expenses(start_date, end_date):
    """ Plots accrued expenses on line graph """
    # TODO: Plot all expenses on same chart, have option to seperate into seperate lines (1 for each expense)
    #       will need to group all expenses by some global frequency though

    # Create an Expense object
    expense1 = Expense(name="Electricity", amount=200, category="utilities", frequency="monthly")
    
    # REVISIT
    if not start_date:
        start_date="2023-01-01"
    if not end_date:
        end_date="2024-01-01"

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    day_count = u.get_time_difference(start_date, end_date)
    frequency_int_annual = u.convert_frequency_of_return(expense1.frequency)
    occurences = u.get_occurences_in_time_interval(day_count, frequency_int_annual)
    expense_track = u.compound_occurences_in_list(expense1.amount, occurences)

    df = pd.DataFrame({
        "Date": pd.date_range(start=start_date, end=end_date, periods=occurences),
        "Accrued Expense": expense_track,
    })

    # Create the line graph
    fig = {
        "data": [
            {
                "x": df["Date"],
                "y": df["Accrued Expense"],
                "type": "line",
                "name": "Accrued Expense",
            },
        ],
        "layout": {
            "title": "Accrued Expense Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Accrued Expense"},
        },
    }

    return fig


@app.callback(
    Output("expense-graph2", "figure"),
    [Input("start-date2", "date"),
     Input("end-date2", "date")]
)
def plot_expenses(start_date, end_date):
    """ Plots accrued expenses on line graph """
    # TODO: Plot all expenses on same chart, have option to seperate into seperate lines (1 for each expense)
    #       will need to group all expenses by some global frequency though

    # Create an Expense object
    expense1 = Expense(name="Electricity", amount=200, category="utilities", frequency="monthly")
    
    # REVISIT
    if not start_date:
        start_date="2023-01-01"
    if not end_date:
        end_date="2024-01-01"

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    day_count = u.get_time_difference(start_date, end_date)
    frequency_int_annual = u.convert_frequency_of_return(expense1.frequency)
    occurences = u.get_occurences_in_time_interval(day_count, frequency_int_annual)
    expense_track = u.compound_occurences_in_list(expense1.amount, occurences)

    df = pd.DataFrame({
        "Date": pd.date_range(start=start_date, end=end_date, periods=occurences),
        "Accrued Expense": expense_track,
    })

    # Create the line graph
    fig = {
        "data": [
            {
                "x": df["Date"],
                "y": df["Accrued Expense"],
                "type": "line",
                "name": "Accrued Expense",
            },
        ],
        "layout": {
            "title": "Accrued Expense Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Accrued Expense"},
        },
    }

    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
