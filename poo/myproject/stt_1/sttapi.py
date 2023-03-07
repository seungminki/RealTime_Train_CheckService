import base64
import json
import threading
import requests
import time

from dotenv import load_dotenv
import os

load_dotenv()
url = os.environ.get('url')
api_key_id = os.environ.get('api_key_id')
api_key = os.environ.get('api_key')

class SttApi:
    frames = []

    def __init__(self, RATE, CHUNK, RECORD_SECONDS):
        self.host = url
        self.STT_STATUS = 'P01' # P01 진행중, P02 첫음검출, P03 끝음검출
        self.RATE = RATE
        self.CHUNK = CHUNK
        self.RECORD_SECONDS = RECORD_SECONDS
        self.index = 0
    
    @staticmethod
    def create(RATE, CHUNK, RECORD_SECONDS):
        return SttApi(RATE, CHUNK, RECORD_SECONDS)

    def post(self, url, field_data) :
        headers = {'API-KEY-ID':api_key_id, 'API-KEY':api_key, 'Content-Type':'application/json'}
        return requests.post(url, headers=headers, data=field_data)

    def setData(self, data):
        self.frames.append(data)

    def getData(self):
        return self.frames[0:self.index]

    def sendData(self, i, data):
        if (self.STT_STATUS == 'P01' or self.STT_STATUS == 'P02'):
            bdata = base64.b64encode(data).decode('utf8')

            field_data = json.dumps({'sttId':self.sttId,'dataIndex':i+1,'data':bdata})
            url = self.host + '/stt/sendData'
            res = self.post(url, field_data)

            jsonObject = json.loads(json.dumps(res.json()))
            self.STT_STATUS = jsonObject.get('analysisResult').get('progressCode')

            return res

    def sendBody(self, sttId, stream):
        self.sttId = sttId

        while(self.STT_STATUS == 'P01' or self.STT_STATUS == 'P02'):
            if(len(self.frames) > (self.index + 1)):
                self.sendData(self.index, self.frames[self.index])
                self.index = self.index + 1
            time.sleep(0.01)

    def prepare(self, keywordlist):
        field_data = json.dumps({'modelId':'0','useEpd':'1','codec':'1','midResult':'1','pitchResult':'1','keywordList':keywordlist})
        url = self.host + '/stt/prepare'
        res = self.post(url, field_data)
        jsonObject = json.loads(json.dumps(res.json()))
        sttId = jsonObject.get('sttId')
        return sttId

    def finish(self, sttId):
        field_data = json.dumps({'sttId':sttId})
        url = self.host + '/stt/finish'
        res = self.post(url, field_data)
        return res