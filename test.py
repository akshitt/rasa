import requests

payload = {'text':'what is gemcal'}
r = requests.post('http://localhost:5005/model/parse', data=payload)
r_dict = r.json()
print(r_dict)
# scores_list = r_dict['scores']

# for scores in scores_list:
#     if scores['action']=='action_product_brand':
#         print(scores['action'], scores['score'])
    