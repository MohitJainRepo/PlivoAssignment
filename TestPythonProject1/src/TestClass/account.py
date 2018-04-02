from util.PlivoService import PlivoService
from util.RequestGenerator import RequestGenerator

class account:
    def getAccountDetails(self):
        queryparams =[]
        service = PlivoService()
        req = RequestGenerator()  
        queryparams.append('MAODUZYTQ0Y2FMYJBLOW')
        apiName = 'getAccountDetails'
        headers = {'Authorization': 'Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ=='} 
        URL,RequestMethod,Payload = service.PlivoService_onlyQueryParams(apiName, queryparams)
        r= req.RequestGenerator(RequestMethod,URL,headers,Payload)
        if not r:
            return r
        response_service=r.json()
        cash_credits = response_service['cash_credits']
        return (cash_credits)