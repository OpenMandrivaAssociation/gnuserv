Summary:        Allows you to attach to an already running Emacs
Name:           gnuserv
Version:        3.12.8
Release:        %mkrel 5
Source0:        http://meltin.net/hacks/emacs/src/%name-%version.tar.bz2
Source1:        emacs-gnuserv-start.el.bz2
Patch1:         gnuserv-3.12.4-configure-destdir.patch.bz2
Patch2:         gnuserv-3.12.5-fixdisplay.patch.bz2
License:        GPL
Group:          Editors
BuildRoot:      %_tmppath/%name-buildroot
BuildRequires:  emacs-nox
Url:            http://meltin.net/hacks/emacs/
Requires:       emacs

%description
gnuserv allows you to attach to an already running Emacs. This allows
external programs to make use of Emacs' editing capabilities. It is
like GNU Emacs' emacsserver/server.el, but has many more features.

You do not need this package if you use XEmacs; it already includes
gnuserv and gnuclient. If you want to use gnuserv with both GNU Emacs
and XEmacs, you will only be able to use the alternative
/usr/bin/gnuclient with one flavor of emacs; you will have to use
either gnuclient.xemacs or gnuclient.emacs for the other flavor.

%prep
%setup -q
%patch1 -p1 -b .configure
%patch2 -p1 -b .fixdisplay

%build
%configure

%install
rm -rf %buildroot
lispdir=%buildroot/%_datadir/emacs/site-lisp/%name
emacsdir=%buildroot%_sysconfdir/emacs/site-start.d
man1dir=%buildroot/%_mandir/man1

mkdir -p $lispdir $man1dir $emacsdir

%makeinstall man1dir=$man1dir
install -m644 devices.elc gnuserv-compat.elc gnuserv.elc $lispdir
bzcat %SOURCE1 > $emacsdir/%name.el

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%config(noreplace) /etc/emacs/site-start.d/%name.el
%_bindir/*
%_datadir/emacs/site-lisp/%name
%_mandir/man1/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.12.8-5mdv2011.0
+ Revision: 619218
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.12.8-4mdv2010.0
+ Revision: 429286
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.12.8-3mdv2009.0
+ Revision: 246505
- rebuild

* Tue Feb 05 2008 Funda Wang <fwang@mandriva.org> 3.12.8-1mdv2008.1
+ Revision: 162531
- update to new version 3.12.8

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Funda Wang <fwang@mandriva.org> 3.12.7-2mdv2008.1
+ Revision: 98741
- Rebuild for new era

  + Emmanuel Andry <eandry@mandriva.org>
    - Import gnuserv



* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 3.12.7-1mdk
- 3.12.7

* Thu Jun 03 2004 Michael Scherer <misc@mandrake.org> 3.12.6-3mdk 
- rebuild for new libintl

* Wed Sep 03 2003 Michael Scherer <scherer.michael@free.fr> 3.12.6-2mdk 
- BuildRequires emacs-nox

* Sun Jul 27 2003 Han Boetes <han@linux-mandrake.com> 3.12.6-1mdk
- Bump
- Cleanups
- Remove .el, gnuserv works fine without them.

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.12.5-3mdk
- buildprereq

* Tue Feb 18 2003 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.12.5-2mdk
- Fix display to another DISPLAY (freebsd patch)(thanks
  han@mijncomputer.nl).

* Tue Jan  7 2003 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.12.5-1mdk
- Requires: emacs.
- Bump to version 3.12.5.

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.12.4-4mdk
- remove useless prefix
- rebuild for new libintl

* Thu Nov 22 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.12.4-3mdk
- Add URL.
- Defalias server-start gnuserv-start when installing.

* Mon Nov 19 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.12.4-2mdk
- Fix DESTDIR with makeinstall.

* Mon Oct  1 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.12.4-1mdk
- First version.

# end of file
