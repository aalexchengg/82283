import requests
from dotenv import load_dotenv
import os

# authorization data
load_dotenv()
personal_use = os.getenv('PUS')
secret_token = os.getenv('ST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

auth = requests.auth.HTTPBasicAuth(personal_use, secret_token)
data = {'grant_type': 'password', 'username': username, 'password': password}
headers = {'User-Agent': 'remi/0.0.1'}
api = "https://oauth.reddit.com"

# get access token for future requests
tk = requests.post('https://www.reddit.com/api/v1/access_token', auth = auth, data = data, headers = headers)
tk = tk.json()['access_token']
headers['Authorization'] = 'bearer {}'.format(tk)



#community
community = "teenagers"
# community = "OVER30REDDIT"

# get top 100 posts
top_100_posts = requests.get("{}/r/{}/top".format(api, community), params = {'limit': '100'}, headers = headers)
top_100_posts = top_100_posts.json()['data']['children']

# for each post, write all comments to txt file
with open('{}.txt'.format(community), 'w', encoding = 'utf-8') as file:
    for post in top_100_posts:
        # get url of post from json data
        url = post['data']['permalink']
        # get post 
        res = requests.get("{}{}".format(api, url), headers = headers)
        res = res.json()
        comments = res[1]['data']['children']
        for comment in comments:
            #if comment is deleted, move on
            if 'body' not in comment['data']:
                continue
            else:
                file.write(comment['data']['body'])
                file.write("\n")


