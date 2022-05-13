#/bin/bash

for i in {1..25}
do
 make clean;make -j12
 cp ./build/app-helloworld_kvm-x86_64 ./../entropy/size_measures/app-helloworld_kvm-x86_64-$i
done
