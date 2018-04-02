from util.PlivoService import PlivoService
from util.RequestGenerator import RequestGenerator

class message:
    
    def sendMessage(self,number1,number2):
        payloadparams=[]
        service = PlivoService()
        req = RequestGenerator()
        payloadparams.append(number1)
        payloadparams.append(number2)
        payloadparams.append("'Hi Plivo'")
        queryparams =[]
        queryparams.append('MAODUZYTQ0Y2FMYJBLOW')
        apiName = 'sendMessage'
        headers = {'Authorization': 'Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ=='}
        URL,RequestMethod,Payload = service.PlivoService_bothQueryAndPayloadParams(apiName, queryparams,payloadparams)
        r= req.RequestGenerator(RequestMethod,URL,headers,Payload)
        if not r:
            return r
        response_service=r.json()
        message_uid = response_service['message_uuid']
        return message_uid[0]
    
    def getMessageDetails(self,message_id):
        queryparams =[]
        service = PlivoService()
        req = RequestGenerator()
        queryparams.append('MAODUZYTQ0Y2FMYJBLOW')
        queryparams.append(message_id)
        apiName = 'getMessageDetail'
        headers = {'Authorization': 'Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ=='}
        URL,RequestMethod,Payload = service.PlivoService_onlyQueryParams(apiName, queryparams)
        r= req.RequestGenerator(RequestMethod,URL,headers,Payload)
        if not r:
            return r
        response_service=r.json()
        total_amount = response_service['total_amount']
        total_rate = response_service['total_rate']
        return(total_amount,total_rate)