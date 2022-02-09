deps_config := \
	/home/terrylos/thesis/unikraft/build/app.uk \
	/home/terrylos/thesis/unikraft/lib/Config.uk \
	/home/terrylos/thesis/unikraft/lib//vfscore/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uktimeconv/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uktime/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uktest/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukswrand/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uksp/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uksignal/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uksglist/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukschedcoop/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uksched/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukrust/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukring/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uknetdev/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukmpi/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukmmap/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uklock/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uklibparam/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukdebug/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukcpio/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukbus/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukboot/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukblkdev/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukargparse/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukallocregion/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukallocpool/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukallocbbuddy/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ukalloc/Config.uk \
	/home/terrylos/thesis/unikraft/lib//uk9p/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ubsan/Config.uk \
	/home/terrylos/thesis/unikraft/lib//syscall_shim/Config.uk \
	/home/terrylos/thesis/unikraft/lib//ramfs/Config.uk \
	/home/terrylos/thesis/unikraft/lib//posix-user/Config.uk \
	/home/terrylos/thesis/unikraft/lib//posix-sysinfo/Config.uk \
	/home/terrylos/thesis/unikraft/lib//posix-process/Config.uk \
	/home/terrylos/thesis/unikraft/lib//posix-libdl/Config.uk \
	/home/terrylos/thesis/unikraft/lib//nolibc/Config.uk \
	/home/terrylos/thesis/unikraft/lib//isrlib/Config.uk \
	/home/terrylos/thesis/unikraft/lib//fdt/Config.uk \
	/home/terrylos/thesis/unikraft/lib//devfs/Config.uk \
	/home/terrylos/thesis/unikraft/lib//9pfs/Config.uk \
	/home/terrylos/thesis/unikraft/build/kconfig/libs.uk \
	/home/terrylos/thesis/unikraft/plat/Config.uk \
	/home/terrylos/thesis/unikraft/plat//xen/Config.uk \
	/home/terrylos/thesis/unikraft/plat//linuxu/Config.uk \
	/home/terrylos/thesis/unikraft/plat//kvm/Config.uk \
	/home/terrylos/thesis/unikraft/build/kconfig/plat.uk \
	/home/terrylos/thesis/unikraft/arch/arm/arm64/Config.uk \
	/home/terrylos/thesis/unikraft/arch/arm/arm/Config.uk \
	/home/terrylos/thesis/unikraft/arch/x86/x86_64/Config.uk \
	/home/terrylos/thesis/unikraft/arch/Config.uk \
	/home/terrylos/thesis/unikraft/Config.uk

/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: \
	$(deps_config)

ifneq "$(UK_FULLVERSION)" "0.7.0~594b73c"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_CODENAME)" "Mimas"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_ARCH)" "x86_64"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_BASE)" "/home/terrylos/thesis/unikraft"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_APP)" "/home/terrylos/thesis/unikraft"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_NAME)" "unikraft"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(CC)" "gcc"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_PLAT_DIR)" "/home/terrylos/thesis/unikraft/plat//kvm /home/terrylos/thesis/unikraft/plat//linuxu /home/terrylos/thesis/unikraft/plat//xen  /home/terrylos/thesis/unikraft/plat/"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_PLAT_IN)" "/home/terrylos/thesis/unikraft/build/kconfig/plat.uk"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_LIB_DIR)" "/home/terrylos/thesis/unikraft/lib//9pfs /home/terrylos/thesis/unikraft/lib//devfs /home/terrylos/thesis/unikraft/lib//fdt /home/terrylos/thesis/unikraft/lib//isrlib /home/terrylos/thesis/unikraft/lib//nolibc /home/terrylos/thesis/unikraft/lib//posix-libdl /home/terrylos/thesis/unikraft/lib//posix-process /home/terrylos/thesis/unikraft/lib//posix-sysinfo /home/terrylos/thesis/unikraft/lib//posix-user /home/terrylos/thesis/unikraft/lib//ramfs /home/terrylos/thesis/unikraft/lib//syscall_shim /home/terrylos/thesis/unikraft/lib//ubsan /home/terrylos/thesis/unikraft/lib//uk9p /home/terrylos/thesis/unikraft/lib//ukalloc /home/terrylos/thesis/unikraft/lib//ukallocbbuddy /home/terrylos/thesis/unikraft/lib//ukallocpool /home/terrylos/thesis/unikraft/lib//ukallocregion /home/terrylos/thesis/unikraft/lib//ukargparse /home/terrylos/thesis/unikraft/lib//ukblkdev /home/terrylos/thesis/unikraft/lib//ukboot /home/terrylos/thesis/unikraft/lib//ukbus /home/terrylos/thesis/unikraft/lib//ukcpio /home/terrylos/thesis/unikraft/lib//ukdebug /home/terrylos/thesis/unikraft/lib//uklibparam /home/terrylos/thesis/unikraft/lib//uklock /home/terrylos/thesis/unikraft/lib//ukmmap /home/terrylos/thesis/unikraft/lib//ukmpi /home/terrylos/thesis/unikraft/lib//uknetdev /home/terrylos/thesis/unikraft/lib//ukring /home/terrylos/thesis/unikraft/lib//ukrust /home/terrylos/thesis/unikraft/lib//uksched /home/terrylos/thesis/unikraft/lib//ukschedcoop /home/terrylos/thesis/unikraft/lib//uksglist /home/terrylos/thesis/unikraft/lib//uksignal /home/terrylos/thesis/unikraft/lib//uksp /home/terrylos/thesis/unikraft/lib//ukswrand /home/terrylos/thesis/unikraft/lib//uktest /home/terrylos/thesis/unikraft/lib//uktime /home/terrylos/thesis/unikraft/lib//uktimeconv /home/terrylos/thesis/unikraft/lib//vfscore /home/terrylos/thesis/unikraft/lib "
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_LIB_IN)" "/home/terrylos/thesis/unikraft/build/kconfig/libs.uk"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_APP_DIR)" "/home/terrylos/thesis/unikraft"
/home/terrylos/thesis/unikraft/build/kconfig/auto.conf: FORCE
endif

$(deps_config): ;
