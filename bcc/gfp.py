#!/usr/bin/python3
___GFP_DMA = 0x01
___GFP_HIGHMEM = 0x02
___GFP_DMA32 = 0x04
___GFP_MOVABLE = 0x08
___GFP_RECLAIMABLE = 0x10

# ___GFP_HIGH = 0x20
# ___GFP_IO = 0x40
# ___GFP_FS = 0x80
# ___GFP_ZERO = 0x100
# ___GFP_ATOMIC = 0x200
# ___GFP_DIRECT_RECLAIM = 0x400
# ___GFP_KSWAPD_RECLAIM = 0x800
# ___GFP_WRITE = 0x1000
# ___GFP_NOWARN = 0x2000
# ___GFP_RETRY_MAYFAIL = 0x4000
# ___GFP_NOFAIL = 0x8000
# ___GFP_NORETRY = 0x10000
# ___GFP_MEMALLOC = 0x20000
# ___GFP_COMP = 0x40000
# ___GFP_NOMEMALLOC = 0x80000
# ___GFP_HARDWALL = 0x100000
# ___GFP_THISNODE = 0x200000
# ___GFP_ACCOUNT = 0x400000
# ___GFP_ZEROTAGS = 0x800000
# ___GFP_SKIP_ZERO = 0x1000000
# ___GFP_SKIP_KASAN_UNPOISON = 0x2000000
# ___GFP_SKIP_KASAN_POISON = 0x4000000
# ___GFP_SKIP_ZERO = 0
# ___GFP_SKIP_KASAN_UNPOISON = 0
# ___GFP_SKIP_KASAN_POISON = 0
# ___GFP_NOLOCKDEP = 0x8000000
# ___GFP_NOLOCKDEP = 0

def get_zone(mask):
    if(mask&___GFP_DMA):
        return "DMA"
    elif(mask&___GFP_HIGHMEM):
        return "HighMem"
    elif(mask&___GFP_DMA32):
        return "DMA32"
    elif(mask&___GFP_MOVABLE):
        return "Movable"
    else:
        return "Normal"