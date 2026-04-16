import requests
import base64
from dotenv import load_dotenv
import os
load_dotenv('.env')
CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
def access_token():
    try:
        credentials=f'{CLIENT_ID}:{CLIENT_SECRET}'
        encoded_credentials=base64.b64encode(credentials.encode()).decode()
        response=requests.post(
            'https://accounts.spotify.com/api/token',
            headers={'Authorization': f'Basic {encoded_credentials}'},
            data={'grant_type':'client_credentials'}
        )
        # print(response.json()['access_token'])
        # print('token generated successfuly')
        return response.json()['access_token']
    except Exception as e:
        print('error in token generation',e)

# print(access_token())

# #  to take latest release  in spotify
# # def function
def get_new_release():
    token=access_token()
    header={'Authorization':f'Bearer {token}'}
    param={'limit':50}
#     # data fetch chyth edkan request pass cheynm
    response=requests.get('https://api.spotify.com/v1/browse/new-releases',headers=header,params=param)
    # print(response)
    if response.status_code == 200:
        # print(response.json())
        data= response.json()
        release=[]
        album=data['albums']['items']
        for i in album:
            print(i)
            a={
                'album_name':i['name'],
                'release_date':i['release_date']
            }
            release.append(a)
            print(release)
    else:
        print(f"Error: {response.status_code}")
    print(response.text)


get_new_release()
    