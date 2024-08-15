import http.client
import json

url = "codeforces.com"
options = '/api/contest.list'
link = 'http://codeforces.com/contest/'


def make_request(url, options, use_https=False):
    if use_https:
        conn = http.client.HTTPSConnection(url)
    else:
        conn = http.client.HTTPConnection(url)
    conn.request("GET", options)
    response = conn.getresponse()
    return response


response = make_request(url, options, use_https=True)

if response.status == 301 or response.status == 302:
    redirected_url = response.getheader('Location')
    if redirected_url:
        new_url = redirected_url.replace('http://', '').replace('https://', '')
        new_host, new_path = new_url.split('/', 1)
        new_path = '/' + new_path
        response = make_request(new_host, new_path, use_https=True)

if response.status == 200:
    data = json.loads(response.read().decode())

    div3 = []
    edu = []

    for fct in data['result']:
        if "Educational" in fct['name']:
            edu.append(fct['id'])
        if "Div. 3" in fct['name']:
            div3.append(fct['id'])

    div3.sort()
    edu.sort()

    with open("Div3.txt", "w") as div3_file:
        for i, contest_id in enumerate(div3, start=1):
            div3_file.write(f"Div3 Rounds {i} : {link}{contest_id}\n")

    with open("Educational.txt", "w") as edu_file:
        for i, contest_id in enumerate(edu, start=1):
            edu_file.write(f"Educational Round {i} : {link}{contest_id}\n")
else:
    print(f"Request failed with status code {response.status}")
