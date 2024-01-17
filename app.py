import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, ctx

import pandas as pd

import datetime

import util as u
from financial_components import Expense
from budget import Budget

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

created_budgets = {}

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
        html.H1("Financial Tracker", className="tab2_title"),
        html.H4("Select Existing Budget"),
        dcc.Dropdown(
                id="budget-dropdown",
                options=[{"label": name, "value": name} for name in created_budgets.keys()],
                value=None,
                ),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H3("Create New Budget"), 
                html.P("Enter Budget Name", className="col_question_label"),
                dbc.Input(
                    id="balance_name", 
                    placeholder="Ex. Checkings", 
                    type="text",
                    class_name="col_input"
                    ),

                html.P("Enter Stored Amount", className="col_question_label"),
                dbc.Input(
                    id="balance_amount",
                    placeholder="Ex: 12800", 
                    type="text", 
                    class_name="col_input"
                    ),

                html.P("Enter Yield Percentage", className="col_question_label"),
                dbc.Input(
                    id="balance_yield_percentage", 
                    placeholder="Ex: 2%", 
                    type="text", 
                    class_name="col_input",
                    ),
                html.Button("Create Budget", id="create_balance_btn", className="col_create_btn"),
                ],

                class_name="tab2_column_top_row"
                ),


            dbc.Col([
                html.H3("Add Income Source"), 
                html.P("Enter Income Source Name", className="col_question_label"),
                dbc.Input(
                    id="income_name", 
                    placeholder="Ex. Salary", 
                    type="text",
                    class_name="col_input"
                    ),

                html.P("Enter Income Amount", className="col_question_label"),
                dbc.Input(
                    id="income_amount",
                    placeholder="Ex: 1700", 
                    type="text", 
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
                    id="expense_name", 
                    placeholder="Ex: Netflix", 
                    type="text", 
                    class_name="col_input"
                    ),
                html.P("Enter Expense Amount", className="col_question_label"),
                dbc.Input(
                    id="expense_amount", 
                    placeholder="Ex: 20", 
                    type="text", 
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
                    id="investment_name", 
                    placeholder="Ex: Apple Stock", 
                    type="text",
                    class_name="col_input"
                    ),

                html.P("Enter Investment Amount", className="col_question_label"),
                dbc.Input(
                    id="investment_amount", 
                    placeholder="Ex: 6500", 
                    type="text", 
                    class_name="col_input"
                    ),

                html.P("Enter Investment Yield Percentage", className="col_question_label"),
                dbc.Input(
                    id="investment_yield", 
                    placeholder="Ex: 4", 
                    type="text", 
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
            dbc.Col([html.Div(id="balance-output-div")],class_name="tab2_column_bottom_row"), # fill with created budget objects
            dbc.Col([html.Div(id="income-output-div")],class_name="tab2_column_bottom_row"), # fill with income objects
            dbc.Col([html.Div(id="expense-output-div")],class_name="tab2_column_bottom_row"), # fill with expense objects
            dbc.Col([html.Div(id="investment-output-div")],class_name="tab2_column_bottom_row") # fill with investment objects
        ])
    ])
])



""" The following functions take the add attribute prompts and insert them into the current budget DS"""



@app.callback(
    [Output("balance-output-div", "children"),
     Output("balance_name", "value"),
     Output("balance_amount", "value"),
     Output("balance_yield_percentage", "value")],
    [Input("budget-dropdown", "value"),
     Input("create_balance_btn", "n_clicks")],
    [State("balance_name", "value"),
     State("balance_amount", "value"),
     State("balance_yield_percentage", "value")]
)
def update_budget(value, n_clicks, name, amount, yield_percentage):
    """ Updates budget display elements """
    
    triggered_id = ctx.triggered_id
    if n_clicks:
        if triggered_id == "create_balance_btn":
            create_balance(name, amount, yield_percentage)
        if not name:
            name = value
        return [html.P(f"Budget: Name={created_budgets[name].name}, Amount={created_budgets[name].allocated_amount}, Frequency={created_budgets[name].yield_percentage}")], "", "", ""
    else:
        return [], "", "", ""
    

@app.callback(
    Output("balance-output-div", "children"),
    [Input("create_balance_btn", "n_clicks")],
    [State("balance_name", "value"),
     State("balance_amount", "value"),
     State("investment_yield_percentage", "value")]
)
def create_balance(name, amount, yield_percentage=None):
    """ Creates budget object and saves in currently created budgets cache """
    
    if name not in created_budgets:
        if name and amount and yield_percentage:
            created_budgets[name] =  Budget(name=name, allocated_amount=amount, yield_percentage=yield_percentage)


@app.callback(
    Output("budget-dropdown", "options"),
    [Input("create_balance_btn", "n_clicks"),
     Input("budget-dropdown", "value")],
     prevent_initial_call=True
)
def update_budget_dropdown(n_clicks, value):
    """ Updates budget dropdown menu """
    
    if n_clicks:
        options = [{"label": name, "value": name} for name in created_budgets.keys()]
        return options
    return []
    

@app.callback(
    [Output("expense-output-div", "children"),
     Output("expense_name", "value"),
     Output("expense_amount", "value"),
     Output("expense_freq", "value")],
    [Input("budget-dropdown", "value"),
     Input("create_expense_btn", "n_clicks")],
    [State("expense_name", "value"),
     State("expense_amount", "value"),
     State("expense_freq", "value")]
)
def update_expense(value, n_clicks, name, amount, frequency):
    """ Updates expense display elements """

    triggered_id = ctx.triggered_id
    if n_clicks:
        current_budget = created_budgets[value]
        if triggered_id == "create_expense_btn":
            create_expense(name, amount, frequency, current_budget)
        return [html.P(f"Expense: Name={obj.name}, Amount={obj.amount}, Frequency={obj.frequency}") for obj in current_budget.expenses], "", "", ""
    else:
        return [], "", "", ""

def create_expense(name, amount, frequency, current_budget):
    """ Creates and adds expense object to active budget """
    
    if name and frequency and amount:
        current_budget.add_expense(amount=amount, name=name, frequency=frequency, category="test")


@app.callback(
    [Output("income-output-div", "children"),
     Output("income_name", "value"),
     Output("income_amount", "value"),
     Output("income_freq", "value")],
    [Input("budget-dropdown", "value"),
     Input("create_income_btn", "n_clicks")],
    [State("income_name", "value"),
     State("income_amount", "value"),
     State("income_freq", "value")]
)
def update_income(value, n_clicks, name, amount, frequency):
    """ Updates income display elements """

    triggered_id = ctx.triggered_id
    if n_clicks:
        current_budget = created_budgets[value]
        if triggered_id == "create_income_btn":
            create_income(name, amount, frequency, current_budget)
    
        return [html.P(f"Income: Name={obj.source}, Amount={obj.amount}, Frequency={obj.frequency}") for obj in current_budget.incomes], "", "", ""
    else:
        return [], "", "", ""


def create_income(name, amount, frequency, current_budget):
    """ Creates and adds income object to active budget """
    
    if name and frequency and amount:
        current_budget.add_income(amount=amount, name=name, frequency=frequency, date="07-15-2022")


@app.callback(
    [Output("investment-output-div", "children"),
     Output("investment_name", "value"),
     Output("investment_amount", "value"),
     Output("investment_yield", "value"),
     Output("investment_freq", "value")],
    [Input("budget-dropdown", "value"),
     Input("create_investment_btn", "n_clicks")],
    [State("investment_name", "value"),
     State("investment_amount", "value"),
     State("investment_yield", "value"),
     State("investment_freq", "value"),]
)
def update_investments(value, n_clicks, name, amount, roi, roi_frequency, description=None, maturity_date=None):
    """ Updates investment display elements"""

    triggered_id = ctx.triggered_id

    if n_clicks:
        current_budget = created_budgets[value]
        print(current_budget.investments)
        if triggered_id == "create_investment_btn":
            create_investment(current_budget, name, amount, roi, roi_frequency, description=None, maturity_date=None)
    
        object_details = [
            html.P(f"Investment: Name={obj.name}, Amount={obj.amount}, roi={obj.roi}, "
                   f"roi_frequency={obj.roi_frequency}") for obj in current_budget.investments
        ]

        return object_details, "", "", "", ""
    else:
        return [], "", "", "", ""


def create_investment(current_budget, name, amount, roi, roi_frequency, description=None, maturity_date=None):
    """ Creates and adds investment object to active budget """
    
    if name and amount and roi and roi_frequency:
        current_budget.add_investment(name=name, amount = amount, roi=roi, roi_frequency=roi_frequency, description="test")



""" End of table insertion functions"""



# Renders page based on active tab selected
@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    """ Switches current tab and embdedded content """
    
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
    

if __name__ == "__main__":
    app.run_server(debug=False)
