# Asyncio 笔记

py3中最重要的一个模块，或者说最有吸引力的模块就是原生直接支持绿色线程, 从3.5版本开始支持 `async/await` 函数, API一支有变化，写的时候需要注意

尽量asyncio 在考虑 threads

几种模型
1. io可以并行，没有需要同步的地方
2. 某个阶段或者最后的结果需要收集到一起，才能做下一步
3. 链式
4. 生产-消费者模型，很大的问题就是怎么停止消费组
5. 执行逻辑需要有同步的地方
6. 动态启动一个co
7. 怎么关闭一个正在运行的co

await 是等待一个异步的结果
async def  是一个coroutine执行体
yeild from ?
Anything defined with async def may not use yield from

```
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

Finally, when you use await f(), it’s required that f() be an object that is awaitable. Well, that’s not very helpful, is it? For now, just know that an awaitable object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator. If you’re writing a program, for the large majority of purposes, you should only need to worry about case #1.

协程实现
* generator-based
* native coroutine

## 重要概念

### Future

future 类似一个coroutinue, 多个非阻塞任务之间的结果等待，使用它来串联。

### yield from

yield 使得函数可以暂停, send 使得生成器之间可以传递参数

`yield from` 

```
yield from itertor 
=
for x in itertor:
    yeild x
```

### transport and protocol

