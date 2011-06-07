Name:			vo-amrwbenc
Version:		0.1.1
Release:		1%{?dist}
Summary:		VisualOn AMR-WB encoder library
Group:			System Environment/Libraries
License:		ASL 2.0
URL:			http://opencore-amr.sourceforge.net/
Source0:		http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)	

%description
This library contains an encoder implementation of the Adaptive 
Multi Rate Wideband (AMR-WB) audio codec. The library is based 
on a codec implementation by VisualOn as part of the Stagefright 
framework from the Google Android project.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT 
rm $RPM_BUILD_ROOT%{_libdir}/libvo-amrwbenc.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README NOTICE
%{_libdir}/libvo-amrwbenc.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/libvo-amrwbenc.a
%{_libdir}/libvo-amrwbenc.so
%{_libdir}/pkgconfig/vo-amrwbenc.pc

%changelog
* Wed May 04 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 0.1.1-1
- upgraded to new version 0.1.1

* Wed May 04 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 0.1.0-1
- Initial build
