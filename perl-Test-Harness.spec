%{?scl:%scl_package perl-Test-Harness}

# Run optional tests
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Test_Harness_enables_optional_test
%else
%bcond_with perl_Test_Harness_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Test-Harness
Epoch:          1
Version:        3.42
Release:        451%{?dist}
Summary:        Run Perl standard test scripts with statistics
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Harness
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
# Remove hard-coded shell bangs
Patch0:         Test-Harness-3.38-Remove-shell-bangs.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
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
%if %{with perl_Test_Harness_enables_optional_test}
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(TAP::Formatter::HTML) >= 0.10
BuildRequires:  %{?scl_prefix}perl(TAP::Harness::Archive)
BuildRequires:  %{?scl_prefix}perl(YAML)
%endif
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

# Filter example dependencies
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_datadir}/doc

%description
This package allows tests to be run and results automatically aggregated and
output to STDOUT.

Although, for historical reasons, the Test-Harness distribution takes its name
from this module it now exists only to provide TAP::Harness with an interface
that is somewhat backwards compatible with Test::Harness 2.xx. If you're
writing new code consider using TAP::Harness directly instead.

%prep
%setup -q -n Test-Harness-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
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
* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.42-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.42-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.42-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.42-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.42-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.42-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.42-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.42-416
- Increase release to favour standalone package

* Tue Mar 20 2018 Petr Pisar <ppisar@redhat.com> - 1:3.42-1
- 3.42 bump

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 1:3.41-1
- 3.41 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.39-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.39-2
- Perl 5.26 rebuild

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 3.39-1
- 3.39 bump

* Tue Mar 14 2017 Petr Pisar <ppisar@redhat.com> - 3.38-1
- 3.38 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-369
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Petr Pisar <ppisar@redhat.com> - 3.36-368
- Remove old obsoleting perl-TAP-Harness-Env

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.36-367
- Avoid loading optional modules from default . (CVE-2016-1238)

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
