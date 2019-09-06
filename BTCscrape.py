def main():
    '''
    Main function for the BTC Scrape project
    '''

    from urllib import request
    import json
    from datetime import datetime
    import sqlite3
    import time

    url =  "https://api.coindesk.com/v1/bpi/currentprice/GBP.json"
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    req = request.Request(url, headers=header)

    for i in range(100):

        with request.urlopen(req) as data:
            jdata = json.load(data)

            dt = jdata['time']['updateduk']
            dt = datetime.strptime(dt, '%b %d, %Y at %H:%M BST')
            #see the strftime documentation for what each symbolset means
            #Neater would be to wrap the grab inside the strptime call to do it in one line
        
            curr = 'GBP'
            rate = jdata['bpi']['GBP']['rate_float']

        conn = sqlite3.connect(r'C:\Projects\BTCscrape\crypto.db')
    
        c = conn.cursor()

        c.execute('insert into BTC (pricedate, currency, rate) values (?, ?, ?)',(dt, curr, rate))
        conn.commit()
        conn.close()

        time.sleep(60)

if __name__ == '__main__':
    main()
    #Runs our main function
