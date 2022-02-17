This repos is dedicated to the implementation of an ASLR module to Unikraft.

Schedule:
1. ASLR Module :heavy_check_mark:
	* Can be set or not through the menuconfig
	* Shuffles the executable and changes offsets at the linking procedure
	* Randomize stack and heap :wavy_dash:

2. ASLR and memory deduplication compatibility
	* Exploring solutions : gcc or binary writing :wavy_dash:
	--> GOT/PLT

3. Thesis writing
	* Introduction :heavy_check_mark:
	* Motivation and Unikraft description :wavy_dash:
	* State of the art :wavy_dash:
	* ASLR solution
	* ASLR/Memory dup compatibility solution
	* Conclusion


Requires Python3.10+ to work.
