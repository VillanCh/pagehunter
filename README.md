# PageHunter

来源于 Sqlmap 的页面比较技术：

- [x] 通过添加 base_page 来判断 Web 应用整体的页面是否稳定，动态，以及严重动态。
- [x] 同时添加 `raw/noscript/textonly` 三种模式来进行判断和计算 ratio
- [x] ratio 动态调整支持固定一定数量的差别字符串作为最大容忍度
- [ ] ratio 支持固定差异容忍度（默认推荐为 0.98）
- [ ] 为页面内容判重提供支持（Comparison）: Ratio 支持 / 正则支持 / 特征字符串
- [ ] 当 TextOnly 的时候，添加提取子串作为判断页面相同的依据

具体使用实例请阅读 

```base
pagehunter.tests.test_*.py
```
