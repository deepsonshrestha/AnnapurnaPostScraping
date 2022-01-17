import requests
import json
import sys

#added for Devanagari support
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


try:
    n=len(sys.argv)
    passed_argument=sys.argv[1]
    try:
        # response = requests.get('https://bg.annapurnapost.com/api/tags/news?per_page=20&tag='+ str(passed_argument))
        # pages=response.json()['totalPage']
        # print('Total Pages'+str(pages))
        result=[]
        # p=3

        # for page in range(1,int(p)+1):
        #     response_per_page=requests.get('https://bg.annapurnapost.com/api/tags/news?page='+str(page)+'&per_page=20&tag='+ str(passed_argument))
        #     result.append(response_per_page.json()['data'])
        #     p=response_per_page.json()['totalPage']
        #     print(p)

        page=1
        numberOfArticles=0
        while numberOfArticles <= 30:
            try:

                response_per_page = requests.get('https://bg.annapurnapost.com/api/tags/news?page=' + str(page) + '&per_page=20&tag=' + str(passed_argument))
                if not response_per_page:
                    break
                result.append(response_per_page.json()['data'])
                numberOfArticles+=len(response_per_page.json()['data'])

                page +=1

            except:
                break


        if not result:
            exit()
        json_string = json.dumps(result)
        # print(len(json_string))
        print('JSON object')
        print(json_string)
    except:
        print("No news found")
except:
    print("No arguments passed")

