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
