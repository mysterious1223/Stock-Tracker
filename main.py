

import requests
import json
import time
from datetime import datetime
#r = requests.get ("https://api.iextrading.com/1.0/ref-data/symbols")


#parsedinfo = json.loads (r.text)

#print (parsedinfo[0])


# we need to get the value for our symbols

# price = https://api.iextrading.com/1.0/stock/AMD/price



stock_curr = [
              {"symbol":"AMD", "name":"", "current_values":0, "Min-Val":30, "High-Val": 50},
              {"symbol":"T", "name":"", "current_values":0, "Min-Val":0, "High-Val": 50},
              {"symbol":"GE", "name":"", "current_values":0, "Min-Val":10, "High-Val": 14},
              {"symbol":"CARA", "name":"", "current_values":0, "Min-Val":0, "High-Val": 50}
              ]

timeout = 2

#print (stock_curr [0]["symbol"])




def init_stocks ():
    # set the name values up
    #print ("init")
    for s_dict in stock_curr:
        #print (get_name (s_dict["symbol"]) + ": " + str(get_value(s_dict["symbol"])))
        s_dict["name"] = get_name (s_dict["symbol"])
        s_dict["current_values"] = get_value (s_dict["symbol"])



def update_stock ():
    

    for s_dict in stock_curr:
        #print (get_name (s_dict["symbol"]) + ": " + str(get_value(s_dict["symbol"])))
        #print (s_dict["symbol"]+": " + str(get_value(s_dict["symbol"])))
        s_dict["current_values"] = get_value (s_dict["symbol"])


def query_url (url):
    
    info = ""
    try:
        r = requests.get (url)
        parsedinfo = json.loads (r.text)
        info = parsedinfo
    except:
        print ("Failed to collect information on "+url)
        info = -1
    return info

def get_name (sym):
    #https://api.iextrading.com/1.0/ref-data/symbols
    
    # get all symbols
    indices = query_url ("https://api.iextrading.com/1.0/ref-data/symbols")
    
    for i in indices:
        #print (i["symbol"])
        if (i['symbol'] == sym):
            #print (i['name'])
            return i ['name']
    return -1

def debug_print_stock_info():
    
    
    
    for s_dict in stock_curr:
        #print (get_name (s_dict["symbol"]) + ": " + str(get_value(s_dict["symbol"])))
        print ("["+str(datetime.now())+"] :"+s_dict["symbol"] + ": " + str(s_dict["current_values"]))
        
        with open ("log.log", "a") as log:
            log.write("["+str(datetime.now())+"] :"+s_dict["symbol"] + ": " + str(s_dict["current_values"]) + "\n")

    with open ("log.log", "a") as log:
        log.write("\n")
    print ("\n")

def get_value(sym):
    #https://api.iextrading.com/1.0/ref-data/symbols
    
    # get all symbols
    value = query_url ("https://api.iextrading.com/1.0/stock/"+sym+"/price")
    
    if value == -1 :
        print ("Failed to get value")
        return -1
    else:
        return value
def start_monitor ():
    print ("starting stock montitor...\n")
    init_stocks()
    print ("init done!\n")
    
    debug_print_stock_info()
    while True:
        time.sleep (timeout)
        update_stock()
        debug_print_stock_info()


def main ():
#update_stock()
    start_monitor()
#get_value("AMD")
if __name__ == "__main__":
    main()

