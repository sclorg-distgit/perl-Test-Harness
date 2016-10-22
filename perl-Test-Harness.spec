%{?scl:%scl_package perl-Test-Harness}

Name:           %{?scl_prefix}perl-Test-Harness
Version:        3.36
Release:        367%{?dist}
Summary:        Run Perl standard test scripts with statistics
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Harness/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Benchmark)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
# Optional run-time:
BuildRequires:  %{?scl_prefix}perl(Encode)
# Keep Pod::Usage 1.12 really optional
BuildRequires:  %{?scl_prefix}perl(Term::ANSIColor)
BuildRequires:  %{?scl_prefix}perl(Time::HiRes)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
# Dev::Null bundled for bootstrap
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(File::Temp)
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(TAP::Formatter::HTML) >= 0.10
BuildRequires:  %{?scl_prefix}perl(YAML)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
# perl-Test-Harness >= 3.29 delivers perl-TAP-Harness-Env files, bug #1067098
Obsoletes:      %{?scl_prefix}perl-TAP-Harness-Env

# Filter example dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_requires_in ^%{_datadir}/doc
%filter_provides_in ^%{_datadir}/doc
%?perl_default_filter
}
# RPM 4.9 style
%else
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_datadir}/doc
%endif

%description
This package allows tests to be run and results automatically aggregated and
output to STDOUT.

Although, for historical reasons, the Test-Harness distribution takes its name
from this module it now exists only to provide TAP::Harness with an interface
that is somewhat backwards compatible with Test::Harness 2.xx. If you're
writing new code consider using TAP::Harness directly instead.

%prep
%setup -q -n Test-Harness-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes Changes-2.64 examples README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 3.36-367
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.36-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.36-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Petr Pisar <ppisar@redhat.com> - 3.36-1
- 3.36 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-2
- Perl 5.22 rebuild

* Mon Feb 02 2015 Petr Pisar <ppisar@redhat.com> - 3.35-1
- 3.35 bump

* Thu Nov 13 2014 Petr Pisar <ppisar@redhat.com> - 3.34-1
- 3.34 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.33-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.33-2
- Perl 5.20 rebuild

* Mon Aug 18 2014 Petr Pisar <ppisar@redhat.com> - 3.33-1
- 3.33 bump

* Thu Jun 12 2014 Petr Pisar <ppisar@redhat.com> - 3.32-1
- 3.32 bump

* Mon Jun 09 2014 Petr Pisar <ppisar@redhat.com> - 3.31-1
- 3.31 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Petr Pisar <ppisar@redhat.com> - 3.30-2
- Obsolete perl-TAP-Harness-Env (bug #1067098)

* Mon Nov 18 2013 Petr Pisar <ppisar@redhat.com> - 3.30-1
- 3.30 bump

* Mon Oct 14 2013 Petr Pisar <ppisar@redhat.com> - 3.29-1
- 3.29 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 3.28-2
- Perl 5.18 rebuild

* Fri May 03 2013 Petr Pisar <ppisar@redhat.com> - 3.28-1
- 3.28 bump

* Thu May 02 2013 Petr Pisar <ppisar@redhat.com> - 3.27-1
- 3.27 bump

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> 3.26-1
- Specfile autogenerated by cpanspec 1.78.
