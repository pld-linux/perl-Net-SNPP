%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SNPP
Summary:	Net::SNPP perl module
Summary(pl):	Modu³ perla Net::SNPP
Name:		perl-Net-SNPP
Version:	1.14
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/DREDD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5e36c9c8c83e70c4cf769abd58397a0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SNPP - Perl interface to SNPP.

%description -l pl
Net::SNPP - interfejs perla do SNPP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/SNPP.pm
%{perl_vendorlib}/Net/SNPP
%{_mandir}/man3/*
