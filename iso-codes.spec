%define name iso-codes
%define version 3.37
%define release %mkrel 0
%define pkgconfigdir %_datadir/pkgconfig

Summary: Mapping between ISO country codes and full names
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pkg-isocodes.alioth.debian.org/downloads/iso-codes-%{version}.tar.bz2
Source1: http://pkg-isocodes.alioth.debian.org/downloads/iso-codes-%{version}.tar.bz2.sig
License: LGPLv2+
Group: System/Libraries
Url: http://pkg-isocodes.alioth.debian.org/
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
rm -rf %{buildroot} *.lang
%makeinstall_std pkgconfigdir=%pkgconfigdir
%find_lang iso_639
%find_lang iso_3166
%find_lang iso_3166_2
%find_lang iso_4217
%find_lang iso_639_3
%find_lang iso_15924
cat iso_*.lang > iso-codes.lang

%clean
rm -rf %{buildroot}

%files -f iso-codes.lang
%defattr(-,root,root)
%doc README ChangeLog TODO
%_datadir/xml/iso-codes/
%pkgconfigdir/iso-codes.pc


