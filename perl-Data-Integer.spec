%define upstream_name    Data-Integer
%define upstream_version 0.004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Details of the native integer data type
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(integer)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is about the native integer numerical data type. A native
integer is one of the types of datum that can appear in the numeric part of
a Perl scalar. This module supplies constants describing the native integer
type.

There are actually two native integer representations: signed and unsigned.
Both are handled by this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 653562
- rebuild for updated spec-helper

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 573802
- import perl-Data-Integer

