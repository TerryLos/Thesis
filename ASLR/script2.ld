SECTIONS
{
. = 0x10920;
.adummymem : { *(.adummymem) }
.text : { *(.text) }
. = 0x7FFD9F0;
.bss : { *(.bss) }
.heap : { *(.heap) }
.stack : { *(.stack) }
.data : { *(.data) }
}
