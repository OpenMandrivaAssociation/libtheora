%define _disable_ld_no_undefined 1

%define name libtheora
%define version 1.1.1
%define fversion %{version}
%define release %mkrel 3
%define major 0
%define decmajor 1
%define encmajor 1
%define libname %mklibname theora %major
%define libnamedec %mklibname theoradec %decmajor
%define libnameenc %mklibname theoraenc %decmajor
%define develname %mklibname -d theora

Summary: Theora video compression codec
Name: %{name}
Version: %{version}
Release: 4
Source0: http://downloads.xiph.org/releases/theora/%{name}-%{fversion}.tar.bz2
#gw this is from texlive, it is not part of tetex
Source1: ltablex.sty
URL: http://www.theora.org/
License: BSD
Group: Video
BuildRequires: automake >= 1.7.9
BuildRequires: autoconf2.5 >= 2.54
BuildRequires: libvorbis-devel >= 1.0.1
BuildRequires: libSDL-devel
BuildRequires: zlib-devel

%description
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libname}
Summary: Theora video compression codec
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnamedec}
Summary: Theora video decoder
Group: System/Libraries

%description -n %{libnamedec}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnameenc}
Summary: Theora video encoder
Group: System/Libraries

%description -n %{libnameenc}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %develname
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: libogg-devel >= 1.0.1
Requires: %libname = %version
Requires: %libnameenc = %version
Requires: %libnamedec = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d theora 0

%description -n %develname
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n theora-tools
Summary: Command line tools for Theora videos
Group: Video
Requires: %libname = %version

%description -n theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.define	name	vorbis-tools

%prep
%setup -q -n %name-%fversion
cp %SOURCE1 doc/spec/

%build
%configure2_5x
%make

%install
%makeinstall_std docdir=%_datadir/doc/libtheora
mv %buildroot%_datadir/doc/libtheora installed-docs
rm -f installed-docs/doxygen-build.stamp

mkdir -p %{buildroot}/%{_bindir}
install -m 755 examples/.libs/dump_video %{buildroot}/%{_bindir}/theora_dump_video
install -m 755 examples/.libs/encoder_example %{buildroot}/%{_bindir}/theora_encode
install -m 755 examples/.libs/player_example %{buildroot}/%{_bindir}/theora_player

%check
make check

%if %mdkversion < 200900
%post   -n %{libname}	-p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname}	-p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post   -n %{libnamedec}	-p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libnamedec}	-p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post   -n %{libnameenc}	-p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libnameenc}	-p /sbin/ldconfig
%endif


%files -n %libname
%doc README COPYING
%_libdir/libtheora.so.%{major}*

%files -n %libnamedec
%doc README COPYING
%_libdir/libtheoradec.so.%{decmajor}*

%files -n %libnameenc
%doc README COPYING
%_libdir/libtheoraenc.so.%{encmajor}*

%files -n theora-tools
%{_bindir}/*

%files -n %develname
%doc installed-docs/*
%_includedir/theora
%_libdir/libtheora*a
%_libdir/libtheora*so
%_libdir/pkgconfig/theora.pc
%_libdir/pkgconfig/theoradec.pc
%_libdir/pkgconfig/theoraenc.pc
