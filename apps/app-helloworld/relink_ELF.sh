#!/usr/bin/sh

if [ "$#" -ne 3 ]; then
    echo " Script usage : relink_ELF BUILD_DIR NAME_EXEC UNIKRAFT_FOLDER"
else
    libkvm=$1/libkvmplat
    lib=$(python string_script.py "$(make print-libs)")
    #Shuffles the linking script
    $3/support/scripts/ASLR/ASLR.py --file_path=$libkvm/link64.lds --lib_list="$lib" --output_path=$libkvm/link64_ASLR.lds
    gcc -nostdlib -Wl,--omagic -Wl,--build-id=none -nostdinc -no-pie  -Wl,-m,elf_x86_64 -T$libkvm/link64_ASLR.lds -L$1 -o $2.dbg
    python3 $3/support/scripts/sect-strip.py   --with-objcopy=""objcopy $1/$2 -o $2 && ""strip -s $2
fi
