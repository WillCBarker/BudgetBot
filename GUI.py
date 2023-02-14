import plotly.express as px
import BudgetBotMain as bb
from datetime import datetime
from dateutil import relativedelta
#Above imports are pre-dash editing
import dash
from dash import Dash, dcc, html, Input, Output


#Random info for testing
x = bb.budget()
x.setFood(500)
x.setInvestments(900)
x.setInsurance(300)
x.setMoneyIn(95000)
print("Costliest: ", x.getCostliestCategory())
print("total Budget: ", x.getTotalBudget())
print("Disc Income: ", x.getDiscretionaryIncome())
futureDay = datetime(2024, 8, 30) #going to need time setting method for GUI
futureDay2 = datetime(2060, 8, 30)
x.setHousing(1200)

#Gathering info from main
container = x.getExpenseContainer()
projectedMoney = x.projectMoney(futureDay)
compoundInterest = x.compoundInterest(futureDay2, 8)

#Creating plots
f1 = px.bar(x = container['expenseNames'], y = container['expenses'])
f2 = px.line(x = projectedMoney[0], y = projectedMoney[1])
f3 = px.line(x = compoundInterest[0], y = compoundInterest[1])
f4 = px.line(x = compoundInterest[0], y = compoundInterest[1])


f1 = f1.to_dict()
f1['layout']['title'] = 'Expenses'

f2 = f2.to_dict()
f2['layout']['title'] = 'Balances'

f3 = f3.to_dict()
f3['layout']['title'] = 'Expenses Compounded'

f4 = f4.to_dict()
f4['layout']['title'] = 'Investments'

app = dash.Dash(__name__)

#dashboard layout using dash library (html & css)
app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="Header",
            style={
                "gridArea": "Header",
                "backgroundColor": '#FFFFFF',
                "height": "80px",
                "textAlign": "center",
                "marginBottom": '5px',
                "margin" : "0",
                'fontSize': '40px',
                "font-family": "Copperplate, sans-serif",
                "font-weight": "bold"
            },
            children="Budget Bot V0.1",
        ),
        html.Div(
            className="Expenses",
            style={
                "gridArea": "Expenses",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "marginTop": "5px",
            },
            children=[
                    dcc.Graph(id='example-graph1', figure=f1,
                    style = {'height': '390px', 'width': '655px', "textAlign": "center"})
                    ],
        ),
        html.Div(
            className="Expenses Compounded",
            style={
                "gridArea": "ExpensesCompounded",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "marginTop": "5px"
            },
            children=[
                    dcc.Graph(id='example-graph2', figure=f3,
                    style = {'height': '390px', 'width': '655px', "textAlign": "center"})
                    ]
            ,
        ),
        html.Div(
            className="Balance Over Time",
            style={
                "gridArea": "Balances",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
            },
            children=[
                    dcc.Graph(id='example-graph3', figure=f2,
                    style = {'height': '400px', 'width': '655px', "textAlign": "center"})
                    ],
        ),
        html.Div(
            className="Investments",
            style={
                "gridArea": "Investments",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
            },
            children=[
                    dcc.Graph(id='example-graph4', figure=f4,
                    style = {'height': '390px', 'width': '655px', "textAlign": "center"})
                    ],
        ),
        html.Div(
            className="Customize",
            style={
                "gridArea": "Customize",
                "backgroundColor": '#FFFFFF',
                "height": "808px",
                "marginTop": "-15px",
                "textAlign": "center"
            },
            children= [html.Div(
                        style = {
                                "marginTop": "20px",
                                "marginBottom": "20px"
                        },
                        children = ["Years of Compounding Balance", 
                                    dcc.Slider(
                                        id='slider',
                                        min=0,
                                        max=100,
                                        step=5,
                                        value=10
                                        )
                                    ]
                                ),
                        html.Div(
                        style = {
                                "marginBottom": "20px"
                        },
                        children = ["Years of Compounding Expense", 
                                    dcc.Slider(
                                        id='slider1',
                                        min=0,
                                        max=100,
                                        step=5,
                                        value=10
                                        )
                                    ]
                                ),
                        html.Div(
                        style = {
                                "marginBottom": "20px"
                        },
                        children = ["Years of Compounding Investment", 
                                    dcc.Slider(
                                        id='slider2',
                                        min=0,
                                        max=100,
                                        step=5,
                                        value=10
                                        )
                                    ]
                                ),
                        ]
                ),
    ],
    style={
        "display": "grid",
        "gridTemplateColumns": "1.20fr 1.20fr 1fr",
        "gridTemplateRows": "45px 355px 355px",
        "gap": "60px 20px",
        "padding": "10px",
        "gridAutoFlow": "row",
        "backgroundColor": '#d9ebfc',
        "gridTemplateAreas": '''"Header Header Header"
                                "Expenses ExpensesCompounded Customize"
                                "Balances Investments Customize"''',
        "height": "97.9vh"
    },
)


current_year = datetime.now()

@app.callback(
    Output('example-graph3', 'figure'),
    Input('slider', 'value'),
)

def update_Balances(value):
    '''
    Updates Balance Over Time chart, scaling money along with input time frame
    '''
    if value < 1:
        value = 1      
    futureDay = current_year.replace(year=current_year.year + value)
    projectedMoney = x.projectMoney(futureDay)
    scaled_y = [y for y in projectedMoney[1]]
    scaled_x = [x for x in projectedMoney[0]]
    line = px.line(x=scaled_x, y = scaled_y)
    line.update_layout(xaxis_title='over {} year(s)'.format(value), yaxis_title="Money", title="Balance Over Time")  
    return line


@app.callback(
    Output('example-graph4', 'figure'),
    Input('slider2', 'value'),
)

def update_Investments(value):
    '''
    Updates Investments Over Time chart, scaling money along with input time frame
    '''
    futureDay = current_year.replace(year=current_year.year + value)
    compoundedMoney = x.compoundInterest(futureDay, 6)
    scaled_y = [y for y in compoundedMoney[1]]
    scaled_x = [x for x in compoundedMoney[0]]
    line = px.line(x=scaled_x, y = scaled_y)
    line.update_layout(xaxis_title='over {} year(s)'.format(value), yaxis_title="Money", title="Investments Over Time") 
    return line

#For update_Expenses_Compounted, use the get total Budget and iterate through, adding each total budget calculation at that respective years x value
@app.callback(
    Output('example-graph2', 'figure'),
    Input('slider1', 'value'),
)

def update_Compounding_Expenses(value):
    '''
    Updates Expenses Over Time chart, scaling money along with input time frame
    '''
    scaled_x = []
    scaled_y = []
    for year in range(1, value + 1):
        scaled_y.append((year * x.getTotalBudget()) * 12)
        scaled_x.append(year)
    line = px.line(x=scaled_x, y = scaled_y)
    line.update_layout(xaxis_title='over {} year(s)'.format(value), yaxis_title="Money", title="Expenses Compounded Over Time") 
    return line

if __name__ == "__main__":
    app.run_server(debug=True)
