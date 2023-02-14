#tracks cashflow, budget, subscriptions, etc.
#shows projections on where money will be at in a period of time, A "what if" scenario
    #Describes where money will be at, what took the largest chunk between present date and set future date
#shows dashboard of all information

from datetime import datetime
from dateutil import relativedelta
from dash import Dash, dcc, html

'''
Ideas:
    - "What if" scenarios, investing in certain stocks, predict yield over time using api pulled avg 20 yr gain for ex.
    - Initial questionaire using pyqt
'''


class budget():
    def __init__(self):
        self.__housing = 0
        self.__food = 0
        self.__transportation = 0
        self.__insurance = 0
        self.__medical = 0
        self.__utilities = 0
        self.__investments = 0
        self.__recreational = 0
        self.__moneyIn = 0
        self.__moneyOut = 0
        self.__moneyIdle = 0
        self.__expenseContainer = {'expenseNames': ['housing', 'food', 'transportation', 'insurance', 'medical', 'utilities', 'investments', 'recreational'],
                                    'expenses' : [self.__housing, self.__food,  self.__transportation, 
                                                    self.__insurance, self.__medical,  self.__utilities, 
                                                    self.__investments, self.__recreational]}

    def setMoneyIn(self, newMoneyIn):
        self.__moneyIn = newMoneyIn
    
    def setMoneyOut(self, newMoneyOut):
        self.__moneyOut = newMoneyOut

    def setMoneyIdle(self, newMoneyIdle):
        self.__moneyIdle = newMoneyIdle

    def setHousing(self, newHousing):
        self.__housing = newHousing
        self.__expenseContainer['expenses'][0] = self.__housing

    def setFood(self, newFood):
        self.__food = newFood
        self.__expenseContainer['expenses'][1] = self.__food

    def setTransportation(self, newTransportation):
        self.__transportation = newTransportation
        self.__expenseContainer['expenses'][2] = self.__transportation

    def setInsurance(self, newInsurance):
        self.__insurance = newInsurance
        self.__expenseContainer['expenses'][3] = self.__insurance

    def setMedical(self, newMedical):
        self.__medical = newMedical
        self.__expenseContainer['expenses'][4] = self.__medical

    def setUtilities(self, newUtilities):
        self.__utilities = newUtilities
        self.__expenseContainer['expenses'][5] = self.__utilities

    def setInvestments(self, newInvestments):
        self.__investments = newInvestments
        self.__expenseContainer['expenses'][6] = self.__investments

    def setRecreational(self, newRecreational):
        self.__recreational = newRecreational
        self.__expenseContainer['expenses'][7] = self.__recreational

    def getMoneyIn(self):
        return self.__moneyIn

    def getMoneyOut(self):
        return self.__moneyOut

    def getMoneyIdle(self):
        return self.__moneyIdle

    def getExpenseContainer(self):
        return self.__expenseContainer

    '''
    Methods directly associated with plotting below
    '''

    def getCostliestCategory(self):
        '''
        Returns most costly category of budget
        @return int
        '''
        maxIndex = self.__expenseContainer['expenses'].index(max(self.__expenseContainer['expenses']))
        return self.__expenseContainer['expenseNames'][maxIndex]


    def getTotalBudget(self):
        '''
        Returns sum of all categories in budget
        @return int
        '''
        return sum(self.__expenseContainer['expenses'])

    def getDiscretionaryIncome(self):
        '''
        Returns money available after all expenses paid
        @return int
        '''
        return self.netIncome() - self.getTotalBudget()

    def getTax(self):
        '''
        Calculates state and federal income tax rate given income.
        Notes:
            -State tax based on Virginia only 
            -Federal tax based assumes single filing
        @return int
        '''
        #State Tax brackets
        if self.__moneyIn <= 3000: stateTax = 0.98
        elif self.__moneyIn <= 50000: stateTax = 0.97
        elif self.__moneyIn <= 17000: stateTax = 0.95
        else: stateTax = 0.9425

        #Federal Tax brackets
        if self.__moneyIn <= 10275: federalTax = 0.10 * self.__moneyIn
        elif self.__moneyIn <= 10276: federalTax = 1027.50 + (0.12 * (self.__moneyIn - 10275))
        elif self.__moneyIn <= 41776: federalTax = 4807.50 + (0.22 * (self.__moneyIn - 41775))
        elif self.__moneyIn <= 89076: federalTax = 15213.50 + (0.24 * (self.__moneyIn - 89075))
        elif self.__moneyIn <= 170051: federalTax = 34647.50 + (0.32 * (self.__moneyIn - 170050))
        elif self.__moneyIn <= 215951: federalTax = 49335.50 + (0.35 * (self.__moneyIn - 215950))
        else: federalTax = 162718 + (0.37 * (self.__moneyIn - 539900))

        return stateTax, federalTax

    def netIncome(self):
        '''
        Calculates income after tax
        @return int
        '''
        stateTax, federalTax = self.getTax()
        return (self.__moneyIn * stateTax) - federalTax

    def projectMoney(self, date):
        '''
        Shows where money will be at input future date based on budget, returning 2 lists - 1. monthly/yearly balance, 2. month/year count
        @return list
        '''
        timeDiff = self.monthDifference(date)
        if timeDiff > 12:
            #if date is over 1 year in the future, plot by year instead of month
            timeDiff = round(timeDiff/12) + 1
            start = 1
        else:
            #A year and under, plots the single year since data is incremented by year
            timeDiff = 2
            start = 0

        balance = []
        count = []
        for i in range(start, timeDiff):
            balance.append(i*self.getDiscretionaryIncome())
            count.append(i)
        return [count, balance]


    def monthDifference(self, date):
        '''
        Uses datetime & relativedelta to find difference between 2 dates in months
        @return int
        '''
        today = datetime.now().strftime('%Y-%m-%d')
        date = date.strftime('%Y-%m-%d')
        start_date = datetime.strptime(today, "%Y-%m-%d")
        end_date = datetime.strptime(date, "%Y-%m-%d")
        diff = relativedelta.relativedelta(end_date, start_date)
        return diff.months + (diff.years * 12)

    def compoundInterest(self, end_date, percentGrowth):
        '''
        Calculates compound interest based on input time frame and yield
        @return list
        '''
        profit = self.__investments
        percentGrowth = percentGrowth/100
        yearDiff = self.monthDifference(end_date)//12
        profitTrack = []
        yearCount = []
        for i in range(yearDiff):
            profit = profit * (1 + percentGrowth) + self.__investments
            profitTrack.append(profit)
            yearCount.append(i)
        return [yearCount, profitTrack]

''' --Test Code
x = budget()
x.setFood(500)
x.setInsurance(300)
x.setMoneyIn(95000)
print("Costliest: ", x.getCostliestCategory())
print("total Budget: ", x.getTotalBudget())
print("Disc Income: ", x.getDiscretionaryIncome())
futureDay = datetime(2024, 8, 30) #going to need time setting method for GUI
x.projectMoney(futureDay)
'''
