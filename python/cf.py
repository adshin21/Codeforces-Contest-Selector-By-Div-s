import requests

url = "http://codeforces.com/api"
options = '/contest.list'
link = 'http://codeforces.com/contest/'

data = requests.get(url+options)
data = data.json()

div3 = []
edu = []
if data['status'] == 'OK':
    data = data['result']
    for i in data:
        if 'Educational' in i['name']:
            edu.append(int(i['id']))

        if 'Div. 3' in i['name']:
            div3.append(int(i['id']))

    div3.sort()
    edu.sort()

    f = open("div3.txt","w+")
    cnt = 1
    for i in div3:
        temp = 'Div3 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()


    f = open("educational.txt","w+")
    cnt = 1
    for i in edu:
        temp = 'Educational Round '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()
