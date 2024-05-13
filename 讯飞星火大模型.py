f =open('./output.txt','rt',encoding='utf-8')
from utils.config import config 
#星火认知大模型v3.5的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
#星火认知大模型v3.5的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = config['spark']['SPARKAI_URL']
SPARKAI_APP_ID = config['spark']['SPARKAI_APP_ID']
SPARKAI_API_SECRET = config['spark']['SPARKAI_API_SECRET']
SPARKAI_API_KEY = config['spark']['SPARKAI_API_KEY']
SPARKAI_DOMAIN = config['spark']['SPARKAI_DOMAIN']

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError('Python environment for SPARK AI is not completely set up: required package "python-dotenv" is missing.') from None
import json
load_dotenv()
if __name__ == '__main__':
    from sparkai.core.callbacks import StdOutCallbackHandler
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        request_timeout=30, # 
        streaming=True,

    )
    messages = [ChatMessage(
        role="user",
        content='请给我下面英文题目最有可能的答案，不需要解释过程,选项保持英文'+f.read(),
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)