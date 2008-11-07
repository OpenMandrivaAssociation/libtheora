%define _disable_ld_no_undefined 1

%define name libtheora
%define version 1.0
%define fversion %{version}
%define release %mkrel 2
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
Release: %{release}
Source0: http://downloads.xiph.org/releases/theora/%{name}-%{fversion}.tar.bz2
#gw this is from texlive, it is not part of tetex
Source1: ltablex.sty
URL: http://www.theora.org/
License: BSD
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: automake1.7 >= 1.7.9
BuildRequires: autoconf2.5 >= 2.54
BuildRequires: libvorbis-devel >= 1.0.1
BuildRequires: libSDL-devel

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

%prep
%setup -q -n %name-%fversion
cp %SOURCE1 doc/spec/

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std docdir=%_datadir/doc/libtheora
mv %buildroot%_datadir/doc/libtheora installed-docs
rm -f installed-docs/doxygen-build.stamp

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

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
%defattr(-,root,root)
%doc README COPYING
%_libdir/libtheora.so.%{major}*

%files -n %libnamedec
%defattr(-,root,root)
%doc README COPYING
%_libdir/libtheoradec.so.%{decmajor}*

%files -n %libnameenc
%defattr(-,root,root)
%doc README COPYING
%_libdir/libtheoraenc.so.%{encmajor}*


%files -n %develname
%defattr(-,root,root)
%doc installed-docs/*
%_includedir/theora
%_libdir/libtheora*a
%_libdir/libtheora*so
%_libdir/pkgconfig/theora.pc
%_libdir/pkgconfig/theoradec.pc
%_libdir/pkgconfig/theoraenc.pc
