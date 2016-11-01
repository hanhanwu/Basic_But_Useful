import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from onedrivesdk.helpers.resource_discovery import ResourceDiscoveryRequest, ServiceInfo
import json
import re
import requests


    

redirect_uri = 'http://localhost:8080'
client_secret = '[my client secret]'
client_id='[my client id]'
resourceId = "https://api.office.com/discovery/"
auth_server_url='https://login.microsoftonline.com/common/oauth2/authorize'
auth_token_url='https://login.microsoftonline.com/common/oauth2/token'

request_url = "https://api.office.com/discovery/v1.0/me/services"
sharepoint_base_url = '[my based sharepoint url]'
sharepoint_site_url = sharepoint_base_url + 'sites/[my site]'


http = onedrivesdk.HttpProvider()
auth = onedrivesdk.AuthProvider(http,
                                client_id,
                                auth_server_url=auth_server_url,
                                auth_token_url=auth_token_url)
auth_url = auth.get_auth_url(redirect_uri)
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
auth.authenticate(code, redirect_uri, client_secret, resource=resourceId)
access_token = auth.access_token
headers = {'Authorization': 'Bearer ' + access_token}
response = json.loads(requests.get(sharepoint_site_url, headers=headers).text)
print response
        
