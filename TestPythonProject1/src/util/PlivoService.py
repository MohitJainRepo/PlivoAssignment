import xmltodict
from Payloads.fetchPayload import fetchFile
import os

class PlivoService:
    
    def readAPIConfig(self,apiName):
        path = os.path.relpath('..\\Data\environment.xml')
        with open(path) as fd:
            doc = xmltodict.parse(fd.read())
            url = None
        for api in doc['services']['api']:
            if api['@name'] == apiName:
                url = api['url']
                requestmethod=api['requestmethod']
                payloadrequired=api['payloadrequired']
                queryparamsrequired=api['queryparamsrequired']
                break
        return(url,requestmethod,payloadrequired,queryparamsrequired)

    def loadAPIDetails(self,apiName):
        url,requestmethod,payloadrequired,queryparamsrequired = self.readAPIConfig(apiName)
        return(url,requestmethod,payloadrequired,queryparamsrequired)
    
    def loadPayloadDetails(self,apiName,payloadParams):
        fetchobj =fetchFile()
        payload = fetchobj.setParams(apiName,payloadParams)
        return(payload)
    
    def PlivoService_bothQueryAndPayloadParams(self,apiName,queryParams=[],payloadParams=[],*args):
        url,requestmethod,payloadrequired,queryparamsrequired = PlivoService.loadAPIDetails(self,apiName)
        RequestMethod=requestmethod
        if (queryparamsrequired == 'true'):
            URL = url.format(*queryParams)
        if (payloadrequired == 'true'):
            Payload = PlivoService.loadPayloadDetails(self,apiName,payloadParams)
        return URL,RequestMethod,Payload
            
    def PlivoService_onlyQueryParams (self,apiName,queryParams=[],*args):
        url,requestmethod,payloadrequired,queryparamsrequired = PlivoService.loadAPIDetails(self,apiName)
        RequestMethod=requestmethod
        URL = url.format(*queryParams)
        Payload = None
        return URL,RequestMethod,Payload
             
    def PlivoService_onlyPayloadParams(self,apiName,payloadParams):
        url,requestmethod,payloadrequired,queryparamsrequired = PlivoService.loadAPIDetails(apiName)
        RequestMethod=requestmethod
        URL=url
        Payload = PlivoService.loadPayloadDetails(self,apiName,payloadParams)
        return URL,RequestMethod,Payload
            