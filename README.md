# 利用bpf统计内核中alloc_page内存信息
> 内核使用alloc_page申请的内存不会显示在meminfo中，经常出现内存不够情况却不知道谁在使用，利用bpf工具统计内核alloc_page内存占用信息

## TARGET
1. 统计所有alloc_pages使用的内存占用信息；
2. 过滤出最多使用路径；

## PROCESS
- 使用 BCC 开发 python 脚本，能够识别 内核/用户进程 的 alloc_pages 调用信息并统计输出
- 已经可以追踪打印内核栈/用户栈符号，不过用户栈大部分函数符号都无法解析，而且不能和 kretprobe 程序一起用（无法解析 alloc_pages 返回的 page 结构体），否则就无法解析内核栈

## PROBLEM
### 如何区分驱动调用？
目前对于内核栈中函数调用信息统计分析后，主要有两条路径：

1. 通过触发页错误，分配实际的物理页
```
    __handle_mm_fault [kernel]
    handle_mm_fault [kernel]
    exc_page_fault [kernel]
    asm_exc_page_fault [kernel]
```
2. 通过系统调用
```
    do_syscall_64 [kernel]
    entry_SYSCALL_64_after_hwframe [kernel]
```

## TODO
- [x] 解析 内核/用户栈
- [ ] 追踪内核中不同驱动的调用信息
- [ ] 消除对特定 包/工具 的依赖，比如可以在内核提供 sys 或者 proc 接口，用户态可以通过简单的 c/python/shell 程序处理