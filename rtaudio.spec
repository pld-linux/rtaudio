Summary:	RtAudio - set of C++ classes providing common API for realtime audio I/O
Summary(pl.UTF-8):   RtAudio - zbiór klas C++ udostępniających wspólne API do we/wy dźwięku
Name:		rtaudio
Version:	3.0.3
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://www.music.mcgill.ca/~gary/rtaudio/release/%{name}-%{version}.tar.gz
# Source0-md5:	dcc08fa6b81971eabacc872acd56319a
URL:		http://www.music.mcgill.ca/~gary/rtaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki RtAudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel
Requires:	jack-audio-connection-kit-devel
Requires:	libstdc++-devel

%description devel
Header files for RtAudio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RtAudio.

%package static
Summary:	Static RtAudio library
Summary(pl.UTF-8):   Statyczna biblioteka RtAudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RtAudio library.

%description static -l pl.UTF-8
Statyczna biblioteka RtAudio.

%prep
%setup -q

%build
#configure is used only for examples

libtool --mode=compile --tag=CXX %{__cxx} -c %{rpmcxxflags} -o RtAudio.lo RtAudio.cpp -D__LINUX_OSS__ -D__LINUX_ALSA__ -D__LINUX_JACK__
libtool --mode=link --tag=CXX %{__cxx} %{rpmldflags} -o librtaudio.la RtAudio.lo -rpath %{_libdir} -ljack -lasound -lpthread

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

libtool --mode=install install librtaudio.la $RPM_BUILD_ROOT%{_libdir}
install RtAudio.h RtError.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme doc/release.txt
%attr(755,root,root) %{_libdir}/librtaudio.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/librtaudio.so
%{_libdir}/librtaudio.la
%{_includedir}/Rt*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librtaudio.a
