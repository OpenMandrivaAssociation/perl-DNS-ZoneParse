%define	upstream_name    DNS-ZoneParse
%define upstream_version 1.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse and manipulate DNS Zone Files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/DNS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/DNS
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 681367
- mass rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 553082
- update to 1.00

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.990.0-1mdv2010.1
+ Revision: 461266
- update to 0.99

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.0
+ Revision: 403155
- rebuild using %%perl_convert_version

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-1mdv2009.1
+ Revision: 303772
- update to new version 0.96

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.95-5mdv2009.0
+ Revision: 256751
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.95-3mdv2008.1
+ Revision: 137175
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.95-2mdv2008.1
+ Revision: 136993
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 13 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-12 13:12:28 (63851)
Import perl-DNS-ZoneParse

* Fri Oct 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.95-1mdv2007.1
- initial Mandriva package

