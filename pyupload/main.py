import time
import shelve
from pyupload.uploader import *
from PicImageSearch import SauceNAO
import os
import csv

uploader_classes = {
    "catbox": CatboxUploader,
    "mixtape": MixTapeUploader,
    "uguu": UguuUploader,
    "fileio": FileioUploader
}


def upload():
    rootdir = '.\data'
    data_list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    headers = ['序号', '文件名', '相似度', '略缩图地址']  # csv headers
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
        saucenao = SauceNAO(api_key='bb3d05cfd3779f1e3b8c6131c9c1b57979dc7994')  # api_key location
        res = saucenao.search(result)
        print("24h查询额度剩余 : " + str(res.long_remaining))  # 每天访问额度剩余
        # print("30s访问额度剩余 : " + str(res.short_remaining))  # 每30秒访问额度剩余
        print("略缩图地址 : " + res.raw[0].thumbnail)  # 略缩图地址
        print("相似度 : " + str(res.raw[0].similarity) + "%")  # 相似度
        # print("相似作品标题 : " + res.raw[0].title)  # 相似的标题
        # print("相似作品作者 : " + res.raw[0].author)  # 作者

        # csv save
        rows = [
            [i, data_list[i], res.raw[0].similarity, res.raw[0].thumbnail]
        ]
        print('正在写入表格文件中，请稍等......')
        with open('./src/similarity.csv', 'a+', newline='') as f:
            f_csv = csv.writer(f)
            if i == 0:
                f_csv.writerow(headers)
            else:
                f_csv.writerows(rows)

        # wait for api limit
        print('\n')
        time.sleep(7)


# def local_save():
#     s = shelve.open('./src/local_save.db')  #
#     try:
#         s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
#         s['MM'] = [1, 2, 3]
#         s['api_key'] = api_key
#     finally:
#         s.close()
#
#     try:
#         s = shelve.open('test_shelf.db')
#         value = s['kk']
#         print(value)
#     finally:
#         s.close()

# s = shelve.open('test_shelf.db', flag='w', writeback=True)
# try:
#     # 增加
#     s['QQQ'] = 2333
#     # 删除
#     del s['MM']
#     # 修改
#     s['kk'] = {'String': 'day day up'}
# finally:
#     s.close()
#
# s = shelve.open('test_shelf.db')
# try:
#     # 方法一：
#     for item in s.items():
#         print('键[{}] = 值[{}]'.format(item[0], s[item[0]]))
#     # 方法二：
#     for key, value in s.items():
#         print(key, value)
# finally:
#     s.close()


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
                                               Author:HuangYu Version:1.0
    \033[0m ''')

    # input('请将图片以非汉字命名，放到data文件夹下，双击回车开始......')

    upload()
    # local_save()
