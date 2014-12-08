%define oname	libdm
%define major	0
%define libname	%mklibname dm %{major}
%define devname	%mklibname -d dm 

Summary:	Data Management API runtime environment
Name:		dmapi
Version:	2.2.12
Release:	4
License:	LGPLv2 and GPLv2
Group:		System/Kernel and hardware
URL:		http://oss.sgi.com/projects/xfs/
Source0:	ftp://oss.sgi.com/projects/xfs/cmd_tars/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	xfsprogs-devel
BuildRequires:	libtool

%description
Files required by system software using the Data Management API
(DMAPI).  This is used to implement the interface defined in the
X/Open document:  Systems Management: Data Storage Managment
(XDSM) API dated February 1997.  This interface is implemented
by the libdm library.

%package -n	%{libname}
Summary:	Main library for %{oname}
Group:		System/Libraries
Provides:	%{oname} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{oname}.

%package -n	%{devname}
Summary:	Data Management API static libraries and headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	dm-devel = %{version}-%{release}

%description -n	%{devname}
dmapi-devel contains the libraries and header files needed to
develop programs which make use of the Data Management API
(DMAPI).  If you install dmapi-devel, you'll also want to install
the dmapi (runtime) package and the xfsprogs-devel package.

%prep
%setup -q

%build
make configure
%configure \
	--disable-static \
	--libdir=/%{_lib} 

%make

%install
%makeinstall_std
make install-dev DIST_ROOT=%{buildroot}/

# (sb) installed but unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dmapi

rm -f %{buildroot}/%{_lib}/*.*a

chmod 0755 %{buildroot}/%{_lib}/libdm.so.*

%files -n %{libname}
/%{_lib}/libdm.so.%{major}*

%files -n %{devname}
%doc doc/PORTING doc/CHANGES.gz doc/COPYING README
/%{_lib}/*.so
%{_libexecdir}/*.so
%{_mandir}/man3/*
%{_includedir}/*/*


