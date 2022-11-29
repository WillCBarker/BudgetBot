import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import BudgetBotMain as bb

import pandas as pd

from datetime import datetime


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

#Creating subblot layout
page = make_subplots(rows=2, cols=2, subplot_titles=('Budget Categories','Projected Money Monthly','Compound Interest Annually' ))

#Gathering info from main
container = x.getExpenseContainer()
projectedMoney = x.projectMoney(futureDay)
compoundInterest = x.compoundInterest(futureDay2, 8)

#Creating plots
f1 = go.Bar(x = container['expenseNames'], y = container['expenses'])
f2 = go.Line(x = projectedMoney[0], y = projectedMoney[1])
f3 = go.Line(x = compoundInterest[0], y = compoundInterest[1])

#Assigning created plots to subplots
page.add_trace(f1, row=1, col=1)
page.add_trace(f2, row=1, col=2)
page.add_trace(f3, row=2, col=1)

#Displaying subplots
page.show()

