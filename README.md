# 利用bpf统计内核中alloc_page内存信息
> 内核使用alloc_page申请的内存不会显示在meminfo中，经常出现内存不够情况却不知道谁在使用，利用bpf工具统计内核alloc_page内存占用信息

## TARGET
1. 统计所有alloc_pages使用的内存占用信息；
2. 过滤出最多使用路径；

## PROCESS
- 使用 BCC 开发 python 脚本，能够识别 内核/用户进程 的 alloc_pages 调用信息并统计输出

## TODO
- [ ] 追踪内核中不同驱动的调用信息
- [ ] 消除对特定 包/工具 的依赖，比如可以在内核提供 sys 或者 proc 接口，用户态可以通过简单的 c/python/shell 程序处理