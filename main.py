import requests
import json
import sys

try:
    n=len(sys.argv)
    passed_argument=sys.argv[1]
    try:
        response = requests.get('https://bg.annapurnapost.com/api/tags/news?per_page=20&tag='+ str(passed_argument))
        pages=response.json()['totalPage']
        print('Total Pages'+str(pages))
        result=[]
        for page in range(1,int(pages)+1):

            response_per_page=requests.get('https://bg.annapurnapost.com/api/tags/news?page='+str(page)+'&per_page=20&tag='+str(passed_argument))

            result.append(response_per_page.json()['data'])

        if not result:
            exit()
        print(result)
        json_string = json.dumps(result)
        print('JSON object')
        print(json_string)
    except:
        print("No such news found")
except:
    print("No arguments passed")

