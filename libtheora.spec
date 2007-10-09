%define name libtheora
%define version 1.0
%define pre beta1
%define fversion %version%pre
%define rel 0.%pre.1
%define release %mkrel %rel
%define major 0
%define libname %mklibname theora %major
%define develname %mklibname -d theora
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary: Theora video compression codec
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.xiph.org/releases/theora/%{name}-%{fversion}.tar.gz
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

%description -n %{libname}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %develname
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: libogg-devel >= 1.0.1
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d theora 0


%description -n %develname
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %name-%fversion

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std docdir=%_datadir/doc/libtheora
mv %buildroot%_datadir/doc/libtheora installed-docs
rm -f installed-docs/doxygen-build.stamp

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n %{libname}	-p /sbin/ldconfig
%postun -n %{libname}	-p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/libtheora*.so.%{major}*

%doc README COPYING
%files -n %develname
%defattr(-,root,root)
%doc installed-docs/*
%_includedir/theora
%_libdir/libtheora*a
%_libdir/libtheora*so
%_libdir/pkgconfig/theora.pc
