# coding=utf-8
"""
输入页数和相对应的项目名称即可查询出想要的页面信息
"""
import requests, json
from urllib.parse import quote


class DouBan(object):
    def __init__(self):
        self.url = "https://movie.douban.com/j/search_subjects?type=tv&tag={}&sort=recommend&page_limit=20&page_start={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36"}

    # 发送请求，获取响应
    def parse_url(self, url):
        # print(url)
        r = requests.get(url, headers=self.headers)
        return r.content.decode()

    # 提取数据
    def get_content(self, json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subjects"]
        return content_list

    def save_content(self, content_list):
        with open("./doban.txt", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
            print("保存成功")

    def req_data(self):
        print("可以输入：热门  美剧  英剧  韩剧  日剧  国产剧  港剧  日本动画  综艺  纪录片")
        target = input("请输入要查询的剧种类：")
        target = quote(target, 'utf-8')
        return target

    def run(self):
        # 请求的url地址
        page_start = 0
        res_page = int(input("请输入要查询的页数："))*20
        target = self.req_data()
        while page_start < res_page:
            url = self.url.format(target, page_start)
            # 发送请求，获取响应
            r = self.parse_url(url)
            # 提取数据
            content_list = self.get_content(r)
            # 保存到本地
            self.save_content(content_list)
            # 接着抓取下一页
            page_start += 20


if __name__ == "__main__":
    douban = DouBan()
    douban.run()
