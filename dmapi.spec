%define lib_name_orig	libdm
%define lib_major	0
%define lib_name	%mklibname dm %{lib_major}
%define devel_name      %mklibname -d dm 

Summary:	Data Management API runtime environment
Name:		dmapi
Version:	2.2.10
Release:	%mkrel 2
Source0:	ftp://oss.sgi.com/projects/xfs/cmd_tars/%{name}-%{version}.tar.gz
License:	LGPLv2 and GPLv2
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://oss.sgi.com/projects/xfs/
BuildRequires:	xfs-devel
BuildRequires:	libext2fs-devel
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
Obsoletes:	dm-devel
Provides:	libdm0-devel = %{version}-%{release}
Obsoletes:	libdm0-devel < 2.2.9-2

%description -n	%{devel_name}
dmapi-devel contains the libraries and header files needed to
develop programs which make use of the Data Management API
(DMAPI).  If you install dmapi-devel, you'll also want to install
the dmapi (runtime) package and the xfsprogs-devel package.

%prep
%setup -q

%build
%configure2_5x --libdir=/%{_lib}
%make

%install
rm -rf %{buildroot}
make install DIST_ROOT=%{buildroot}/
make install-dev DIST_ROOT=%{buildroot}/

# (sb) installed but unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dmapi

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
/%{_lib}/*.so.*

%files -n %{devel_name}
%defattr(-,root,root)
%doc doc/PORTING doc/CHANGES.gz doc/COPYING README
/%{_lib}/*.so
/%{_lib}/*a
%{_libdir}/*.so
%{_libdir}/*a
%{_mandir}/man3/*
%{_includedir}/*/*


