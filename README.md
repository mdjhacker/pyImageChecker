<p align="center">
  <a href="https://github.com/mdjhacker/pyImageChecker">
    <img src="/assert/img_2.png" alt="Logo" width="100" height="100">
  </a>
</p>

<h2 align="center">PyImageChecker<br>网络图像查重系统</h2>
<p align="center">
<a href="https://github.com/mdjhacker/pyImageChecker"><img alt="GitHub license" src="https://img.shields.io/github/license/mdjhacker/pyImageChecker"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-v3.7-blue" alt="python" /></a>
<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>
<a href="https://www.neau.edu.cn/"><img src="https://img.shields.io/badge/school-neau-brightgreen" alt="school"/></a>
<a href="https://github.com/mdjhacker/pyImageChecker/releases/tag/v1.0.0"><img src="https://img.shields.io/badge/version-v1.0.0-blue" alt="version"/></a>
<a href="https://pan.baidu.com/s/1qqH4AmWVwZASHc6LuX8kVQ?pwd=1111"><img src="https://img.shields.io/badge/download-%E7%99%BE%E5%BA%A6%E4%BA%91-blue" alt="" /></a>
</p>

## DEMO
<p align="center">
<img src="assert/img_11.png" alt="" width="250" height="150">
<img src="/assert/3333.png" alt="" width="250" height="150">
</p>

## 编写理由
高校举办的图片竞选类活动中，存在部分人员直接利用网络图片顶替。传统的人力筛选模式不利于大量图像的筛选。因此利用python进行批量审查，推动原创风气。

## 原理
通过`Catbox`和`Saucenao`的api，先上传到`Catbox`图床，再通过`Saucenao`对回传数据进行分析，输出到`csv`表格中便于对比。

## 已实现功能
- [x] 图片重复率查询
- [x] 重复率表格导出
- [x] API持久化储存
## 使用方法
- [申请API](https://saucenao.com/user.php)
- [下载安装文件](https://github.com/mdjhacker/pyImageChecker/releases)
- 将API输入填写框，需要鉴别的图像放于`data`文件夹，鉴别后的表格将生成于`src`目录，命名为`similarity.csv`
- python二次开发
    ```
    pip install -r requirements.txt
    
    cd PyImageChecker
    
    python main.py
    ```

## 鸣谢
![img.png](assert/img.png)

![img_1.png](assert/img_1.png)

[PicImageSearch](https://github.com/kitUIN/PicImageSearch)

[Pyupload](https://github.com/yukinotenshi/pyupload)
## TODO
- [ ] 多查询api，增加重复率准确度
## BUG
issue/pull requests
