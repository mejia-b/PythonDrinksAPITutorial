import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
question_list = response.json()['items']
print(type(question_list))
print(question_list)
for question in question_list:
    if question['tags'] == 'python':
        print(question['title'])
        print(question['link'])
    else:
        print("skipped")
    print()

