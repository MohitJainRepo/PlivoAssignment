from util.PlivoService import PlivoService
from util.RequestGenerator import RequestGenerator

class numbers:
    
    def getNumbers(self):
        queryparams =[]
        service = PlivoService()
        req = RequestGenerator()
        queryparams.append('MAODUZYTQ0Y2FMYJBLOW')
        apiName = 'getAllNumbers'
        headers = {'Authorization': 'Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ=='}
        URL,RequestMethod,Payload = service.PlivoService_onlyQueryParams(apiName, queryparams)
        r = req.RequestGenerator(RequestMethod,URL,headers,Payload)
        if not r:
            return r
        response_service = r.json()
        number1 = response_service['objects'][0]['number']
        number2 = response_service['objects'][2]['number']
        return (number1,number2)