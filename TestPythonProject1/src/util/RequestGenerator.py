import requests

class RequestGenerator:
    def RequestGenerator(self,RequestMethod,URL,headers,Payload,timeout=2):
        if(RequestMethod =='GET'):
            try:
                return(requests.get(URL,headers=headers))
            except ConnectionError:
                print(TimeoutError)
            except:
                print("unknown exception")
                return False
    
        elif(RequestMethod =='POST'):
            try:
                return(requests.post(URL,headers=headers,data=Payload))
            except ConnectionError:
                print(TimeoutError)
            except:
                print("unknown exception")
                return False
            
        elif(RequestMethod =='PUT'):
            #To Implement
            return 
        
        elif(RequestMethod =='DELETE'):
            #To Implement
            return
        
        else:
            assert False,("Invalid RequestMethod Type")