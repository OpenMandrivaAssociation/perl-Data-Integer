%define upstream_name    Data-Integer

Name:       perl-%{upstream_name}
Version:	0.007
Release:    1

Summary:    Details of the native integer data type
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/robrwo/Data-Integer
Source0:    https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{upstream_name}-%{version}.tar.gz

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

%description
This module is about the native integer numerical data type. A native
integer is one of the types of datum that can appear in the numeric part of
a Perl scalar. This module supplies constants describing the native integer
type.

There are actually two native integer representations: signed and unsigned.
Both are handled by this module.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
