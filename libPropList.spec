Summary:	library for reading/writing GNUstep-style defaults databases
Summary(es):	Biblioteca necesaria para el WindowMaker
Summary(pl):	Biblioteka libPropList
Summary(pt_BR):	Biblioteca necessАria para o WindowMaker
Summary(ru):	Библиотека для чтения/записи баз умолчаний в стиле GNUstep
Summary(uk):	Б╕бл╕отека для читання/запису баз умовчань в стил╕ GNUstep
Name:		libPropList
Version:	0.10.1
Release:	11
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

%description
The libPropList library, hereafter referred to as PL, uses an opaque
data type to represent a tree structure made of strings, data blocks,
arrays and dictionaries (key-value pair lists). This structure can be
manipulated, written out to and read in from a file, and synchronized
with the contents of a file. The purpose of PL is to closely mimick
the behaviour of the property lists used in GNUstep/OPENSTEP (there
formed with the NSString, NSData, NSArray and NSDictionary classes)
and to be compatible with it. PL enables programs that use
configuration or preference files to make these compatible with
GNUstep/OPENSTEP's user defaults handling mechanism, without needing
to use Objective-C or GNUstep/OPENSTEP themselves.

%description -l es
Biblioteca para acceder a base de datos GNUstep-style. Necesaria para
el WindowMaker.

%description -l pl
libPropList jest bibliotek╠ wymagan╠ przez Window Maker'a.

%description -l pt_BR
Biblioteca para acessar base de dados GNUstep-style. NecessАria para o
WindowMaker

%description -l ru
Библиотека libPropList, далее PL, использует непрозрачные типы данных
для представления древовидной структуры строк символов, блоков данных,
массивов и словарей (списков пар ключ-значение). Этой структурой можно
манипулировать, записывать в файл и считывать из файла,
синхронизировать с содержанием файла. Цель PL - повторить поведение
списков свойств из GNUstep/OPENSTEP и быть совместимой с ними. PL
позволяет программам, использующим файлы конфигурации или персональных
настроек, делать это совместимо с механизмом обработки умолчаний
пользователей GNUstep/OPENSTEP без необходимости использовать
Objective-C или GNUstep/OPENSTEP.

%description -l uk
Б╕бл╕отека libPropList, надал╕ PL, використову╓ непрозор╕ типи даних
для представлення деревовидно╖ структури ланцюжк╕в символ╕в, блок╕в
даних, масив╕в та словник╕в (списк╕в пар ключ-значення). Ц╕╓ю
структурою можна ман╕пулювати, записувати в файл та зчитувати з файлу
та синхрон╕зувати з вм╕стом файлу. Мета PL - повторити повед╕нку
списк╕в властивостей з GNUstep/OPENSTEP та бути сум╕сною з ними. PL
дозволя╓ програмам, що використовують файли конф╕гурац╕╖ чи
персональних налаштувань, робити це сум╕сно з механ╕змом обробки
умовчань користувач╕в GNUstep/OPENSTEP без необх╕дност╕
використовувати Objective-C чи GNUstep/OPENSTEP.

%package devel
Summary:	libPropList libraries
Summary(es):	Archivos de inclusiСn y bibliotecas para libPropList
Summary(pl):	Biblioteki libPropList
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para o libPropList
Summary(ru):	Библиотека для баз умолчаний в стиле GNUstep
Summary(uk):	Б╕бл╕отека для баз умовчань в стил╕ GNUstep
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the headers that programmers will need to
develop applications which will use libPropList.

%description devel -l es
Este paquete contiene los archivos de inclusiСn y bibliotecas que se
necesitan para desarrollar programas que usan libPropList.

%description devel -l pl
Ten pakiet zawiera pliki nagЁСwkowe i biblioteki niezbЙdne do
tworzenia aplikacji korzystaj╠cych z biblioteki libPropList.

%description devel -l pt_BR
Este pacote contИm os arquivos de inclusЦo e bibliotecas que sЦo
necessАrios para desenvolver programas que usam o libPropList.

%description devel -l ru
Этот пакет содержит .h файлы для разработки программ, использующих
libPropList.

%description devel -l uk
Цей пакет м╕стить .h файли для розробки програм, як╕ використовують
libPropList.

%package static
Summary:	libPropList static libraries
Summary(es):	Archivos de inclusiСn y bibliotecas para libPropList en versiСn estАtica
Summary(pl):	Biblioteki statyczne libPropList
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para o libPropList em versЦo estАtica
Summary(ru):	Статические библиотеки для libPropLis
Summary(uk):	Статичн╕ б╕бл╕отеки для libPropLis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building libPropList
applications.

%description static -l es
Archivos de inclusiСn y bibliotecas para libPropList en versiСn
estАtica

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbЙdne do tworzenia
aplikacji korzystaj╠cych z biblioteki libPropList.

%description static -l pt_BR
Arquivos de inclusЦo e bibliotecas para o libPropList em versЦo
estАtica

%description static -l ru
Этот пакет содержит статические библиотеки для сборки программ,
использующих libPropList.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки для програм, як╕ використовують
libPropList.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
