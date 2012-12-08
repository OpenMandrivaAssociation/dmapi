%define lib_name_orig	libdm
%define lib_major	0
%define lib_name	%mklibname dm %{lib_major}
%define devel_name      %mklibname -d dm 

Summary:	Data Management API runtime environment
Name:		dmapi
Version:	2.2.10
Release:	6
License:	LGPLv2 and GPLv2
Group:		System/Kernel and hardware
URL:		http://oss.sgi.com/projects/xfs/
Source0:	ftp://oss.sgi.com/projects/xfs/cmd_tars/%{name}-%{version}.tar.gz
BuildRequires:	xfsprogs-devel
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	libtool

%description
Files required by system software using the Data Management API
(DMAPI).  This is used to implement the interface defined in the
X/Open document:  Systems Management: Data Storage Managment
(XDSM) API dated February 1997.  This interface is implemented
by the libdm library.

%package -n	%{lib_name}
Summary:	Main library for %{lib_name_orig}
Group:		System/Libraries
Provides:	%{lib_name_orig} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{lib_name_orig}.

%package -n	%{devel_name}
Summary:	Data Management API static libraries and headers
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	dm-devel = %{version}-%{release}
Provides:	libdm0-devel = %{version}-%{release}

%description -n	%{devel_name}
dmapi-devel contains the libraries and header files needed to
develop programs which make use of the Data Management API
(DMAPI).  If you install dmapi-devel, you'll also want to install
the dmapi (runtime) package and the xfsprogs-devel package.

%prep
%setup -q

%build
%configure2_5x --libdir=/%{_lib} --disable-static
%make

%install
rm -rf %{buildroot}
make install DIST_ROOT=%{buildroot}/
make install-dev DIST_ROOT=%{buildroot}/

# (sb) installed but unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dmapi

rm -f %{buildroot}/%{_lib}/*.*a

chmod 0755 %{buildroot}/%{_lib}/libdm.so.*

%files -n %{lib_name}
/%{_lib}/*.so.*

%files -n %{devel_name}
%doc doc/PORTING doc/CHANGES.gz doc/COPYING README
/%{_lib}/*.so
%{_libdir}/*.so
%{_mandir}/man3/*
%{_includedir}/*/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-4mdv2011.0
+ Revision: 663784
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-3mdv2011.0
+ Revision: 604797
- rebuild

* Mon Dec 28 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.10-2mdv2010.1
+ Revision: 483184
- rebuild

* Wed May 06 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.10-1mdv2010.0
+ Revision: 372679
- Update to new version 2.2.10
- Don't run aclocal and autoconf, it breaks the build and is not needed

* Thu Feb 05 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.9-2mdv2009.1
+ Revision: 337877
- SPEC file clean-ups:
- Fix license
- use %%{buildroot} instead of $RPM_BUILD_ROOT
- Don't package documentation files in lib package
- Rename devel package to follow official policy

* Thu Feb 05 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.9-1mdv2009.1
+ Revision: 337865
- Update to new version 2.2.9

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.5-4mdv2009.1
+ Revision: 316556
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.2.5-3mdv2009.0
+ Revision: 220651
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.2.5-2mdv2008.1
+ Revision: 124066
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 03 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 2.2.5-2mdv2007.0
+ Revision: 131829
- Rebuilt.
- Import dmapi

* Sun Jul 09 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.5-1mdv2007.0
- 2.2.5.

* Wed Jun 21 2006 Stew Benedict <sbenedict@mandriva.com> 2.2.3-1mdv2007.0
- 2.2.3

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 2.2.1-5mdk
- rebuild for sparc

* Wed Jan 11 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.2.1-4mdk
- add BuildRequires: libtool

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.2.1-3mdk
- Rebuild

* Sun Jun 19 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.2.1-2mdk
- add BuildRequires: libext2fs-devel

* Sat Jun 04 2005 Stew Benedict <sbenedict@mandriva.com> 2.2.1-1mdk
- 2.2.1

