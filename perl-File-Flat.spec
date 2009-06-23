#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Flat
Summary:	File::Flat - implements a flat filesystem
Summary(pl.UTF-8):	File::Flat - implementacja płaskiego systemu plików
Name:		perl-File-Flat
Version:	1.04
Release:	1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	20367f74ff34d92b3c839b3da282b4e0
URL:		http://search.cpan.org/dist/File-Flat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
# in Makefile versioned dependencies are set, 
BuildRequires:	perl-prefork
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-File-NCopy
BuildRequires:	perl-File-Remove
BuildRequires:	perl-File-Slurp
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

%description -l pl.UTF-8
File::Flat implementuje płaski system plików. Płaski system plików to
taki, w którym nie istnieją katalogi. Moduł udostępnia abstrakcję
ponad każdym normalnym systemem plików, powodującą, że zachowuje się,
jakby katalogi nie istniały. W efekcie automatycznie tworzy wszystkie
potrzebne katalogi. Służy do rzeczy takich jak skrypty instalacyjne i
inne, żeby nie trzeba było się martwić o istnienie katalogów -
wystarczy po prostu pisać do pliku, nie ważne gdzie on jest.

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
