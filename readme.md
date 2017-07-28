CharacterPickUp -- 人物关系提取
----
- 根据人物名字从大量文本中分析人物关系


实现方法
---
- 根据人物名字统计`共现`
- 超过阈值则认为相关



- 使用 [jieba](https://github.com/fxsjy/jieba) 将每句话分割为一个个可能的块
- 统计块的出现概率
