Summary:	libPropList library
Summary(pl):	Biblioteka libPropList
Name:		libPropList
Version:	0.8.3
Release:	2
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Conflicts:	glibc <= 2.0.7

%description
libPropList library, needed by Window Maker.

%description -l pl
libPropList jest biblioteka potrzebną do uruchamiania Window Maker'a.

%package devel
Summary:	libPropList libraries
Summary(pl):	Biblioteki libPropList
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
libPropList headers files

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe i biblioteki niezbędne do tworzenia
aplikacji korzystających z biblioteki libPropList. 

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
Ten pakiet zawiera statyczne biblioteki niezbędne do tworzenia
aplikacji korzystających z biblioteki libPropList. 

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 
make 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

bzip2 -9  AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.bz2 ChangeLog.bz2 NEWS.bz2 README.bz2
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*.h

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Wed Feb 24 1999 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.3-2]
- added "Conflicts: glibc <= 2.0.7" for preven installing with proper
  version glibc,
- removed /usr/X11R6/lib/lib*.la from static.

* Fri Jan 29 1999 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.3-1]
- added striping shared bibraries,
- removed "Prereq: /sbin/ldconfig" (this is generated automatically),
- changed base Source url and added using %%{version} macro in Source,
- fixed Requires for static subpackage 
  (must be %%{name}-devel = %%{version}).

* Fri Jan 29 1999 Artur Frysiak <wiget@usa.net>
- separated from WindowMaker.spec
