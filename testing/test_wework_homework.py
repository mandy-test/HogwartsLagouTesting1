
"""
作业
企业微信
使用 requests 实现部门的增删改查
"""
import requests


class TestWeworkApi:
    secrete = 'idWKk_dfyLxWept8o0K8nGc15LHZKzmTYsuQSMd9ixc'
    id = 'ww5c30c081f30784ff'

    def setup(self):
        res = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = res.json()['access_token']
        print(self.token)

    def test_wework_api(self):
        # 获取部门列表
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id=2')
        print("获取部门列表")
        print(r.json())
        print(f"Errcode:{r.json()['errcode']}")
        if r.json()['errcode'] == 0:
            # 删除部门
            print("删除部门")
            r = requests.get(
                f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2')
            print(r.json())

        # 创建部门
        print("创建部门")
        create_data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=' + self.token,
                          json=create_data)
        print(r.json())

        # 更新部门
        print("更新部门")
        data = {
            "id": 2,
            "name": "广州研发中心new",
            "name_en": "RDGZ_new",
            "parentid": 1,
            "order": 1
        }

        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=' + self.token, json=data)
        print(r.json())