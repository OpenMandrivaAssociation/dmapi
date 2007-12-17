%define	name	dmapi
%define	version	2.2.5
%define	release	%mkrel 2

%define lib_name_orig	libdm
%define lib_major	0
%define lib_name	%mklibname dm %{lib_major}

Summary:	Data Management API runtime environment
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://oss.sgi.com/projects/xfs/download/cmd_tars/%{name}_%{version}-1.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
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

%package -n	%{lib_name}-devel
Summary:	Data Management API static libraries and headers
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	dm-devel = %{version}-%{release}
Obsoletes:	dm-devel

%description -n	%{lib_name}-devel
dmapi-devel contains the libraries and header files needed to
develop programs which make use of the Data Management API
(DMAPI).  If you install dmapi-devel, you'll also want to install
the dmapi (runtime) package and the xfsprogs-devel package.

%prep
%setup -q

%build
aclocal && autoconf
%configure2_5x --libdir=/%{_lib}
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DIST_ROOT=%{buildroot}/
make install-dev DIST_ROOT=%{buildroot}/

# (sb) installed but unpackaged files
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/dmapi

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc doc/COPYING README
/%{_lib}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc doc/PORTING doc/CHANGES.gz doc/COPYING README
/%{_lib}/*.so
/%{_lib}/*a
%{_libdir}/*.so
%{_libdir}/*a
%{_mandir}/man3/*
%{_includedir}/*/*


