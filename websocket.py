import asyncio,base64,json
import websockets
from utils.GetwssURL import GetwssURL
from utils.data import data
links = data['all_links']

def makeData(chunk,status):
    chunk = base64.b64encode(chunk).decode()
    if status==2:
         data = {
              'data':{
                   'status':2
              }
         }
         print('send end')
    elif status==0:
        data = {
            'common':{
                'app_id':'0424fea3'
                },
            'business':{
                'language':'en_us',
                'domain':'iat',
                'vad_eos':99999
            },
            'data':{
                'status':0,
                'format':'audio/L16;rate=16000',
                'encoding':'raw',
                'audio':chunk
            }
            }
    elif status==1:
        data = {
            'data':{
                'status':1,
                'format':'audio/L16;rate=16000',
                'encoding':'raw',
                'audio':chunk
                }
                }

    return json.dumps(data)



out = ''
res_status = -1
chunk_size = 1208  # 每个分段的大小
async def main():
    global res_status,chunk_size,out
    url = GetwssURL()

    for i in links:
        status = 0
        with open(f'./pcm/{i}.pcm','rb') as f:
            pcm_data = f.read()
        async with websockets.connect(url) as websocket:
            receive_task = asyncio.create_task(receive_messages(websocket,i))
            for j in range(0,len(pcm_data),chunk_size):
                chunk = pcm_data[j:j+chunk_size]
                if (j+chunk_size)>=len(pcm_data):
                    status = 2
                wsdata = makeData(chunk,status)
                await websocket.send(wsdata)
                status = 1
            await receive_task
            
async def receive_messages(websocket,ie):
    global out,res_status
    res_status = -1
    while True:
        try:
            response = await websocket.recv()
            data = json.loads(response)
            res_status = data['data']['status']
            print(res_status)
            data = data['data']['result']['ws']
            for i in data:
                out += i['cw'][0]['w']
                #print(out)
            if res_status==2:
                with open(f'./dist/{ie}.txt','wt') as ff:
                    ff.write(out)
                print(out)
                out = ''
                break
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break
asyncio.run(main())