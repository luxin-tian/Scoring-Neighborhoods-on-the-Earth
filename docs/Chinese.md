# 为地球上的社区打分

该项目使用[Elo评分系统](https://en.wikipedia.org/wiki/Elo_rating_system)来量化衡量世界各地的城市感知。该测量基于对人类的数字调查，其中要求用户在某些维度（例如安全性）方面比较两个街景图像。

目前，我使用来自[Place Pulse 2.0]（http://pulse.media.mit.edu/data/）的调查数据，该数据涵盖了来自六大洲28个国家的56个城市，并且仍在持续进行中。我提供了可重现的Python脚本，该脚本可在该项目的资源库中计算Elo Rating分数，作为``elorating``模块的演示。我们还可以在[交互式地图](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/)上看到结果。

此外，由于[Place Pulse 2.0](http://pulse.media.mit.edu/data/)从[Google地图]（https://developers.google.com/maps/documentation）检索街景图像，因此它不覆盖中国大陆（Google自2010年起终止在中国的消费者服务，请参见[Wikipedia](https://en.wikipedia.org/wiki/Google_China)。我计划将来使用[百度地图](https://lbsyun.baidu.com)提供的街景图像将该项目扩展到中国大陆。现在，我用Python完成了一个程序，该程序可以检索街景图像。我已经将此程序包含在该项目在GitHub上的目录中。


## 交互地图
我们基于六个维度为全球56个城市的街区打分，这意味着你可以比较__纽约__和__中国香港__的两个街区哪一个更宜居！选择一个来浏览（下一个页面将是英文的，但你可以点击任何一个英文城市名称来浏览可视化交互地图）：
- [安全](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/safety)
- [宜居](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/lively)
- [富有](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/wealthy)
- [美观](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/beautiful)
- [忧郁](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/depressing)
- [无聊](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/boring)

## 评分算法
[Elo 评分系统](https://en.wikipedia.org/wiki/Elo_rating_system)

作为该项目的副产品，我用Python编写了一个``elorating``模块，该模块可用于任何采用[Elo评分系统](https://en.wikipedia.org/wiki/Elo_rating_system)的数据科学项目。 特别是，作为计算经济学学生，我需要指出的是，尽管[Elo评分系统](https://en.wikipedia.org/wiki/Elo_rating_system)最初旨在根据比赛记录来衡量棋手的相对技能水平，它也可以作为一个[社会福利函数](https://en.wikipedia.org/wiki/Social_welfare_function)，来根据个人偏好显示出集体偏好，这是微观经济学和社会选择理论的范畴。

## 项目文档
[为地球上的社区打分项目文档](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/build/html/index.html)

## 关于我
[田璐鑫](https://luxin-tian.github.io/profile/) 
[芝加哥大学](https://www.uchicago.edu)
[计算社会科学](https://macss.uchicago.edu) 硕士学生

## 关于计算社会科学
了解更多[计算社会科学](https://macss.uchicago.edu)在数字时代的影响力。