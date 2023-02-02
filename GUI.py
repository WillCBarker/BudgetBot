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
f4 = px.line(x = projectedMoney[0], y = projectedMoney[1])

f1 = f1.to_dict()
f1['layout']['paper_bgcolor'] ='#96b8d9'
f1['layout']['plot_bgcolor'] = '#96b8d9'
f1['layout']['title'] = 'Expenses'

f2 = f2.to_dict()
f2['layout']['paper_bgcolor'] ='#96b8d9'
f2['layout']['plot_bgcolor'] = '#96b8d9'
f2['layout']['title'] = 'Balances'

f4 = f4.to_dict()
f4['layout']['paper_bgcolor'] ='#96b8d9'
f4['layout']['plot_bgcolor'] = '#96b8d9'
f4['layout']['title'] = 'Taxes'

f3 = f3.to_dict()
f3['layout']['paper_bgcolor'] ='#96b8d9'
f3['layout']['plot_bgcolor'] = '#96b8d9'
f3['layout']['title'] = 'Investments'

app = dash.Dash(__name__)

#dashboard layout using dash library (html & css)
app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="Header",
            style={
                "gridArea": "Header",
                "backgroundColor": '#96b8d9',
                "textAlign": "center",
                "height": "80px",
                "margin-bottom": '350px',
                'font-size': '40px'
                #"outline": "black solid 1px"
            },
            children="This is a financial dashboard",
        ),
        html.Div(
            className="Balances",
            style={
                "gridArea": "Balances",
                #"backgroundColor": "#e5fae3",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                #"outline": "black solid 1px"
            },
            children=[
        dcc.Graph(id='example-graph1', figure=f2,
            style = {'height': '400px', 'width': '655px', "textAlign": "center"})
    ],
        ),
        html.Div(
            className="Taxes",
            style={
                "gridArea": "Taxes",
                #"backgroundColor": "#e5fae3",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                #"outline": "black solid 1px"
            },
            children=[
        dcc.Graph(id='example-graph2', figure=f4,
            style = {'height': '400px', 'width': '655px', "textAlign": "center"})
    ],
        ),
        html.Div(
            className="Investments",
            style={
                "gridArea": "Investments",
                #"backgroundColor": "#e5fae3",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                #"outline": "black solid 1px"
            },
            children=[
        dcc.Graph(id='example-graph3', figure=f3,
            style = {'height': '390px', 'width': '655px', "textAlign": "center"})
    ],
        ),
        html.Div(
            className="Expenses",
            style={
                "gridArea": "Expenses",
                "backgroundColor": '#8dabc9',
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                #"outline": "black solid 1px"
            },
            children=[
        dcc.Graph(id='example-graph4', figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                     {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'},
                     ],
            'layout': {'paper_bgcolor': '#96b8d9',
                       'plot_bgcolor': '#96b8d9',
                       'title': 'Expenses',
                       },
        },
            style = {'height': '390px', 'width': '655px', "textAlign": "center"}
        )
    ],
        ),
        html.Div(
            className="Customize",
            style={
                "gridArea": "Customize",
                "backgroundColor": '#96b8d9',
                #"outline": "black solid 2px",
                "height": "804px",
                "margin-top": "-15px"
            },
            children=dcc.Slider(
                        id='slider',
                        min=0,
                        max=100,
                        step=5,
                        value=10
                    ),
        ),
    ],
    style={
        "display": "grid",
        "gridTemplateColumns": "1.20fr 1.20fr 1fr",
        "gridTemplateRows": "45px 355px 355px",
        "gap": "60px 20px",
        "padding": "10px",
        "gridAutoFlow": "row",
        "backgroundColor": '#7594b3 ',
        "gridTemplateAreas": '''"Header Header Header"
                                "Expenses Investments Customize"
                                "Balances Taxes Customize"''',
        "height": "96vh"
    },
)


current_year = datetime.now()

@app.callback(
    Output('example-graph1', 'figure'),
    Input('slider', 'value')
)

def update_Balances(value):
    if value < 1:
        value = 1      
    futureDay = current_year.replace(year=current_year.year + value)
    projectedMoney = x.projectMoney(futureDay)
    scaled_y = [y for y in projectedMoney[1]]
    scaled_x = [x for x in projectedMoney[0]]
    line = px.line(x=scaled_x, y = scaled_y)
    line.update_layout(xaxis_title='over {} year(s)'.format(value), yaxis_title="Money")  
    return line

if __name__ == "__main__":
    app.run_server(debug=True)
