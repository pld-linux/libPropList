Summary:	libPropList library
Summary(pl):	Biblioteka libPropList
Name:		libPropList
Version:	0.8.3
Release:	4
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRoot:	/tmp/%{name}-%{version}-root

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
./configure \
	--prefix=/usr/X11R6 
make 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*.h

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.8.3-4]
- compiled on rpm 3

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.8.3-3]
- gzipping documentation (instead bzipping)
- fixed pl translation

* Wed Feb 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.3-2]
- added "Conflicts: glibc <= 2.0.7" for preven installing with proper
  version glibc,
- removed /usr/X11R6/lib/lib*.la from static.

* Fri Jan 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.3-1]
- added striping shared bibraries,
- removed "Prereq: /sbin/ldconfig" (this is generated automatically),
- changed base Source url and added using %%{version} macro in Source,
- fixed Requires for static subpackage 
  (must be %%{name}-devel = %%{version}).

* Fri Jan 29 1999 Artur Frysiak <wiget@usa.net>
- separated from WindowMaker.spec
