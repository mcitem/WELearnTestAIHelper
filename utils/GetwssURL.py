import hmac
import hashlib
import base64
from datetime import datetime,timezone
from urllib.parse import quote
from utils.config import config
def GetwssURL():
    APPID = config['iat']['APPID']
    APISecret = config['iat']['APISecret']
    APIKey = config['iat']['APIKey']

    date = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    host = 'mcitem.com'

    signature_origin = f'host: {host}\ndate: {date}\nGET /v2/iat HTTP/1.1'
    signature_sha = hmac.new(APISecret.encode(), signature_origin.encode(), hashlib.sha256).digest()
    signature = base64.b64encode(signature_sha).decode()

    authorization_origin = f'api_key="{APIKey}",algorithm="hmac-sha256",headers="host date request-line",signature="{signature}"'
    authorization = base64.b64encode(authorization_origin.encode()).decode()

    wssURL = f'wss://iat-api.xfyun.cn/v2/iat?authorization={authorization}&date={quote(date)}&host={host}'
    return wssURL