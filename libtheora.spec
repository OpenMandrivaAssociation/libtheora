%define _disable_ld_no_undefined 1

%define major 1
%define decmajor 2
%define encmajor 2
%define libname %mklibname theora
%define oldlibname %mklibname theora 0
%define libnamedec %mklibname theoradec
%define oldlibnamedec %mklibname theoradec 1
%define libnameenc %mklibname theoraenc
%define oldlibnameenc %mklibname theoraenc 1
%define develname %mklibname -d theora
#define beta alpha1

Summary:	Theora video compression codec
Name:		libtheora
Version:	1.2.0
Release:	%{?beta:0.%{beta}.}2
License:	BSD
Group:		Video
Url:		https://www.theora.org/
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.gz
#gw this is from texlive, it is not part of tetex
Source1:	ltablex.sty
#Patch0:		libtheora-1.1.1-libpng16.patch
#Patch1:		libtheora-1.1.1-fix-underlinking.patch
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
%rename %{oldlibname}

%description -n %{libname}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnamedec}
Summary:	Theora video decoder
Group:		System/Libraries
%rename %{oldlibnamedec}

%description -n %{libnamedec}
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.

%package -n %{libnameenc}
Summary:	Theora video encoder
Group:		System/Libraries
%rename %{oldlibnameenc}

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
%setup -qn %{name}-%{version}
#patch0 -p0 -b .p0~
#patch1 -p1 -b .p1~
cp %{SOURCE1} doc/spec/
%before_configure
./autogen.sh

%build
# remove fforce-addr
# clang does not like it
sed -i 's/-fforce-addr//g' configure
%configure \
	--disable-static

%make_build

%install
%make_install docdir=%{_datadir}/doc/libtheora
mv %{buildroot}%{_datadir}/doc/libtheora installed-docs
rm -f installed-docs/doxygen-build.stamp

mkdir -p %{buildroot}/%{_bindir}
install -m 755 examples/.libs/dump_video %{buildroot}/%{_bindir}/theora_dump_video
install -m 755 examples/.libs/encoder_example %{buildroot}/%{_bindir}/theora_encode
install -m 755 examples/.libs/player_example %{buildroot}/%{_bindir}/theora_player

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
