Summary:	libPropList library
Summary(pl):	Biblioteka libPropList
Name:		libPropList
Version:	0.8.3
Release:	5
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
libPropList library, needed by Window Maker.

%description -l pl
libPropList jest bibliotek± wymagan± przez Window Maker'a.

%package devel
Summary:	libPropList libraries
Summary(pl):	Biblioteki libPropList
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
libPropList headers files

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki niezbêdne do tworzenia
aplikacji korzystaj±cych z biblioteki libPropList. 

%package static
Summary:	libPropList static libraries
Summary(pl):	Biblioteki statyczne libPropList
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building libPropList
applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbêdne do tworzenia
aplikacji korzystaj±cych z biblioteki libPropList. 

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
