

top_builddir=.
top_srcdir=.
srcdir=.

DESTDIR=

include ./Make.rules

DIRS=$(top_srcdir)/lib/libcap
EXEEXT=
INSTALL_DEPS=
LIBTOOL_DEPS=.//ltmain.sh
LIBLTDL=

MAIN_LDFLAGS=
MAIN_LIBS=

BUILD_PROFTPD_OBJS=$(BUILD_OBJS) $(BUILD_STATIC_MODULE_OBJS)
BUILD_PROFTPD_ARCHIVES=$(BUILD_STATIC_MODULE_ARCHIVES)
BUILD_BIN=proftpd$(EXEEXT) ftpcount$(EXEEXT) ftpdctl$(EXEEXT) ftpscrub$(EXEEXT) ftpshut$(EXEEXT) ftptop$(EXEEXT) ftpwho$(EXEEXT)


all: $(BUILD_BIN)

include/buildstamp.h:
	echo \#define BUILD_STAMP \"`date +"%a %b %e %Y %H:%M:%S %Z"`\" > include/buildstamp.h

dummy:

lib: include/buildstamp.h dummy
	cd lib/ && $(MAKE) lib

src: include/buildstamp.h dummy
	cd src/ && $(MAKE) src

modules: include/buildstamp.h dummy
	cd modules/ && $(MAKE) static
	test -z "$(SHARED_MODULE_OBJS)" -a -z "$(SHARED_MODULE_DIRS)" || (cd modules/ && $(MAKE) shared)

utils: include/buildstamp.h dummy
	cd utils/ && $(MAKE) utils

locale: include/buildstamp.h dummy
	test -z "$(ENABLE_NLS)" || (cd locale/ && $(MAKE) locale)

dirs: include/buildstamp.h dummy
	@dirs="$(DIRS)"; \
	for dir in $$dirs; do \
		if [ -d "$$dir" ]; then cd $$dir/ && $(MAKE); fi; \
	done

proftpd$(EXEEXT): lib src modules dirs locale
	$(LIBTOOL) --mode=link --tag=CC $(CC) $(LDFLAGS) $(MAIN_LDFLAGS) -o $@ $(BUILD_PROFTPD_OBJS) $(BUILD_PROFTPD_ARCHIVES) $(LIBS) $(MAIN_LIBS)

ftpcount$(EXEEXT): lib utils
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPCOUNT_OBJS) $(UTILS_LIBS)

ftpdctl$(EXEEXT): lib src
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPDCTL_OBJS) $(LIBS)

ftpscrub$(EXEEXT): lib utils
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPSCRUB_OBJS) $(UTILS_LIBS)

ftpshut$(EXEEXT): lib utils
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPSHUT_OBJS) $(UTILS_LIBS)

ftptop$(EXEEXT): lib utils
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPTOP_OBJS) $(CURSES_LIBS) $(UTILS_LIBS)

ftpwho$(EXEEXT): lib utils
	$(CC) $(LDFLAGS) -o $@ $(BUILD_FTPWHO_OBJS) $(UTILS_LIBS)

check: proftpd$(EXEEXT)
	test -z "$(ENABLE_TESTS)" || (cd tests/ && $(MAKE) check)

# BSD install -d doesn't work, so ...
$(DESTDIR)$(localedir) $(DESTDIR)$(includedir) $(DESTDIR)$(includedir)/proftpd $(DESTDIR)$(libdir) $(DESTDIR)$(pkgconfigdir) $(DESTDIR)$(libdir)/proftpd $(DESTDIR)$(libexecdir) $(DESTDIR)$(localstatedir) $(DESTDIR)$(sysconfdir) $(DESTDIR)$(bindir) $(DESTDIR)$(sbindir) $(DESTDIR)$(mandir) $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(mandir)/man5 $(DESTDIR)$(mandir)/man8:
	@if [ ! -d $@ ]; then \
		mkdir -p $@; \
		chown $(INSTALL_USER):$(INSTALL_GROUP) $@; \
		chmod 0755 $@; \
	fi

install-proftpd: proftpd $(DESTDIR)$(includedir) $(DESTDIR)$(localstatedir) $(DESTDIR)$(sysconfdir) $(DESTDIR)$(sbindir)
	$(INSTALL_SBIN) proftpd $(DESTDIR)$(sbindir)/proftpd
	if [ -f $(DESTDIR)$(sbindir)/in.proftpd ] ; then \
		rm -f $(DESTDIR)$(sbindir)/in.proftpd ; \
	fi
	ln -s proftpd $(DESTDIR)$(sbindir)/in.proftpd
	-chown -h $(INSTALL_USER):$(INSTALL_GROUP) $(DESTDIR)$(sbindir)/in.proftpd

install-libs: $(DESTDIR)$(libdir)/proftpd
	cd lib/ && $(MAKE) install

install-headers: $(DESTDIR)$(includedir)/proftpd
	$(INSTALL_MAN) config.h $(DESTDIR)$(includedir)/proftpd/config.h
	cd include/ && $(MAKE) install

install-pkgconfig: $(DESTDIR)$(pkgconfigdir)
	@echo 'prefix=$(prefix)' > proftpd.pc
	@echo 'exec_prefix=$${prefix}' >> proftpd.pc
	@echo 'libdir=$${prefix}/lib/proftpd' >> proftpd.pc
	@echo 'includedir=$${prefix}/include/proftpd' >> proftpd.pc
	@echo '' >> proftpd.pc
	@echo 'Name: ProFTPD' >> proftpd.pc
	@echo 'Description: Professional FTP Daemon' >> proftpd.pc
	@echo 'Version: $(VERSION)' >> proftpd.pc
	@echo 'Requires: ' >> proftpd.pc
	@echo 'Libs: -L$${libdir}' >> proftpd.pc
	@echo 'Cflags: -I$${includedir}' >> proftpd.pc
	$(INSTALL_MAN) proftpd.pc $(DESTDIR)$(pkgconfigdir)/proftpd.pc

install-locales: $(DESTDIR)$(localedir)
	test -z "$(ENABLE_NLS)" || (cd locale/ && $(MAKE) install)

install-modules: $(DESTDIR)$(libexecdir) $(DESTDIR)$(sysconfdir)
	test -z "$(SHARED_MODULE_OBJS)" -a -z "$(SHARED_MODULE_DIRS)" -a -z "$(STATIC_MODULE_DIRS)" || (cd modules/ && $(MAKE) install)

install-utils: $(DESTDIR)$(sbindir) $(DESTDIR)$(bindir)
	$(INSTALL_BIN)  ftpcount $(DESTDIR)$(bindir)/ftpcount
	$(INSTALL_BIN)  ftpdctl  $(DESTDIR)$(bindir)/ftpdctl
	$(INSTALL_SBIN) ftpscrub $(DESTDIR)$(sbindir)/ftpscrub
	$(INSTALL_SBIN) ftpshut  $(DESTDIR)$(sbindir)/ftpshut
	$(INSTALL_BIN)  ftptop   $(DESTDIR)$(bindir)/ftptop
	$(INSTALL_BIN)  ftpwho   $(DESTDIR)$(bindir)/ftpwho
	$(INSTALL) -o $(INSTALL_USER) -g $(INSTALL_GROUP) -m 0755 src/prxs $(DESTDIR)$(bindir)/prxs

install-conf: $(DESTDIR)$(sysconfdir)
	if [ ! -f $(DESTDIR)$(sysconfdir)/proftpd.conf ] ; then \
		$(INSTALL) -o $(INSTALL_USER) -g $(INSTALL_GROUP) -m 0644 \
		           $(top_srcdir)/sample-configurations/basic.conf \
	       	           $(DESTDIR)$(sysconfdir)/proftpd.conf ; \
	fi

install-libltdl:
	cd lib/libltdl/ && $(MAKE) install

install-man: $(DESTDIR)$(mandir) $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(mandir)/man5 $(DESTDIR)$(mandir)/man8
	$(INSTALL_MAN) $(top_srcdir)/src/ftpdctl.8    $(DESTDIR)$(mandir)/man8
	$(INSTALL_MAN) $(top_srcdir)/src/proftpd.8    $(DESTDIR)$(mandir)/man8
	$(INSTALL_MAN) $(top_srcdir)/utils/ftpscrub.8 $(DESTDIR)$(mandir)/man8
	$(INSTALL_MAN) $(top_srcdir)/utils/ftpshut.8  $(DESTDIR)$(mandir)/man8
	$(INSTALL_MAN) $(top_srcdir)/utils/ftpcount.1 $(DESTDIR)$(mandir)/man1
	$(INSTALL_MAN) $(top_srcdir)/utils/ftptop.1   $(DESTDIR)$(mandir)/man1
	$(INSTALL_MAN) $(top_srcdir)/utils/ftpwho.1   $(DESTDIR)$(mandir)/man1
	$(INSTALL_MAN) $(top_srcdir)/src/xferlog.5    $(DESTDIR)$(mandir)/man5

install-all: install-proftpd install-modules install-utils install-conf install-man install-libs install-headers install-pkgconfig install-locales $(INSTALL_DEPS)

install: all install-all

depend:
	cd src/     && $(MAKE) depend
	cd modules/ && $(MAKE) depend
	cd lib/     && $(MAKE) depend
	cd utils/   && $(MAKE) depend

clean:
	cd src/     && $(MAKE) clean
	cd modules/ && $(MAKE) clean
	cd lib/     && $(MAKE) clean
	cd utils/   && $(MAKE) clean
	cd locale/  && $(MAKE) clean
	test -z "$(ENABLE_TESTS)" || (cd tests/ && $(MAKE) clean)

	@dirs="$(DIRS)"; \
	for dir in $$dirs; do \
		if [ -d "$$dir" ]; then cd $$dir/ && $(MAKE) clean; fi; \
	done

	rm -f proftpd.pc include/buildstamp.h
	rm -f $(BUILD_BIN)

distclean: clean
	cd lib/ && $(MAKE) distclean
	rm -f Makefile Make.modules Make.rules \
	      lib/Makefile locale/Makefile modules/Makefile src/Makefile \
              utils/Makefile
	rm -f config.h config.status config.cache config.log libtool stamp-h
	rm -f include/buildstamp.h
	rm -rf .libs/

dist: depend distclean
	rm -rf `find . -name CVS`
	rm -rf `find . -name .cvsignore`
	rm -rf `find . -name core`
	rm -rf `find . -name '*~'`
	rm -fr `find . -name '*.bak'`
	# RPM needs this in the top-level directory in order to support '-t'
	mv -f contrib/dist/rpm/proftpd.spec .
	# Other users may need to execute these scripts
	chmod a+x configure config.sub install-sh modules/glue.sh


# autoheader might not change config.h.in, so touch a stamp file.
${srcdir}/config.h.in: stamp-h.in
${srcdir}/stamp-h.in: configure.in acconfig.h
	cd ${srcdir} && autoheader
	echo timestamp > ${srcdir}/stamp-h.in

config.h: stamp-h
stamp-h: config.h.in config.status
	./config.status

# This target tends to cause more problems than its worth; there are many
# differences between autoconf versions, installed macros, etc between the
# machine used to generate the shipping configure script and the machine on
# which this target might trigger.  So try to keep the craziness down by
# avoiding this altogether.
#${srcdir}/configure: configure.in
#	cd ${srcdir} && autoconf

Make.rules: Make.rules.in config.status
	./config.status

Makefile: Makefile.in Make.rules.in config.status
	./config.status

config.status: configure
	./config.status --recheck

libtool: $(LIBTOOL_DEPS)
	$(SHELL) ./config.status --recheck
