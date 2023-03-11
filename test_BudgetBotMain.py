from BudgetBotMain import budget
import unittest
from datetime import datetime

class testBudget(unittest.TestCase):
    def __init__(self):
        #Create mock budget object for testing
        self.newBudget = budget()
        self.newBudget.setMoneyIn(100000)
        self.newBudget.setMoneyOut(2000)
        self.newBudget.setMoneyIdle(3000)
        self.newBudget.setHousing(1200)
        self.newBudget.setFood(250)
        self.newBudget.setTransportation(180)
        self.newBudget.setInsurance(199)
        self.newBudget.setUtilities(320)
        self.newBudget.setInvestments(5000)
        self.newBudget.setRecreational(700)

    def test_getTotalBudget(self):
        assert self.newBudget.getTotalBudget() == 7849

    def test_getTax(self):
        stateTax, fedTax = self.newBudget.getTax()
        assert stateTax == 0.9425
        assert fedTax == 12231.5
    
    def test_netIncome(self):
        assert self.newBudget.netIncome() == 82018.5

    def test_getDiscretionaryIncome(self):
        assert self.newBudget.getDiscretionaryIncome() == 74169.5

    def test_monthDifference(self):
        test_date = datetime(2067, 8, 3)
        assert self.newBudget.monthDifference(test_date) == 532

    def test_compoundInterest(self):
        percentGrowth = 7
        end_date = datetime(2044, 12, 25)
        profit = self.newBudget.compoundInterest(end_date, percentGrowth)[1][-1]
        assert profit == 245028.72

    def test_projectMoney(self):
        end_date = datetime(2050, 4, 19)
        assert self.newBudget.projectMoney(end_date)[1][-1] == 2002576.5


if __name__ == "__main__":
    test = testBudget()
    test.test_getTotalBudget()
    test.test_getTax()
    test.test_netIncome()
    test.test_getDiscretionaryIncome()
    test.test_monthDifference()
    test.test_compoundInterest()
    test.test_projectMoney()