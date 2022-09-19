#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/types.h>
#include <linux/init.h>
#include <linux/gfp.h>

// 模块加载函数
static int __init init_fun(void) //函数名随意，__init和__exit是init.h中定义的宏
{
    // 初始化代码
    printk("alloc_trace kernel module init\n");
    return 0;
}
// 模块卸载函数
static void __exit exit_fun(void)
{
    // 释放代码
    printk("alloc_trace kernel module exit\n");
}

module_init(init_fun); // 驱动程序初始化的入口点
module_exit(exit_fun); // 对于可加载模块，内核在此处调用module_cleanup()函数，而对于内置的模块，它什么都不做。
MODULE_LICENSE("GPL"); // 许可权限声明，如果不申明，模块加载时会收到内核的警告