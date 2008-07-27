#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for reading/writing GNUstep-style defaults databases
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu bazy danych ustawień w stylu GNUstepa
Summary(ru.UTF-8):	Библиотека для чтения/записи баз умолчаний в стиле GNUstep
Summary(uk.UTF-8):	Бібліотека для читання/запису баз умовчань в стилі GNUstep
Name:		libPropList
Version:	0.10.1
Release:	14
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
# Source0-md5:	ff32a4edbf9d0861012b2f10fd302ad5
URL:		http://www.windowmaker.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
Biblioteca para acceder a base de datos GNUstep-style.

%description -l pl.UTF-8
Biblioteka libPropList, określana tu jako PL, używa ukrytego typu
danych do reprezentacji struktury drzewiastej stworzonej z łańcuchów,
bloków danych, tablic i słowników (list par klucz-wartość). Struktura
ta może być modyfikowana, zapisywana i wczytywana z pliku oraz
synchronizowana z zawartością pliku. Celem PL jest bliskie naśladowanie 
zachowania list własności używanych w GNUstepie i OPENSTEPie 
(uformowanych w klasy NSString, NSData, NSArray i NSDictionary) 
i kompatybilność z nimi. PL umożliwia programom używającym plików 
z konfiguracją lub ustawieniami być kompatybinymi z mechanizmem obsługi 
ustawień GNUstepa/OPENSTEPa, bez potrzeby używania języka Objective-C 
ani samego GNUstepa/OPENSTEPa.

%description -l pt_BR.UTF-8
Biblioteca para acessar base de dados GNUstep-style.

%description -l ru.UTF-8
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

%description -l uk.UTF-8
Бібліотека libPropList, надалі PL, використовує непрозорі типи даних
для представлення деревовидної структури ланцюжків символів, блоків
даних, масивів та словників (списків пар ключ-значення). Цією
структурою можна маніпулювати, записувати в файл та зчитувати з файлу
та синхронізувати з вмістом файлу. Мета PL - повторити поведінку
списків властивостей з GNUstep/OPENSTEP та бути сумісною з ними. PL
дозволяє програмам, що використовують файли конфігурації чи
персональних налаштувань, робити це сумісно з механізмом обробки
умовчань користувачів GNUstep/OPENSTEP без необхідності
використовувати Objective-C чи GNUstep/OPENSTEP.

%package devel
Summary:	Header files for libPropList library
Summary(es.UTF-8):	Archivos de inclusión para libPropList
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libPropList
Summary(pt_BR.UTF-8):	Arquivos de inclusão para o libPropList
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to
develop applications which will use libPropList.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión que se necesitan
para desarrollar programas que usan libPropList.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia aplikacji
korzystających z biblioteki libPropList.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
desenvolver programas que usam o libPropList.

%description devel -l ru.UTF-8
Этот пакет содержит .h файлы для разработки программ, использующих
libPropList.

%description devel -l uk.UTF-8
Цей пакет містить .h файли для розробки програм, які використовують
libPropList.

%package static
Summary:	Static libPropList library
Summary(es.UTF-8):	Biblioteca estática para libPropList
Summary(pl.UTF-8):	Biblioteka statyczna libPropList
Summary(pt_BR.UTF-8):	Biblioteca estática para o libPropList
Summary(ru.UTF-8):	Статические библиотеки для libPropLis
Summary(uk.UTF-8):	Статичні бібліотеки для libPropLis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libPropList library.

%description static -l es.UTF-8
Biblioteca estática para libPropList.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki libPropList.

%description static -l pt_BR.UTF-8
Biblioteca estática para o libPropList.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки libPropList.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки libPropList.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
