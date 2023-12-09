# Balance over time
# Investments compounding over time
# Expenses over time
# Cashflow over time

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

import pandas as pd

import datetime

import util as u
from financial_components import Expense
from budget import Budget

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# Define the layout of the app
app_color = {"graph_bg": "#c2d1b4", "graph_line": "#a3b899"}

app.layout = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(
                    label="Tab one",
                    tab_id="tab-1",
                    label_style={"color": "black"},
                    active_tab_style={"background-color": "#4d6650"}
                ),
                dbc.Tab(
                    label="Tab two",
                    tab_id="tab-2",
                    label_style={"color": "black"},
                    active_tab_style={"color": "#4d6650"}
                )
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(html.P(id="content", className="p-4")),
    ],
)
                    
tab1_content = html.Div(
    [
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.H4(
                            "MY VERSION STARTING",
                            className="app__header__title",
                        ),
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
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "EXPENSE OG",
                                            className="graph__title",
                                        )
                                    ]
                                ),
                                dcc.Graph(
                                    id="expense-graph",
                                    figure=dict(
                                        layout=dict(
                                            plot_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                            paper_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                        )
                                    ),
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                    },
                                ),
                            ],
                            className="expense_container",
                        ),
                    ],
                    className="two-thirds graph__container",
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
                                            plot_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                            paper_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                        )
                                    ),
                                ),
                            ],
                            className="one-third graph__container first",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "EXPENSE2",
                                            className="graph__title",
                                        )
                                    ]
                                ),
                                dcc.Graph(
                                    id="expense-graph2",
                                    figure=dict(
                                        layout=dict(
                                            plot_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                            paper_bgcolor=app_color[
                                                "graph_bg"
                                            ],
                                        )
                                    ),
                                ),
                            ],
                            className="one-third graph__container second",
                        ),
                    ],
                    className="bottom_right_box",
                ),
            ],
            className="app__content",
        ),
    ],
    className="app__container",
)

tab2_content = html.Div([
    dbc.Container([
        html.H1("Financial Tracker"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H3("Add General Balance"), 
                html.P("Enter Balance Name", className="col_question_label"),
                dbc.Input(
                    id='income_name', 
                    placeholder='Ex. Checkings', 
                    type='text',
                    class_name="col_input"
                    ),

                html.P("Enter Stored Amount", className="col_question_label"),
                dbc.Input(
                    id='income_amount',
                    placeholder='Ex: 12800', 
                    type='text', 
                    class_name="col_input"
                    ),

                html.P("Enter Yield Percentage", className="col_question_label"),
                dbc.Input(
                    id='investment_yield', 
                    placeholder='Ex: 2%', 
                    type='text', 
                    class_name="col_input",
                    ),
                html.Button("Add Balance", id="create_balance_btn", className="col_create_btn"),
                ],

                class_name="tab2_column_top_row"
                ),


            dbc.Col([
                html.H3("Add Income Source"), 
                html.P("Enter Income Source Name", className="col_question_label"),
                dbc.Input(
                    id='income_name', 
                    placeholder='Ex. Salary', 
                    type='text',
                    class_name="col_input"
                    ),

                html.P("Enter Income Amount", className="col_question_label"),
                dbc.Input(
                    id='income_amount',
                    placeholder='Ex: 1700', 
                    type='text', 
                    class_name="col_input"
                    ),

                html.P("How often will this income be received?", className="col_question_label"),
                dbc.RadioItems(
                    options=[
                        {"label": "Just this once", "value": 1},
                        {"label": "Daily", "value": "Daily"},
                        {"label": "Weekly", "value": "Weekly"},
                        {"label": "Biweekly", "value": "Biweekly"},
                        {"label": "Monthly", "value": "Monthly"},
                        {"label": "Quarterly", "value": "Quarterly"},
                        {"label": "Semiannually", "value": "Semiannually"},
                        {"label": "Annually", "value": "Annually"},
                    ],
                    id="income_freq",
                    value=1,
                    class_name="col_input",
                    ),
                html.Button("Add Income", id="create_income_btn", className="col_create_btn"),
                ],

                class_name="tab2_column_top_row"
                ),


                            dbc.Col([
                html.H3("Add Expense"),
                html.P("Enter Expense Name", className="col_question_label"),
                dbc.Input(
                    id='expense_name', 
                    placeholder='Ex: Netflix', 
                    type='text', 
                    class_name="col_input"
                    ),
                html.P("Enter Expense Amount", className="col_question_label"),
                dbc.Input(
                    id='expense_amount', 
                    placeholder='Ex: 20', 
                    type='text', 
                    class_name="col_input"
                    ),
                html.P("How often will this expense occur?", className="col_question_label"),
                dbc.RadioItems(
                    options=[
                        {"label": "Just this once", "value": 1},
                        {"label": "Daily", "value": "Daily"},
                        {"label": "Weekly", "value": "Weekly"},
                        {"label": "Biweekly", "value": "Biweekly"},
                        {"label": "Monthly", "value": "Monthly"},
                        {"label": "Quarterly", "value": "Quarterly"},
                        {"label": "Semiannually", "value": "Semiannually"},
                        {"label": "Annually", "value": "Annually"},
                    ],
                    id="expense_freq",
                    value=1,
                    class_name="col_input",
                ),
                html.Button("Add Expense", id="create_expense_btn", className="col_create_btn"),
                ],

                class_name="tab2_column_top_row"
                ),


            dbc.Col([
                html.H3("Add Investment"), 
                html.P("Enter Investment Name", className="col_question_label"),
                dbc.Input(
                    id='investment_name', 
                    placeholder='Ex: Apple Stock', 
                    type='text',
                    class_name="col_input"
                    ),

                html.P("Enter Investment Amount", className="col_question_label"),
                dbc.Input(
                    id='investment_amount', 
                    placeholder='Ex: 6500', 
                    type='text', 
                    class_name="col_input"
                    ),

                html.P("Enter Investment Yield Percentage", className="col_question_label"),
                dbc.Input(
                    id='investment_yield', 
                    placeholder='Ex: 4', 
                    type='text', 
                    class_name="col_input"
                    ),

                html.P("How often will this investment accrue?", className="col_question_label"),
                dbc.RadioItems(
                    options=[
                        {"label": "Daily", "value": "Daily"},
                        {"label": "Weekly", "value": "Weekly"},
                        {"label": "Biweekly", "value": "Biweekly"},
                        {"label": "Monthly", "value": "Monthly"},
                        {"label": "Quarterly", "value": "Quarterly"},
                        {"label": "Semiannually", "value": "Semiannually"},
                        {"label": "Annually", "value": "Annually"},
                    ],
                    id="investment_freq",
                    value=1,
                    class_name="col_input",
                    ),
                html.Button("Add Investment", id="create_investment_btn", className="col_create_btn"),
                ],

                class_name="tab2_column_top_row"
                ),

            
        ]),
        dbc.Row([
            dbc.Col([],class_name="tab2_column_bottom_row"), # fill with created budget objects
            dbc.Col([html.Div(id='income-output-div')],class_name="tab2_column_bottom_row"), # fill with income objects
            dbc.Col([html.Div(id='expense-output-div')],class_name="tab2_column_bottom_row"), # fill with expense objects
            dbc.Col([],class_name="tab2_column_bottom_row") # fill with investment objects
        ])
    ])
])

""" Following functions take the add attribute prompts and insert them into the current budget DS"""
B = Budget("my-budget", 10000)
@app.callback(
    Output('expense-output-div', 'children'),
    [Input('create_expense_btn', 'n_clicks')],
    [State('expense_name', 'value'),
     State('expense_amount', 'value'),
     State('expense_freq', 'value')]
)
def create_expense(n_clicks, name, amount, frequency):
    if n_clicks:
        if name and frequency and amount:
            B.add_expense(amount=amount, name=name, frequency=frequency, category="test")
        expenses = B.expenses
        object_details = [html.P(f"Expense: Name={obj.name}, Amount={obj.amount}, Frequency={obj.frequency}") for obj in expenses]
        return object_details


@app.callback(
    Output('income-output-div', 'children'),
    [Input('create_income_btn', 'n_clicks')],
    [State('income_name', 'value'),
     State('income_amount', 'value'),
     State('income_freq', 'value')]
)
def create_income(n_clicks, name, amount, frequency):
    if n_clicks:
        if name and frequency and amount:
            B.add_income(amount=amount, name=name, frequency=frequency, date="07-15-2022")
        incomes = B.incomes
        object_details = [html.P(f"Income: Name={obj.source}, Amount={obj.amount}, Frequency={obj.frequency}") for obj in incomes]
        return object_details





# Renders page based on active tab selected
@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    return html.P("This shouldn't ever be displayed...")


@app.callback(
    Output("expense-graph", "figure"),
    [
    Input("start-date", "date"),
    Input("end-date", "date"),
     ]
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
