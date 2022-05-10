deps_config := \
	/home/terrylos/Thesis/apps/app-helloworld/Config.uk \
	/home/terrylos/Thesis/unikraft/lib/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//vfscore/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uktimeconv/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uktime/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uktest/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukswrand/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uksp/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uksignal/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uksglist/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukschedcoop/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uksched/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukrust/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukring/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uknetdev/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukmpi/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukmmap/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uklock/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uklibparam/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukdebug/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukcpio/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukbus/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukboot/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukblkdev/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukargparse/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukallocregion/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukallocpool/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukallocbbuddy/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ukalloc/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//uk9p/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ubsan/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//syscall_shim/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//ramfs/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//posix-user/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//posix-sysinfo/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//posix-process/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//posix-libdl/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//nolibc/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//isrlib/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//fdt/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//devfs/Config.uk \
	/home/terrylos/Thesis/unikraft/lib//9pfs/Config.uk \
	/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/libs.uk \
	/home/terrylos/Thesis/unikraft/plat/Config.uk \
	/home/terrylos/Thesis/unikraft/plat//xen/Config.uk \
	/home/terrylos/Thesis/unikraft/plat//linuxu/Config.uk \
	/home/terrylos/Thesis/unikraft/plat//kvm/Config.uk \
	/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/plat.uk \
	/home/terrylos/Thesis/unikraft/arch/arm/arm64/Config.uk \
	/home/terrylos/Thesis/unikraft/arch/arm/arm/Config.uk \
	/home/terrylos/Thesis/unikraft/arch/x86/x86_64/Config.uk \
	/home/terrylos/Thesis/unikraft/arch/Config.uk \
	/home/terrylos/Thesis/unikraft/Config.uk

/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: \
	$(deps_config)

ifneq "$(UK_FULLVERSION)" "0.7.0~3e14fc5-custom"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_CODENAME)" "Mimas"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_ARCH)" "x86_64"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_BASE)" "/home/terrylos/Thesis/unikraft"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_APP)" "/home/terrylos/Thesis/apps/app-helloworld"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(UK_NAME)" "app-helloworld"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(CC)" "gcc"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_PLAT_DIR)" "/home/terrylos/Thesis/unikraft/plat//kvm /home/terrylos/Thesis/unikraft/plat//linuxu /home/terrylos/Thesis/unikraft/plat//xen  /home/terrylos/Thesis/unikraft/plat/"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_PLAT_IN)" "/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/plat.uk"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_LIB_DIR)" "/home/terrylos/Thesis/unikraft/lib//9pfs /home/terrylos/Thesis/unikraft/lib//devfs /home/terrylos/Thesis/unikraft/lib//fdt /home/terrylos/Thesis/unikraft/lib//isrlib /home/terrylos/Thesis/unikraft/lib//nolibc /home/terrylos/Thesis/unikraft/lib//posix-libdl /home/terrylos/Thesis/unikraft/lib//posix-process /home/terrylos/Thesis/unikraft/lib//posix-sysinfo /home/terrylos/Thesis/unikraft/lib//posix-user /home/terrylos/Thesis/unikraft/lib//ramfs /home/terrylos/Thesis/unikraft/lib//syscall_shim /home/terrylos/Thesis/unikraft/lib//ubsan /home/terrylos/Thesis/unikraft/lib//uk9p /home/terrylos/Thesis/unikraft/lib//ukalloc /home/terrylos/Thesis/unikraft/lib//ukallocbbuddy /home/terrylos/Thesis/unikraft/lib//ukallocpool /home/terrylos/Thesis/unikraft/lib//ukallocregion /home/terrylos/Thesis/unikraft/lib//ukargparse /home/terrylos/Thesis/unikraft/lib//ukblkdev /home/terrylos/Thesis/unikraft/lib//ukboot /home/terrylos/Thesis/unikraft/lib//ukbus /home/terrylos/Thesis/unikraft/lib//ukcpio /home/terrylos/Thesis/unikraft/lib//ukdebug /home/terrylos/Thesis/unikraft/lib//uklibparam /home/terrylos/Thesis/unikraft/lib//uklock /home/terrylos/Thesis/unikraft/lib//ukmmap /home/terrylos/Thesis/unikraft/lib//ukmpi /home/terrylos/Thesis/unikraft/lib//uknetdev /home/terrylos/Thesis/unikraft/lib//ukring /home/terrylos/Thesis/unikraft/lib//ukrust /home/terrylos/Thesis/unikraft/lib//uksched /home/terrylos/Thesis/unikraft/lib//ukschedcoop /home/terrylos/Thesis/unikraft/lib//uksglist /home/terrylos/Thesis/unikraft/lib//uksignal /home/terrylos/Thesis/unikraft/lib//uksp /home/terrylos/Thesis/unikraft/lib//ukswrand /home/terrylos/Thesis/unikraft/lib//uktest /home/terrylos/Thesis/unikraft/lib//uktime /home/terrylos/Thesis/unikraft/lib//uktimeconv /home/terrylos/Thesis/unikraft/lib//vfscore /home/terrylos/Thesis/unikraft/lib "
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_LIB_IN)" "/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/libs.uk"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif
ifneq "$(KCONFIG_APP_DIR)" "/home/terrylos/Thesis/apps/app-helloworld"
/home/terrylos/Thesis/apps/app-helloworld/build/kconfig/auto.conf: FORCE
endif

$(deps_config): ;
