Summary:	Library for reading/writing GNUstep-style defaults databases
Summary(pl):	Biblioteka do odczytu i zapisu bazy danych ustawie� w stylu GNUstepa
Summary(ru):	���������� ��� ������/������ ��� ��������� � ����� GNUstep
Summary(uk):	��̦����� ��� �������/������ ��� �������� � ���̦ GNUstep
Name:		libPropList
Version:	0.10.1
Release:	13
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

%description -l es
Biblioteca para acceder a base de datos GNUstep-style.

%description -l pl
Biblioteka libPropList, okre�lana tu jako PL, u�ywa ukrytego typu
danych do reprezentacji struktury drzewiastej stworzonej z �a�cuch�w,
blok�w danych, tablic i s�ownik�w (list par klucz-warto��). Struktura
ta mo�e by� modyfikowana, zapisywana i wczytywana z pliku oraz
synchronizowana z zawarto�ci� pliku. Celem PL jest bliskie na�ladowanie 
zachowania list w�asno�ci u�ywanych w GNUstepie i OPENSTEPie 
(uformowanych w klasy NSString, NSData, NSArray i NSDictionary) 
i kompatybilno�� z nimi. PL umo�liwia programom u�ywaj�cym plik�w 
z konfiguracj� lub ustawieniami by� kompatybinymi z mechanizmem obs�ugi 
ustawie� GNUstepa/OPENSTEPa, bez potrzeby u�ywania j�zyka Objective-C 
ani samego GNUstepa/OPENSTEPa.

%description -l pt_BR
Biblioteca para acessar base de dados GNUstep-style.

%description -l ru
���������� libPropList, ����� PL, ���������� ������������ ���� ������
��� ������������� ����������� ��������� ����� ��������, ������ ������,
�������� � �������� (������� ��� ����-��������). ���� ���������� �����
��������������, ���������� � ���� � ��������� �� �����,
���������������� � ����������� �����. ���� PL - ��������� ���������
������� ������� �� GNUstep/OPENSTEP � ���� ����������� � ����. PL
��������� ����������, ������������ ����� ������������ ��� ������������
��������, ������ ��� ���������� � ���������� ��������� ���������
������������� GNUstep/OPENSTEP ��� ������������� ������������
Objective-C ��� GNUstep/OPENSTEP.

%description -l uk
��̦����� libPropList, ����̦ PL, ����������դ �������Ҧ ���� �����
��� ������������� ����������ϧ ��������� ������˦� �����̦�, ���˦�
�����, ����צ� �� ������˦� (����˦� ��� ����-��������). 㦤�
���������� ����� ��Φ��������, ���������� � ���� �� ��������� � �����
�� ������Φ������ � �ͦ���� �����. ���� PL - ��������� ����Ħ���
����˦� ������������ � GNUstep/OPENSTEP �� ���� ��ͦ���� � ����. PL
������Ѥ ���������, �� �������������� ����� ���Ʀ����æ� ��
������������ �����������, ������ �� ��ͦ��� � ����Φ���� �������
�������� ���������ަ� GNUstep/OPENSTEP ��� ����Ȧ����Ԧ
��������������� Objective-C �� GNUstep/OPENSTEP.

%package devel
Summary:	Header files for libPropList library
Summary(es):	Archivos de inclusi�n para libPropList
Summary(pl):	Pliki nag��wkowe biblioteki libPropList
Summary(pt_BR):	Arquivos de inclus�o para o libPropList
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the headers that programmers will need to
develop applications which will use libPropList.

%description devel -l es
Este paquete contiene los archivos de inclusi�n que se necesitan
para desarrollar programas que usan libPropList.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe niezb�dne do tworzenia aplikacji
korzystaj�cych z biblioteki libPropList.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o que s�o necess�rios para
desenvolver programas que usam o libPropList.

%description devel -l ru
���� ����� �������� .h ����� ��� ���������� ��������, ������������
libPropList.

%description devel -l uk
��� ����� ͦ����� .h ����� ��� �������� �������, �˦ ��������������
libPropList.

%package static
Summary:	Static libPropList library
Summary(es):	Biblioteca est�tica para libPropList
Summary(pl):	Biblioteka statyczna libPropList
Summary(pt_BR):	Biblioteca est�tica para o libPropList
Summary(ru):	����������� ���������� ��� libPropLis
Summary(uk):	������Φ ¦�̦����� ��� libPropLis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of libPropList library.

%description static -l es
Biblioteca est�tica para libPropList.

%description static -l pl
Ten pakiet zawiera statyczn� wersj� biblioteki libPropList.

%description static -l pt_BR
Biblioteca est�tica para o libPropList.

%description static -l ru
���� ����� �������� ����������� ���������� libPropList.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦����� libPropList.

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
