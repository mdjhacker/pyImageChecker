# -*- encoding: utf-8 --
import time
from catbox import *
from saucenao import SauceNAO
import os
import csv
import colorama

colorama.init(autoreset=True)
uploader_classes = {
    "catbox": CatboxUploader,
}
# api_key='bb3d05cfd3779f1e3b8c6131c9c1b57979dc7994'


def upload():
    rootdir = '.\data'
    data_list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    headers = ['序号', '文件名', '相似度', '略缩图地址', '搜索时间']  # csv headers
    for i in range(0, len(data_list)):
        # path = os.path.join(rootdir, data_list[i])
        new_path = 'data/' + data_list[i]
        print("文件名称 : " + data_list[i])

        # catbox uploader
        uploader_class = uploader_classes["catbox"]
        uploader_instance = uploader_class(new_path)
        result = uploader_instance.execute()  # catbox link
        print("OK")
        # print("Your link : {}".format(result))

        # saucenao searcher
        saucenao = SauceNAO(api_key)  # api_key location
        res = saucenao.search(result)
        print("24h查询额度剩余 : " + str(res.long_remaining))  # 每天访问额度剩余
        # print("30s访问额度剩余 : " + str(res.short_remaining))  # 每30秒访问额度剩余
        print("相似图网址 : " + res.raw[0].thumbnail)  # 略缩图地址
        print("相似度 : " + str(res.raw[0].similarity) + "%")  # 相似度
        # print("相似作品标题 : " + res.raw[0].title)  # 相似的标题
        # print("相似作品作者 : " + res.raw[0].author)  # 作者

        # csv save
        rows = [
            [i,
             data_list[i],
             res.raw[0].similarity,
             res.raw[0].thumbnail,
             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
        ]
        print('正在写入表格文件中，请稍等......')
        with open('./src/similarity.csv', 'a+', newline='') as f:
            f_csv = csv.writer(f)
            if i == 0:
                f_csv.writerow(headers)
                f_csv.writerows(rows)
            else:
                f_csv.writerows(rows)

        # wait for api limit
        print('\n')
        time.sleep(7)


def api_code_check_save():
    global api_key
    #  判断是否存在文件（是-）
    if os.path.exists('src/api_code.csv'):
        with open('./src/api_code.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                time.sleep(0.0001)  # 有坑，不用占位符号暂无法输出
        print('检测到Api_key本地存在，已自动填写！{}'.format(row[0]))
        api_key = row[0]
    else:
        api_key = input('无本地API文件,第一次请手动输入:')
        headers = ['Api_code']
        rows = [
            {'Api_code': api_key}
        ]
        with open('./src/api_code.csv', 'w', newline='') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)


if __name__ == "__main__":
    print('''\033[36m
     __  .___  ___.      ___       _______  _______ 
    |  | |   \/   |     /   \     /  _____||   ____|
    |  | |  \  /  |    /  ^  \   |  |  __  |  |__   
    |  | |  |\/|  |   /  /_\  \  |  | |_ | |   __|  
    |  | |  |  |  |  /  _____  \ |  |__| | |  |____ 
    |__| |__|  |__| /__/     \__\ \______| |_______|
      ______  __    __   _______   ______  __  ___  _______ .______      
     /      ||  |  |  | |   ____| /      ||  |/  / |   ____||   _  \     
    |  ,----'|  |__|  | |  |__   |  ,----'|  '  /  |  |__   |  |_)  |    
    |  |     |   __   | |   __|  |  |     |    <   |   __|  |      /     
    |  `----.|  |  |  | |  |____ |  `----.|  .  \  |  |____ |  |\  \----.
     \______||__|  |__| |_______| \______||__|\__\ |_______|| _| `._____|
                                                              Version:1.0
    \033[0m ''')

    # input('请将图片以非汉字命名，放到data文件夹下，双击回车开始......')
    api_code_check_save()
    upload()
    print('所有任务执行完毕，窗口将于10s后自动关闭！')
    time.sleep(10)
