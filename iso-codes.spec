%define name iso-codes
%define version 1.2
%define release %mkrel 1
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif

Summary: Mapping between ISO country codes and full names
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.debian.org/debian/pool/main/i/iso-codes/%{name}_%{version}.orig.tar.bz2
License: GPL
Group: System/Libraries
#gw FIXME outdated URL
Url: http://people.debian.org/~mckinstry/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-pyxml
BuildRequires: python
BuildArch: noarch

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs
throughout Mandriva Linux.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
rm -rf $RPM_BUILD_ROOT *.lang
%makeinstall_std pkgconfigdir=%pkgconfigdir
%find_lang iso_639
%find_lang iso_3166
%find_lang iso_3166_2
%find_lang iso_4217
%find_lang iso_639_3
cat iso_*.lang > iso-codes.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f iso-codes.lang
%defattr(-,root,root)
%doc README ChangeLog TODO
%_datadir/xml/iso-codes/
%_datadir/iso-codes/
%pkgconfigdir/iso-codes.pc


