Summary:	Sound processing library
Name:		soundtouch
Version:	1.8.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.surina.net/soundtouch/%{name}-%{version}.tar.gz
# Source0-md5:	d02c6c91cb13901ca273a2b4b143ce41
URL:		http://www.surina.net/soundtouch/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# gcc runs out of regs in mmx_gcc.cpp
%define		specflags_ia32	-fomit-frame-pointer

%description
SoundTouch is a library for changing tempo, pitch and playback rate of
digital sound.

%package devel
Summary:	Header files for SoundTouch library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SoundTouch library.

%package soundstretch
Summary:	SoundStretch - sound processing application
Group:		Applications/Sound
URL:		http://sky.prohosting.com/oparviai/soundtouch/soundstretch.html
Requires:	%{name} = %{version}-%{release}

%description soundstretch
SoundStretch is a command-line application for changing tempo, pitch
and playback rates of WAV sound files. This program also demonstrates
how the "SoundTouch" library can be used to process sound in own
programs.

%prep
%setup -qn %{name}

# unDOS
%{__sed} -i -e 's/\r$//' soundtouch.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/soundtouch
%{_aclocaldir}/soundtouch.m4
%{_pkgconfigdir}/soundtouch.pc

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch

