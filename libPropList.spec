Summary:	library for reading/writing GNUstep-style defaults databases
Summary(es):	Biblioteca necesaria para el WindowMaker
Summary(pl):	Biblioteka libPropList
Summary(pt_BR):	Biblioteca necess�ria para o WindowMaker
Summary(ru):	���������� ��� ������/������ ��� ��������� � ����� GNUstep
Summary(uk):	��̦����� ��� �������/������ ��� �������� � ���̦ GNUstep
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
libPropList jest bibliotek� wymagan� przez Window Maker'a.

%description -l pt_BR
Biblioteca para acessar base de dados GNUstep-style. Necess�ria para o
WindowMaker

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
Summary:	libPropList libraries
Summary(es):	Archivos de inclusi�n y bibliotecas para libPropList
Summary(pl):	Biblioteki libPropList
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o libPropList
Summary(ru):	���������� ��� ��� ��������� � ����� GNUstep
Summary(uk):	��̦����� ��� ��� �������� � ���̦ GNUstep
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the headers that programmers will need to
develop applications which will use libPropList.

%description devel -l es
Este paquete contiene los archivos de inclusi�n y bibliotecas que se
necesitan para desarrollar programas que usan libPropList.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe i biblioteki niezb�dne do
tworzenia aplikacji korzystaj�cych z biblioteki libPropList.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o e bibliotecas que s�o
necess�rios para desenvolver programas que usam o libPropList.

%description devel -l ru
���� ����� �������� .h ����� ��� ���������� ��������, ������������
libPropList.

%description devel -l uk
��� ����� ͦ����� .h ����� ��� �������� �������, �˦ ��������������
libPropList.

%package static
Summary:	libPropList static libraries
Summary(es):	Archivos de inclusi�n y bibliotecas para libPropList en versi�n est�tica
Summary(pl):	Biblioteki statyczne libPropList
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o libPropList em vers�o est�tica
Summary(ru):	����������� ���������� ��� libPropLis
Summary(uk):	������Φ ¦�̦����� ��� libPropLis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building libPropList
applications.

%description static -l es
Archivos de inclusi�n y bibliotecas para libPropList en versi�n
est�tica

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezb�dne do tworzenia
aplikacji korzystaj�cych z biblioteki libPropList.

%description static -l pt_BR
Arquivos de inclus�o e bibliotecas para o libPropList em vers�o
est�tica

%description static -l ru
���� ����� �������� ����������� ���������� ��� ������ ��������,
������������ libPropList.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦����� ��� �������, �˦ ��������������
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
