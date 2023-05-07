Summary:	RtAudio - set of C++ classes providing common API for realtime audio I/O
Summary(pl.UTF-8):	RtAudio - zbiór klas C++ udostępniających wspólne API do we/wy dźwięku
Name:		rtaudio
Version:	5.2.0
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://www.music.mcgill.ca/~gary/rtaudio/release/%{name}-%{version}.tar.gz
# Source0-md5:	2482b10c83b5376348b39b81359db447
Patch0:		%{name}-libdir.patch
URL:		http://www.music.mcgill.ca/~gary/rtaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.14
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RtAudio - a set of C++ classes which provide a common API for realtime
audio input/output across Linux (native ALSA, JACK, and OSS), SGI,
Macintosh OS X (CoreAudio), and Windows (DirectSound and ASIO)
operating systems.

%description -l pl.UTF-8
RtAudio to zbiór klas C++ udostępniających wspólne API dla
wejścia/wyjścia dźwięku w czasie rzeczywistym na systemach
operacyjnych Linux (natywna ALSA, JACK, OSS), SGI, MacOS X (CoreAudio)
i Windows (DirectSound i ASIO).

%package devel
Summary:	Header files for RtAudio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RtAudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel
Requires:	jack-audio-connection-kit-devel
Requires:	libstdc++-devel >= 6:4.7
Requires:	pulseaudio-devel

%description devel
Header files for RtAudio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RtAudio.

%package static
Summary:	Static RtAudio library
Summary(pl.UTF-8):	Statyczna biblioteka RtAudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RtAudio library.

%description static -l pl.UTF-8
Statyczna biblioteka RtAudio.

%package apidocs
Summary:	API documentation for RtAudio library
Summary(pl.UTF-8):	Dokumentacja API biblioteki RtAudio
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for RtAudio library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki RtAudio.

%prep
%setup -q
%patch0 -p1

# missing in dist, restore from autoconf-archive
install -d m4
cp -p /usr/share/aclocal/ax_cxx_compile_stdcxx.m4 m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-alsa \
	--with-jack \
	--with-pulse
# NOTE: --with-oss is broken on Linux currently

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librtaudio.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md doc/release.txt
%attr(755,root,root) %{_libdir}/librtaudio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtaudio.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtaudio.so
%{_includedir}/rtaudio
%{_pkgconfigdir}/rtaudio.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librtaudio.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
