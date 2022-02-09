# PyImageChecker
<a href="https://github.com/mdjhacker/pyImageChecker"><img alt="GitHub license" src="https://img.shields.io/github/license/mdjhacker/pyImageChecker"></a>
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)

## 编写理由
高校举办的图片竞选类活动中，存在部分人员直接利用网络图片顶替。传统的人力筛选模式不利于大量图像的筛选。因此利用python进行批量审查，推动原创风气，同时避免主办方人员出现错颁奖的状况。

## 原理
通过`Catbox`和`Saucenao`的api，先上传到`Catbox`图床，再通过`Saucenao`对回传数据进行分析，输出到`csv`表格中便于对比。

## 已实现功能


## 安装方法
```
pyupload .gitignore --host=catbox

[1674/1674] bytes |====================>|Your link : https://files.catbox.moe/e03ygs.gitignore
```

## 鸣谢
![img.png](assert/img.png)

![img_1.png](assert/img_1.png)

[PicImageSearch](https://github.com/kitUIN/PicImageSearch)

[Pyupload](https://github.com/yukinotenshi/pyupload)
## Issues? Changes?
Just open an issue/pull requests
