SECTIONS
{
. = 0x102B0;
.text : { *(.text) }
. = 0x7FFE438;
.bss : { *(.bss) }
.data : { *(.data) }
}
