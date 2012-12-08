%define name iso-codes
%define version 3.26
%define release %mkrel 4
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif

Summary: Mapping between ISO country codes and full names
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes_%{version}.orig.tar.bz2
#Source1: ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes-%{version}.tar.bz2.sig
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
rm -rf $RPM_BUILD_ROOT *.lang
%makeinstall_std pkgconfigdir=%pkgconfigdir
%find_lang iso_639
%find_lang iso_3166
%find_lang iso_3166_2
%find_lang iso_4217
%find_lang iso_639_3
%find_lang iso_15924
cat iso_*.lang > iso-codes.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f iso-codes.lang
%defattr(-,root,root)
%doc README ChangeLog TODO
%_datadir/xml/iso-codes/
%pkgconfigdir/iso-codes.pc




%changelog
* Wed Jun 22 2011 Götz Waschk <waschk@mandriva.org> 3.26-1mdv2011.0
+ Revision: 686608
- new version
- extract source package from debian, official ftp is down

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.24.2-2
+ Revision: 665528
- mass rebuild

* Tue Mar 08 2011 Götz Waschk <waschk@mandriva.org> 3.24.2-1
+ Revision: 642830
- update to new version 3.24.2

* Sun Feb 13 2011 Götz Waschk <waschk@mandriva.org> 3.24.1-1
+ Revision: 637584
- update to new version 3.24.1

* Tue Jan 04 2011 Götz Waschk <waschk@mandriva.org> 3.24-1mdv2011.0
+ Revision: 628540
- update to new version 3.24

* Wed Dec 08 2010 Götz Waschk <waschk@mandriva.org> 3.23-1mdv2011.0
+ Revision: 616053
- update to new version 3.23

* Thu Nov 11 2010 Götz Waschk <waschk@mandriva.org> 3.22-1mdv2011.0
+ Revision: 595976
- update to new version 3.22

* Fri Oct 08 2010 Götz Waschk <waschk@mandriva.org> 3.21-1mdv2011.0
+ Revision: 584137
- update to new version 3.21

* Wed Sep 08 2010 Götz Waschk <waschk@mandriva.org> 3.20-1mdv2011.0
+ Revision: 576758
- update to new version 3.20

* Sat Aug 07 2010 Götz Waschk <waschk@mandriva.org> 3.19-1mdv2011.0
+ Revision: 567292
- update to new version 3.19

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 3.14-1mdv2010.1
+ Revision: 513237
- update to new version 3.14

* Tue Feb 02 2010 Frederik Himpe <fhimpe@mandriva.org> 3.13-1mdv2010.1
+ Revision: 499748
- update to new version 3.13

* Fri Jan 01 2010 Frederik Himpe <fhimpe@mandriva.org> 3.12.1-1mdv2010.1
+ Revision: 484752
- update to new version 3.12.1

* Sat Dec 05 2009 Götz Waschk <waschk@mandriva.org> 3.12-1mdv2010.1
+ Revision: 473844
- update to new version 3.12

* Mon Nov 23 2009 Götz Waschk <waschk@mandriva.org> 3.11.1-1mdv2010.1
+ Revision: 469292
- update to new version 3.11.1

* Thu Oct 01 2009 Frederik Himpe <fhimpe@mandriva.org> 3.11-1mdv2010.0
+ Revision: 452261
- update to new version 3.11

* Tue Sep 01 2009 Frederik Himpe <fhimpe@mandriva.org> 3.10.3-1mdv2010.0
+ Revision: 423684
- update to new version 3.10.3

* Mon Aug 03 2009 Frederik Himpe <fhimpe@mandriva.org> 3.10.2-1mdv2010.0
+ Revision: 408491
- update to new version 3.10.2

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 3.10.1-1mdv2010.0
+ Revision: 389594
- update to new version 3.10.1

* Mon Jun 01 2009 Frederik Himpe <fhimpe@mandriva.org> 3.10-1mdv2010.0
+ Revision: 381833
- update to new version 3.10

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 3.9-1mdv2010.0
+ Revision: 370013
- Update to new version 3.9

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Fri Feb 06 2009 Götz Waschk <waschk@mandriva.org> 3.6-1mdv2009.1
+ Revision: 338043
- update to new version 3.6

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 3.5.1-1mdv2009.1
+ Revision: 326460
- update to new version 3.5.1

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 3.5-1mdv2009.1
+ Revision: 309890
- update to new version 3.5

* Wed Nov 05 2008 Götz Waschk <waschk@mandriva.org> 3.4-1mdv2009.1
+ Revision: 299989
- update to new version 3.4

* Fri Aug 29 2008 Götz Waschk <waschk@mandriva.org> 3.3-1mdv2009.0
+ Revision: 277261
- new version

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 3.2-1mdv2009.0
+ Revision: 262949
- new version

* Wed Jul 02 2008 Götz Waschk <waschk@mandriva.org> 3.1-1mdv2009.0
+ Revision: 230753
- new version
- new URL
- add tarball signature file
- fix license

* Mon Jun 09 2008 Götz Waschk <waschk@mandriva.org> 3.0-1mdv2009.0
+ Revision: 217021
- new version

* Mon May 05 2008 Götz Waschk <waschk@mandriva.org> 2.1-1mdv2009.0
+ Revision: 201276
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2009.0
+ Revision: 192394
- new version

* Sun Feb 10 2008 Götz Waschk <waschk@mandriva.org> 1.9-1mdv2008.1
+ Revision: 164966
- new version

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 1.8-1mdv2008.1
+ Revision: 146366
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 30 2007 Götz Waschk <waschk@mandriva.org> 1.7-1mdv2008.1
+ Revision: 139617
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 1.6-1mdv2008.1
+ Revision: 115826
- new version

* Sun Oct 07 2007 Götz Waschk <waschk@mandriva.org> 1.5-1mdv2008.1
+ Revision: 95678
- new version
- add iso 15924 translation

* Wed Aug 29 2007 Götz Waschk <waschk@mandriva.org> 1.4-1mdv2008.0
+ Revision: 73346
- new version

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 1.3-1mdv2008.0
+ Revision: 57991
- new version

* Fri Jul 06 2007 Götz Waschk <waschk@mandriva.org> 1.2-1mdv2008.0
+ Revision: 48892
- new version
- drop extra iso_639/nl.po, it was updated upstream


* Wed Mar 28 2007 Götz Waschk <waschk@mandriva.org> 1.0-2mdv2007.1
+ Revision: 149081
- fix Dutch translation (bug #29936)

* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2007.1
+ Revision: 91683
- new version

* Thu Nov 16 2006 Götz Waschk <waschk@mandriva.org> 0.58-1mdv2007.1
+ Revision: 85016
- Import iso-codes

* Thu Nov 16 2006 G�tz Waschk <waschk@mandriva.org> 0.58-1mdv2007.1
- new version

* Tue Aug 29 2006 Götz Waschk <waschk@mandriva.org> 0.53-1mdv2007.0
- New release 0.53

* Wed Jul 12 2006 G�tz Waschk <waschk@mandriva.org> 0.52-1mdv2007.0
- fix build
- New release 0.52

* Thu Apr 27 2006 Götz Waschk <waschk@mandriva.org> 0.51-1mdk
- New release 0.51

* Wed Mar 15 2006 G�tz Waschk <waschk@mandriva.org> 0.50-1mdk
- use Debian's source tarball
- new version

* Wed Nov 02 2005 Götz Waschk <waschk@mandriva.org> 0.49-1mdk
- New release 0.49

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 0.47-1mdk
- New release 0.47

* Fri Apr 29 2005 G�tz Waschk <waschk@mandriva.org> 0.46-3mdk
- fix pkgconfig file location

* Wed Apr 13 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.46-2mdk
- fix buildrequires

* Wed Apr 13 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.46-1mdk
- initial package

