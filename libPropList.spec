Summary:	library for reading/writing GNUstep-style defaults databases
Summary(pl):	Biblioteka libPropList
Name:		libPropList
Version:	0.9.1
Release:	1
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
The libPropList library, hereafter referred to as PL, uses an opaque data
type to represent a tree structure made of strings, data blocks, arrays and
dictionaries (key-value pair lists). This structure can be manipulated,
written out to and read in from a file, and synchronized with the contents
of a file. The purpose of PL is to closely mimick the behaviour of the
property lists used in GNUstep/OPENSTEP (there formed with the NSString,
NSData, NSArray and NSDictionary classes) and to be compatible with it. PL
enables programs that use configuration or preference files to make these
compatible with GNUstep/OPENSTEP's user defaults handling mechanism, without
needing to use Objective-C or GNUstep/OPENSTEP themselves.

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
LDFLAGS="-s"; export LDFLAGS
%configure

make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
