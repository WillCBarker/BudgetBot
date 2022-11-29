#tracks cashflow, budget, subscriptions, etc.
#shows projections on where money will be at in a period of time, A "what if" scenario
    #Describes where money will be at, what took the largest chunk between present date and set future date
#shows dashboard of all information

from datetime import datetime
from dateutil import relativedelta


'''
******TO DO******
1. compound interest addition later on
2. USE PLOTLY, mutliple charts on single page capability
3. Tax calculations, Scrape from web
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
        self.__container = {'housing': self.__housing, 'food': self.__food, 'transportation': self.__transportation, 
                            'insurance': self.__insurance, 'medical': self.__medical, 'utilities': self.__utilities, 
                            'investments': self.__investments, 'recreational': self.__recreational}

    def setMoneyIn(self, newMoneyIn):
        self.__moneyIn = newMoneyIn
    
    def setMoneyOut(self, newMoneyOut):
        self.__moneyOut = newMoneyOut

    def setMoneyIdle(self, newMoneyIdle):
        self.__moneyIdle = newMoneyIdle

    def setHousing(self, newHousing):
        self.__housing = newHousing
        self.__container['housing'] = self.__housing

    def setFood(self, newFood):
        self.__food = newFood
        self.__container['food'] = self.__food

    def setTransportation(self, newTransportation):
        self.__transportation = newTransportation
        self.__container['transportation'] = self.__transportation

    def setInsurance(self, newInsurance):
        self.__insurance = newInsurance
        self.__container['insurance'] = self.__insurance

    def setMedical(self, newMedical):
        self.__medical = newMedical
        self.__container['medical'] = self.__medical

    def setUtilities(self, newUtilities):
        self.__utilities = newUtilities
        self.__container['utilities'] = self.__utilities

    def setInvestments(self, newInvestments):
        self.__investments = newInvestments
        self.__container['investments'] = self.__investments

    def setRecreational(self, newRecreational):
        self.__recreational = newRecreational
        self.__container['recreational'] = self.__recreational

    def getMoneyIn(self):
        return self.__moneyIn

    def getMoneyOut(self):
        return self.__moneyOut

    def getMoneyIdle(self):
        return self.__moneyIdle

    '''
    Methods directly associated with plotting below
    '''

    def getCostliestCategory(self):
        '''
        Returns most costly category of budget
        @return int
        '''
        return max(self.__container, key = self.__container.get) 


    def getTotalBudget(self):
        '''
        Returns sum of all categories in budget
        @return int
        '''
        return sum(self.__container.values())

    def getDiscretionaryIncome(self):
        '''
        Returns money available after all expenses paid
        @return int
        '''
        return self.netIncome() - self.getTotalBudget()

    def netIncome(self):
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

        return (self.__moneyIn * stateTax) - federalTax

    def projectMoney(self, date):
        '''
        Shows where money will be at input future date
        @return int
        '''
        monthDiff = self.monthDifference(date)
        moneyCompiled = self.getDiscretionaryIncome() * monthDiff
        return moneyCompiled


    def monthDifference(self, date):
        '''
        Uses datetime & relativedelta to find difference between 2 dates in months
        @return Int
        '''
        today = datetime.now().strftime('%Y-%m-%d')
        date = date.strftime('%Y-%m-%d')
        start_date = datetime.strptime(today, "%Y-%m-%d")
        end_date = datetime.strptime(date, "%Y-%m-%d")
        diff = relativedelta.relativedelta(end_date, start_date)
        return diff.months + (diff.years * 12)






x = budget()
x.setFood(500)
x.setInsurance(300)
x.setMoneyIn(95000)
print("Costliest: ", x.getCostliestCategory())
print("total Budget: ", x.getTotalBudget())
print("Disc Income: ", x.getDiscretionaryIncome())
futureDay = datetime(2024, 8, 30) #going to need time setting method for GUI
x.projectMoney(futureDay)