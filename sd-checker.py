import requests
import sys
import os
import signal

from datetime import datetime

def banner():
    print(B+ """
      _____ ___             __  __ __    ___    __  __  _    ___  ____   
     / ___/|   \           /  ]|  |  |  /  _]  /  ]|  |/ ]  /  _]|    \  
    (   \_ |    \  _____  /  / |  |  | /  [_  /  / |  ' /  /  [_ |  D  ) 
     \__  ||  D  ||     |/  /  |  _  ||    _]/  /  |    \ |    _]|    /  
     /  \ ||     ||_____/   \_ |  |  ||   [_/   \_ |     \|   [_ |    \  
     \    ||     |      \     ||  |  ||     \     ||  .  ||     ||  .  \ 
      \___||_____|       \____||__|__||_____|\____||__|\_||_____||__|\_|

                                  By: sh3r1
    """ + B)


# Console Colors based from https://github.com/aboul3la/Sublist3r
# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''

else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def error_parse(error):
    banner()
    print("Usage: python " + sys.argv[0] )
    print("Error: " + error)
    sys.exit()

    
def main():
    
    banner()
    
    # first argument - text file for subdomain
    # ex: subdomain.txt
    file = sys.argv[1]
    with open(file) as f:
        for line in f:
            #try:
            response('http://',line.strip())
            #except:
                #response('https://',line.strip())
    
                

def response(schema,subdomain):
    try:
        url = schema + subdomain
        res = requests.get(url,verify=True)
        print(G + '[' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '] - ' + url + ' = ' + str(res.status_code) + G)
    except :
        print(R + '[' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '] - ' + url + ' = Not Found'  + R)
        #urls = 'https://' + subdomain
        #ress = requests.get(urls,verify=True)
        #print(Y + urls + Y)
        #print(G + '[' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '] - ' + urls + ' = ' + str(ress.status_code) + G)
    
    
   
    

if __name__ == '__main__':
    main()
