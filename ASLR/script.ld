SECTIONS
{
. = 0x10CB8;
.text : { *(.text) }
. = 0x7FFF538;
.data : { *(.data) }
.bss : { *(.bss) }
}
