Summary:	GO - GNOME word processor
Summary(pl):	GO - Procesor tekstu dla GNOME
Name:		go
Version:	0.1.35
Release:	7
License:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/go/%{name}-%{version}.tar.gz
Patch0:		go-def.patch
Patch1:		go-desktop.patch
Patch2:		go-plugins.patch
URL:		http://www-personal.umich.edu/~clahey/software/
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.14
BuildRequires:	libxml-devel
BuildRequires:	imlib-devel
BuildRequires:	libhnj-devel >= 0.1.1
BuildRequires:	zlib-devel
Requires:	go-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_libexecdir	%{_libdir}

%description
A word processor for GNOME.

%description -l pl
Procesor tekstu dla ¶rodowiska GNOME.

%package plugins
Summary:	Go Plugins
Summary(pl):	Wtyczki Go
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory

%description plugins
This package contains a set of plugins written for Go but used also by
few other editors.

%description plugins -l pl
Ten pakiet zawiera zestaw wtyczek napisanych dla Go, ale u¿ywanych
równie¿ przez kilka innych edytorów.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
automake
LDFLAGS="-s" ; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Wordprocessors \
	install

gzip -9nf AUTHORS ChangeLog README HISTORY THANKS TODO

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,HISTORY,THANKS,TODO}.gz
%attr(755,root,root) %{_bindir}/go
%{_datadir}/hypn
%{_applnkdir}/Office/Wordprocessors/go.desktop

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/go
%dir %{_libdir}/go/plugins
%attr(755,root,root) %{_libdir}/go/plugins/*
