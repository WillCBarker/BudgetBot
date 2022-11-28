#tracks cashflow, budget, subscriptions, etc.
#shows projections on where money will be at in a period of time, A "what if" scenario
    #Describes where money will be at, what took the largest chunk between present date and set future date
#shows dashboard of all information

'''
******TO DO******
1. compound interest addition later on
2. USE PLOTLY, mutliple charts on single page capability
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
        return self.__moneyIn - self.getTotalBudget()





x = budget()
x.setFood(500)
x.setInsurance(79)
x.setMoneyIn(750)
print("Costliest: ", x.getCostliestCategory())
print("total Budget: ", x.getTotalBudget())
print("Disc Income: ", x.getDiscretionaryIncome())