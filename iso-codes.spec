%define pkgconfigdir %{_datadir}/pkgconfig

Summary:	Mapping between ISO country codes and full names
Name:		iso-codes
Version:	3.54
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://pkg-isocodes.alioth.debian.org/
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
Source1:	iso-codes.rpmlintrc
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
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%make

%install
%makeinstall_std pkgconfigdir=%{pkgconfigdir}
%find_lang iso_639 iso_3166 iso_3166_2 iso_4217 iso_639_3 iso_639_5 iso_15924 iso-codes.lang

%files -f iso-codes.lang
%doc README ChangeLog TODO
%{_datadir}/xml/iso-codes/
%{pkgconfigdir}/iso-codes.pc

