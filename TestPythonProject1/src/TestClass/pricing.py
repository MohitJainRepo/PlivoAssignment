from util.PlivoService import PlivoService
from util.RequestGenerator import RequestGenerator

class pricing:
    def getPricing(self):
        queryparams =[]
        service = PlivoService()
        req = RequestGenerator()
        queryparams.append('MAODUZYTQ0Y2FMYJBLOW')
        queryparams.append('US')
        apiName = 'getPricing'
        headers = {'Authorization': 'Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ=='} 
        URL,RequestMethod,Payload = service.PlivoService_onlyQueryParams(apiName, queryparams)
        r= req.RequestGenerator(RequestMethod,URL,headers,Payload)
        if not r:
            return r
        response_service=r.json()
        outbound_rate = response_service['message']['outbound']['rate']
        return (outbound_rate)