redis 应用
========

常见的一些redis实现的功能，例如cron，延迟队列，去重队列，社交关系的好友关系，各种计数器等

python 2.7

### 去重队列

主要依赖lua脚本的原子性

* list + set 的方式实现
* zset的方式实现

### 大key删除

redis中一些大key的删除操作

* hash 删除
* list 删除
* set 删除
* sortset 删除 

总的思路，有scan方法使用scan方法，没有的话就是部分删除，多次删除




