obj-m := alloctrace.o
DIRS := /usr/src/kernels/$(shell uname -r)
all:
	make -C $(DIRS) M=$(PWD) modules
clean:
	rm -Rf *.o *.ko *.mod.c *.order *.symvers