#!/bin/bash

size=0
for i in {1..25}
do
image=app-helloworld_kvm-x86_64-$i
((size+=$(stat -c%s "$image")))
done
avgSize=$(($size/25))
normalSize=$(stat -c%s app-helloworld_kvm-x86_64)
echo ASLR:$avgSize bytes "|" NO_ASLR:$normalSize bytes
