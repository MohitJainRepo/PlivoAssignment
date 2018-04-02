
class fetchFile :
    
    msgFormat={}
    
    def __init__(self):
        self.setParamFormat()
    
    def setParamFormat(self):
        self.msgFormat['sendMessage']=['src', 'dst', 'text']
        
    def getParamFormat(self,key):
        if key not in self.msgFormat.keys():
            return False
        else:
            return self.msgFormat[key]
            
    def setParams (self,apiName,payloadparams):
        dictop={}
        for k,v in enumerate(self.getParamFormat(apiName)):
            dictop[v]=payloadparams[k]
        return dictop

# Unit Testing of fetchFile Class    
if __name__=='__main__':
    fetchobj=fetchFile()
    #print(fetchobj.msgFormat)
    payloadParams=[999, 888, 'Hi Plivo']
    apiName='sendMessage'
    payload = fetchobj.fetchFile(apiName,payloadParams)
    print(payload)