%define _disable_ld_no_undefined 1

%define major 0
%define decmajor 1
%define encmajor 1
%define libname %mklibname theora %{major}
%define libnamedec %mklibname theoradec %{decmajor}
%define libnameenc %mklibname theoraenc %{encmajor}
%define develname %mklibname -d theora

Summary:	Theora video compression codec
Name:		libtheora
Version:	1.1.1
Release:	7
License:	BSD
Group:		Video
URL:		http://www.theora.org/
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
#gw this is from texlive, it is not part of tetex
Source1:	ltablex.sty
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(vorbis) >= 1.0.1
BuildRequires:	pkgconfig(zlib)

%description
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libname}
Summary:	Theora video compression codec
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnamedec}
Summary:	Theora video decoder
Group:		System/Libraries

%description -n %{libnamedec}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnameenc}
Summary:	Theora video encoder
Group:		System/Libraries

%description -n %{libnameenc}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libnameenc} = %{version}
Requires:	%{libnamedec} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d theora 0} < 1.1.1-5

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n theora-tools
Summary:	Command line tools for Theora videos
Group:		Video

%description -n theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.define name vorbis-tools

%prep
%setup -q
cp %{SOURCE1} doc/spec/

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std docdir=%{_datadir}/doc/libtheora
mv %{buildroot}%{_datadir}/doc/libtheora installed-docs
rm -f installed-docs/doxygen-build.stamp

mkdir -p %{buildroot}/%{_bindir}
install -m 755 examples/.libs/dump_video %{buildroot}/%{_bindir}/theora_dump_video
install -m 755 examples/.libs/encoder_example %{buildroot}/%{_bindir}/theora_encode
install -m 755 examples/.libs/player_example %{buildroot}/%{_bindir}/theora_player

%check
make check

%files -n %{libname}
%{_libdir}/libtheora.so.%{major}*

%files -n %{libnamedec}
%{_libdir}/libtheoradec.so.%{decmajor}*

%files -n %{libnameenc}
%{_libdir}/libtheoraenc.so.%{encmajor}*

%files -n theora-tools
%{_bindir}/*

%files -n %{develname}
%doc installed-docs/*
%{_includedir}/theora
%{_libdir}/libtheora*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/pkgconfig/theoraenc.pc



%changelog
* Wed Apr 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-5
+ Revision: 793422
- rebuild for .la files
- disable spec
- cleaned up spec

* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-4
+ Revision: 732010
- added theora-tools package and new packaging policy fixes in spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3
+ Revision: 661533
- mass rebuild

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2011.0
+ Revision: 627715
- don't force the usage of automake1.7

* Fri Nov 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 460833
- new version

* Fri Sep 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 449247
- Fix BuildRequires
- update to new version 1.1.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-3mdv2010.0
+ Revision: 425755
- rebuild

* Fri Nov 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-2mdv2009.1
+ Revision: 300809
- provide libtheora by library subpackage

* Tue Nov 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1mdv2009.1
+ Revision: 299912
- new version
- remove patch

* Mon Nov 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.rc2.1mdv2009.1
+ Revision: 299449
- new version
- drop patch

* Thu Oct 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.rc1.1mdv2009.1
+ Revision: 294201
- add missing file
- new version

* Tue Aug 19 2008 Emmanuel Andry <eandry@mandriva.org> 1.0-0.beta3.2mdv2009.0
+ Revision: 273926
- enable _disable_ld_no_undefined

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.beta3.1mdv2009.0
+ Revision: 207511
- new version
- add missing LaTeX style for documentation build
- add new libs theoradec and theoraenc
- enable checks

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.beta2.1mdv2008.1
+ Revision: 101110
- new version

* Tue Oct 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.beta1.1mdv2008.1
+ Revision: 96167
- new version
- new devel name

* Sat Jun 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-0.alpha7.1mdv2008.0
+ Revision: 43409
- Import libtheora



* Thu Jun 22 2006 Götz Waschk <waschk@mandriva.org> 1.0-0.alpha7.1mdv2007.0
- new version

* Fri Jun  9 2006 Götz Waschk <waschk@mandriva.org> 1.0-0.alpha6.1mdv2007.0
- drop patches
- new version

* Wed Sep  7 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.alpha5.1mdk
- rediff patch 0
- new version

* Thu May 12 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.alpha4.2mdk
- rebuild

* Mon Apr 25 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.alpha4.1mdk
- mkrel
- libification
- rediff patch 0
- new version

* Wed Sep 29 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-0.alpha3.3mdk
- lib64 fixes
- build static library with PIC as it can be built into a DSO

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.alpha3.2mdk
- fix buildrequires
- fix URL

* Fri Apr  2 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.alpha3.1mdk
- initial package
