SECTIONS
{
. = 0x380C12;
 _text = .;
.text :{
  KEEP (*(.data.boot))
  *(.text.boot)
    . = . + 0xDDF6;
libukbus.o (.text);
  . = . + 0x5631;
libnolibc.o (.text);
  . = . + 0x7D88;
libukboot.o (.text);
  . = . + 0x889F;
libukallocbbuddy.o (.text);
  . = . + 0x9E14;
libkvmplat.o (.text);
  . = . + 0x1542;
libukboot_main.o (.text);
  . = . + 0xF4B;
appentropy.o (.text);
  . = . + 0x2144;
libuktimeconv.o (.text);
  . = . + 0x5626;
libukswrand.o (.text);
  . = . + 0x70D7;
libukargparse.o (.text);
  . = . + 0x8E56;
libkvmvirtio.o (.text);
  . = . + 0xA172;
libukalloc.o (.text);
  . = . + 0xE576;
libukdebug.o (.text);
  . = . + 0x4E71;
libuktime.o (.text);
  . = . + 0x4622;
libuksglist.o (.text);
  . = . + 0xE8E4;
libx86_64arch.o (.text);
  . = . + 0x6D7;
libkvmpci.o (.text);
  *(.text)
  *(.text.*)
 }
 _etext = .;
. = ALIGN((1 << 12));
 uk_ctortab_start = .;
.uk_ctortab :{ KEEP(*(SORT_BY_NAME(.uk_ctortab[0-9]))) }
 uk_ctortab_end = .;
 uk_inittab_start = .;
.uk_inittab :{ KEEP(*(SORT_BY_NAME(.uk_inittab[1-6][0-9]))) }
 uk_inittab_end = .;
. = ALIGN(0x8);
 _ctors = .;
.preinit_array :{
  PROVIDE_HIDDEN (__preinit_array_start = .);
  KEEP (*(.preinit_array))
  PROVIDE_HIDDEN (__preinit_array_end = .);
 }
. = ALIGN(0x8);
.init_array :{
  PROVIDE_HIDDEN (__init_array_start = .);
  KEEP (*(SORT_BY_INIT_PRIORITY(.init_array.*) SORT_BY_INIT_PRIORITY(.ctors.*)))
  KEEP (*(.init_array .ctors))
  PROVIDE_HIDDEN (__init_array_end = .);
 }
 _ectors = .;
 __eh_frame_hdr_start = .;
.eh_frame_hdr :{ *(.eh_frame_hdr) *(.eh_frame_hdr.*) }
 __eh_frame_hdr_end = .;
. = ALIGN(0x20);
 _tls_start = .;
.tdata :{ *(.tdata) *(.tdata.*) *(.gnu.linkonce.td.*) }
 _etdata = .;
.tbss :{ *(.tbss) *(.tbss.*) *(.gnu.linkonce.tb.*) . = ALIGN(0x20); }
 _tls_end = . + SIZEOF(.tbss);
. = ALIGN((1 << 12));
 __eh_frame_start = .;
.eh_frame :{ *(.eh_frame) *(.eh_frame.*) }
 __eh_frame_end = .;
. = ALIGN((1 << 12));
 _rodata = .;
.rodata :{
  *(.rodata)
  *(.rodata.*)
 }
 _erodata = .;
. = ALIGN((1 << 12));
 _data = .;
.data :{
  *(.data)
  *(.data.*)
 }
 _edata = .;
. = ALIGN((1 << 12));
 __bss_start = .;
.bss :{
  *(.bss)
  *(.bss.*)
  *(COMMON)
  . = ALIGN((1 << 12));
 }
.intrstack :{
  *(.intrstack)
  . = ALIGN((1 << 12));
 }
 _end = .;
.comment 0 :{ *(.comment) }
.debug 0 :{ *(.debug) }
.line 0 :{ *(.line) }
.debug_srcinfo 0 :{ *(.debug_srcinfo) }
.debug_sfnames 0 :{ *(.debug_sfnames) }
.debug_aranges 0 :{ *(.debug_aranges) }
.debug_pubnames 0 :{ *(.debug_pubnames) }
.debug_info 0 :{ *(.debug_info .gnu.linkonce.wi.*) }
.debug_abbrev 0 :{ *(.debug_abbrev) }
.debug_line 0 :{ *(.debug_line .debug_line.* .debug_line_end ) }
.debug_frame 0 :{ *(.debug_frame) }
.debug_str 0 :{ *(.debug_str) }
.debug_loc 0 :{ *(.debug_loc) }
.debug_macinfo 0 :{ *(.debug_macinfo) }
.debug_weaknames 0 :{ *(.debug_weaknames) }
.debug_funcnames 0 :{ *(.debug_funcnames) }
.debug_typenames 0 :{ *(.debug_typenames) }
.debug_varnames 0 :{ *(.debug_varnames) }
.debug_pubtypes 0 :{ *(.debug_pubtypes) }
.debug_ranges 0 :{ *(.debug_ranges) }
.debug_macro 0 :{ *(.debug_macro) }
.gnu.attributes 0 :{ KEEP (*(.gnu.attributes)) }
}