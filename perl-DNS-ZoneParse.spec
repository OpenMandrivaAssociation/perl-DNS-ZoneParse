%define	module DNS-ZoneParse

Name:		perl-%{module}
Version:	0.95
Release:	%mkrel 5
Summary:	Parse and manipulate DNS Zone Files
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/DNS/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module will parse a Zone File and put all the Resource Records (RRs) into
an anonymous hash structure. At the moment, the following types of RRs are
supported: SOA, NS, MX, A, CNAME, TXT, PTR. It could be useful for maintaining
DNS zones, or for transferring DNS zones to other servers. If you want to
generate an XML-friendly version of your zone files, it is easy to use
XML::Simple with this module once you have parsed the zonefile.

DNS::ZoneParse scans the DNS zonefile - removes comments and seperates the file
into its constituent records. It then parses each record and stores the records
internally. See below for information on the accessor methods.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DNS
%{_mandir}/*/*
