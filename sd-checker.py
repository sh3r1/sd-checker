import requests
import sys
import os
import signal

   
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("+  _____ ___             __  __ __    ___    __  __  _    ___  ____   + ")
print("+ / ___/|   \           /  ]|  |  |  /  _]  /  ]|  |/ ]  /  _]|    \  + ")
print("+(   \_ |    \  _____  /  / |  |  | /  [_  /  / |  ' /  /  [_ |  D  ) + ")
print("+ \__  ||  D  ||     |/  /  |  _  ||    _]/  /  |    \ |    _]|    /  + ")
print("+ /  \ ||     ||_____/   \_ |  |  ||   [_/   \_ |     \|   [_ |    \  + ")
print("+ \    ||     |      \     ||  |  ||     \     ||  .  ||     ||  .  \ + ")
print("+  \___||_____|       \____||__|__||_____|\____||__|\_||_____||__|\_| + ")
print("+                  ------------ By. sh3r1 ---------------             + ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, sd-checker requires Python 3.x\n")
    sys.exit(1)
    
def main():

    try:
        # first argument - text file for subdomain
        # ex: subdomain.txt
        file = sys.argv[1]
     
        with open(file) as f:
            for line in f:
                try:
                    response('http://',line.strip())
                    
                except:
                    print("Trying https..")
                    response('https://',line.strip())
    except KeyboardInterrupt:
        sys.exit(0)
            
                

def response(schema,subdomain):

    
    if(schema == 'http'):
        url = schema + subdomain
        res = requests.get(url,verify=True)
        print(url + ' = ' + str(res.status_code))
        print("")
    else:
        try:
            url = schema + subdomain
            res = requests.get(url,verify=True)
            print(url + ' = ' + str(res.status_code))
            print("")
        except:
            print(url + ' = not found')
            print("")
    

if __name__ == '__main__':
    #try:
        main()
    #except KeyboardInterrupt:
       # sys.exit(0)

        
        
     
