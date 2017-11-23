%define pkgconfigdir %{_datadir}/pkgconfig

Summary:	Mapping between ISO country codes and full names
Name:		iso-codes
Version:	3.77
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://pkg-isocodes.alioth.debian.org/
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
Source1:	iso-codes.rpmlintrc
BuildRequires:	python
BuildArch:	noarch

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs
throughout OpenMandriva Linux.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std pkgconfigdir=%{pkgconfigdir}

%find_lang iso_639
%find_lang iso_3166
%find_lang iso_3166_2
%find_lang iso_4217
%find_lang iso_639_3
%find_lang iso_15924
%find_lang iso_639_5
%find_lang iso_3166-1
%find_lang iso_3166-2
%find_lang iso_3166-3
%find_lang iso_639-2
%find_lang iso_639-3
%find_lang iso_639-5

cat iso_*.lang > iso-codes.lang

%files -f iso-codes.lang
%doc ChangeLog
%dir %{_datadir}/xml/iso-codes/
%{_datadir}/xml/iso-codes/*.xml
%{_datadir}/iso-codes/json/*.json
%{pkgconfigdir}/iso-codes.pc
