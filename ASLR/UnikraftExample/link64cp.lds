SECTIONS
{
. = 0x100510;
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
. = ALIGN((1 << 12));
.debug_info 0 :{ *(.debug_info .gnu.linkonce.wi.*) }
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
. = ALIGN((1 << 12));
.debug_str 0 :{ *(.debug_str) }
 _tls_start = .;
.tdata :{ *(.tdata) *(.tdata.*) *(.gnu.linkonce.td.*) }
 _etdata = .;
. = ALIGN((1 << 12));
.debug_typenames 0 :{ *(.debug_typenames) }
. = ALIGN(0x8);
.tbss :{ *(.tbss) *(.tbss.*) *(.gnu.linkonce.tb.*) . = ALIGN(0x8); }
. = ALIGN(0x8);
.comment 0 :{ *(.comment) }
.debug_abbrev 0 :{ *(.debug_abbrev) }
. = ALIGN((1 << 12));
.line 0 :{ *(.line) }
. = ALIGN((1 << 12));
.gnu.attributes 0 :{ KEEP (*(.gnu.attributes)) }
 __eh_frame_start = .;
.eh_frame :{ *(.eh_frame) *(.eh_frame.*) }
 __eh_frame_end = .;
.debug_weaknames 0 :{ *(.debug_weaknames) }
.debug_pubtypes 0 :{ *(.debug_pubtypes) }
 _data = .;
.data :{
  *(.data)
  *(.data.*)
 }
 _edata = .;
 uk_ctortab_start = .;
.uk_ctortab :{ KEEP(*(SORT_BY_NAME(.uk_ctortab[0-9]))) }
 uk_ctortab_end = .;
.debug_ranges 0 :{ *(.debug_ranges) }
.debug_aranges 0 :{ *(.debug_aranges) }
.debug_loc 0 :{ *(.debug_loc) }
.debug_pubnames 0 :{ *(.debug_pubnames) }
.debug_line 0 :{ *(.debug_line .debug_line.* .debug_line_end ) }
 _text = .;
.text :{
  KEEP (*(.data.boot))
  *(.text.boot)
  *(.text)
  *(.text.*)
 }
 _etext = .;
 uk_inittab_start = .;
.uk_inittab :{ KEEP(*(SORT_BY_NAME(.uk_inittab[1-6][0-9]))) }
 uk_inittab_end = .;
.debug_macro 0 :{ *(.debug_macro) }
 __eh_frame_hdr_start = .;
.eh_frame_hdr :{ *(.eh_frame_hdr) *(.eh_frame_hdr.*) }
 __eh_frame_hdr_end = .;
.debug_sfnames 0 :{ *(.debug_sfnames) }
.debug_frame 0 :{ *(.debug_frame) }
.debug_varnames 0 :{ *(.debug_varnames) }
.debug_macinfo 0 :{ *(.debug_macinfo) }
 _rodata = .;
.rodata :{
  *(.rodata)
  *(.rodata.*)
 }
 _erodata = .;
.debug_funcnames 0 :{ *(.debug_funcnames) }
.debug 0 :{ *(.debug) }
.debug_srcinfo 0 :{ *(.debug_srcinfo) }
}
