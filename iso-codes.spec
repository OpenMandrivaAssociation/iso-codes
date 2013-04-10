%define pkgconfigdir %{_datadir}/pkgconfig

Summary:	Mapping between ISO country codes and full names
Name:		iso-codes
Version:	3.41
Release:	1
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
License:	LGPLv2+
Group:		System/Libraries
Url:		http://pkg-isocodes.alioth.debian.org/
BuildRequires:	python-pyxml
BuildRequires:	python
BuildArch:	noarch

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
%find_lang iso_15924
cat iso_*.lang > iso-codes.lang

%files -f iso-codes.lang
%doc README ChangeLog TODO
%{_datadir}/xml/iso-codes/
%pkgconfigdir/iso-codes.pc
