%define	upstream_name    DNS-ZoneParse
%define upstream_version 0.99

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse and manipulate DNS Zone Files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/DNS/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
