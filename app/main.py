from fastapi import FastAPI,Request
import uvicorn
import json
from package.message import SendMessages

api = FastAPI()





@api.post('/')
async def alter_api(request: Request):
    try:
        _m = await request.json()
        # print(_m)

        # 获取报警信息
        contents = _m['alerts']
        # from package.test_data import result
        # contents = result['alerts']


        # 获取报警类型
        _t = request.query_params.get('type')
        _o   = SendMessages()
        _s = await _o.switch(_type=_t, contents=contents)
        
        # 返回值为 True 或  False
        if not _s:
            return json.dumps({'code': -1, 'msg': 'faild'})

        return json.dumps({'code': 200, 'msg': 'success'})
    except:
        return json.dumps({'code': -1, 'msg': 'faild'})


if __name__ == '__main__':
    uvicorn.run('main:api',host='0.0.0.0', port=5001,reload=True)




