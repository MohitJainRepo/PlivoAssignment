from TestClass.numbers import numbers
from TestClass.message import message
from TestClass.pricing import pricing
from TestClass.account import account

class tests:
    def test_validateScenario(self):
    
        acc = account()
        initial_cash_credits = acc.getAccountDetails()
        print('Initial cash credit : ' + initial_cash_credits)
        #if float(initial_cash_credits) <=0 or initial_cash_credits == 'False':
        #   return False
                        
        num = numbers()
        number1,number2 = num.getNumbers()
        print('source number : '+number1)
        print('destination number : '+number2)
                
        msg = message()
        message_id = msg.sendMessage(number1, number2)
        print('message id : '+message_id)
        if not message_id:
            return False
                
        total_amount,total_rate = msg.getMessageDetails(message_id)
        print('total amount : '+total_amount)
        print('total rate : ' +total_rate)
                
        price = pricing()
        outbound_rate = price.getPricing()
        print('outbound rate : '+outbound_rate)
        
        #if not outbound_rate == total_amount:
        #    return False
        
        #if not outbound_rate == total_rate:
        #    return False
                         
        acc = account()
        final_cash_credits = acc.getAccountDetails()
        print('Final cash credit : '+final_cash_credits)
                
        available_balance = float(initial_cash_credits) - float(total_rate);
        print('available balance after sending SMS : ' + str(available_balance))
        
        if not float(available_balance) == float(final_cash_credits):
            return False    

        return True
       
test=tests()     
result=test.test_validateScenario()
if result == False:
    print('Test Case Failed')
elif result == True:
    print('Test Case Passed')
        