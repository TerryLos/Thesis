ENTRY(_libkvmplat_entry)
SECTIONS
{
. = 0x100E38;
.debug_loc 0 :{ *(.debug_loc) }
. = ALIGN((1 << 12));
 _rodata = .;
.rodata :{
  *(.rodata)
  *(.rodata.*)
 }
 _erodata = .;
.line 0 :{ *(.line) }
. = ALIGN((1 << 12));
.debug_weaknames 0 :{ *(.debug_weaknames) }
.debug_srcinfo 0 :{ *(.debug_srcinfo) }
. = ALIGN((1 << 12));
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
. = ALIGN(0x8);
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
. = ALIGN(0x8);
 __eh_frame_start = .;
.eh_frame :{ *(.eh_frame) *(.eh_frame.*) }
 __eh_frame_end = .;
. = ALIGN((1 << 12));
 _tls_start = .;
.tdata :{ *(.tdata) *(.tdata.*) *(.gnu.linkonce.td.*) }
 _etdata = .;
.tbss :{ *(.tbss) *(.tbss.*) *(.gnu.linkonce.tb.*) . = ALIGN(0x8); }
 _tls_end = . + SIZEOF(.tbss);
. = ALIGN((1 << 12));
.gnu.attributes 0 :{ KEEP (*(.gnu.attributes)) }
.debug_info 0 :{ *(.debug_info .gnu.linkonce.wi.*) }
.debug_aranges 0 :{ *(.debug_aranges) }
.debug_macro 0 :{ *(.debug_macro) }
.debug_varnames 0 :{ *(.debug_varnames) }
.debug_ranges 0 :{ *(.debug_ranges) }
.debug_abbrev 0 :{ *(.debug_abbrev) }
 _text = .;
.text :{
  KEEP (*(.data.boot))
  *(.text.boot)
  *(.text)
  *(.text.*)
 }
 _etext = .;
.debug_macinfo 0 :{ *(.debug_macinfo) }
 __eh_frame_hdr_start = .;
.eh_frame_hdr :{ *(.eh_frame_hdr) *(.eh_frame_hdr.*) }
 __eh_frame_hdr_end = .;
 uk_ctortab_start = .;
.uk_ctortab :{ KEEP(*(SORT_BY_NAME(.uk_ctortab[0-9]))) }
 uk_ctortab_end = .;
.debug_frame 0 :{ *(.debug_frame) }
.debug_typenames 0 :{ *(.debug_typenames) }
.debug_line 0 :{ *(.debug_line .debug_line.* .debug_line_end ) }
.debug_str 0 :{ *(.debug_str) }
.debug_pubnames 0 :{ *(.debug_pubnames) }
.comment 0 :{ *(.comment) }
 _data = .;
.data :{
  *(.data)
  *(.data.*)
 }
 _edata = .;
.debug_sfnames 0 :{ *(.debug_sfnames) }
 uk_inittab_start = .;
.uk_inittab :{ KEEP(*(SORT_BY_NAME(.uk_inittab[1-6][0-9]))) }
 uk_inittab_end = .;
.debug 0 :{ *(.debug) }
.debug_pubtypes 0 :{ *(.debug_pubtypes) }
.debug_funcnames 0 :{ *(.debug_funcnames) }
}
