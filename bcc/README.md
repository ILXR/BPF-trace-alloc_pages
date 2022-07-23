# 设计思路

## 常规输出（以进程为单位统计）

不需要携带任何命令，会以进程为单位输出所有进程调用 alloc_pages 的统计信息：

| 进程id | 命令 | 申请到的页数 | 申请失败的页数 | 总申请页数 |
|:-:|:-:|:-:|:-:|:-:|
| PID | COMM | SUCCESS | FAIL | ALL |

## detail 模式

添加 -d 参数:
> track_alloc_pages -d

直接输出每一次的调用信息

| 进程id | 命令 | 线程id | 申请的页数 | GFP分配标志 | 返回的地址 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| PID | COMM | TID | PAGES | MASK | ADDR |

## 指定进程（以线程为单位统计）

指定 -p 参数：
> track_alloc_pages -p [pid]

可以单独监视某一个进程的调用信息，以线程为单位进行统计：

| 线程id | 命令 | 申请到的页数 | 申请失败的页数 | 总申请页数 |
|:-:|:-:|:-:|:-:|:-:|
| TID | COMM | SUCCESS | FAIL | ALL |

## 指定进程 detail 模式
-p 可以和 -d 一起用：
> track_alloc_pages -d -p [pid]

这是对该进程的每一次调用信息都进行输出:

| 进程id | 命令 | 线程id | 申请的页数 | GFP分配标志 | 返回的地址 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| PID | COMM | TID | PAGES | MASK | ADDR |