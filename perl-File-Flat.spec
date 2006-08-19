#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Flat
Summary:	File::Flat - implements a flat filesystem
Summary(pl):	File::Flat - implementacja p³askiego systemu plików
Name:		perl-File-Flat
Version:	0.96
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1cfc9d23bf76e0deeae0dbb0765b486c
URL:		http://search.cpan.org/dist/File-Flat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-NCopy
BuildRequires:	perl-File-Remove
BuildRequires:	perl-Test-ClassAPI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Flat implements a flat filesystem. A flat filesystem is a
filesystem in which directories do not exist. It provides an
abstraction over any normal filesystem which makes it appear as if
directories do not exist. In effect, it will automatically create
directories as needed. This is created for things like install scripts
and such, as you never need to worry about the existance of
directories, just write to a file, no matter where it is.

%description -l pl
File::Flat implementuje p³aski system plików. P³aski system plików to
taki, w którym nie istniej± katalogi. Modu³ udostêpnia abstrakcjê
ponad ka¿dym normalnym systemem plików, powoduj±c±, ¿e zachowuje siê,
jakby katalogi nie istnia³y. W efekcie automatycznie tworzy wszystkie
potrzebne katalogi. S³u¿y do rzeczy takich jak skrypty instalacyjne i
inne, ¿eby nie trzeba by³o siê martwiæ o istnienie katalogów -
wystarczy po prostu pisaæ do pliku, nie wa¿ne gdzie on jest.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/Flat.pm
%{_mandir}/man3/*
