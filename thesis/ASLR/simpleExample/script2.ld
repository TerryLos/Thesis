SECTIONS
{
. = 0x11678;
.adummymem : { *(.adummymem) }
.text : { *(.text) }
. = 0x7FFF1A8;
.bss : { *(.bss) }
.stack : { *(.stack) }
.data : { *(.data) }
.heap : { *(.heap) }
}