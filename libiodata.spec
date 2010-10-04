%define _name iodata
Name:    libiodata
Version: 0.0.13
Release: 1
Summary: Library for input/ouput data
Group:   System/Libraries
License: LGPLv2
URL:     http://meego.gitorious.org/meego-middleware/iodata
Source0: %{_name}-%{version}.tar.bz2
Patch0:  %{name}-linklibs.patch

BuildRequires: pkgconfig(QtCore) >= 4.5
BuildRequires: bison
BuildRequires: flex
BuildRequires: libqmlog-devel

%description
This package provides a library for writing and reading structured data.

%package devel
Summary:  Development package for %{name}
Group:    Development/Libraries
Requires: pkgconfig(QtCore) >= 4.5
Requires: %{name} = %{version}-%{release}

%description devel
Provides header files for iodata library.

%package tests
Summary:  Testcases for iodata library
Group:    Development/System

%description tests
%{summary}.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
qmake
make

%install
make INSTALL_ROOT=%{buildroot} install
install -d %{buildroot}/%{_datadir}/%{name}-tests/
mv %{buildroot}/%{_datadir}/%{_name}-tests/tests.xml %{buildroot}/%{_datadir}/%{name}-tests/tests.xml

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING debian/changelog
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/iodata/*
%{_libdir}/%{name}.so
%{_datadir}/qt4/mkspecs/features/iodata.prf

%files tests
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{_name}-test
%{_datadir}/%{name}-tests/tests.xml
