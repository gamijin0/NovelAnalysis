CharacterPickUp -- 人物关系提取
----
- 根据人物名字从大量文本中分析人物关系


实现方法
---
- 根据人物名字统计`共现`
    - 若一个场景出现 `3次A,2次B,1次C`
    - 则
        - A-B: 3+2=5
        - A-C: 3+1=4
        - B-C: 2+1=3
    - 待改进

- 超过阈值则认为相关

示例
---
![平凡的世界人物关系](https://github.com/gamijin0/NovelAnalysis/raw/master/example_1/pfdsj.png)



