Summary:	GO - GNOME word processor
Summary(pl.UTF-8):	GO - Procesor tekstu dla GNOME
Name:		go
Version:	0.1.35
Release:	9
License:	GPL
Group:		X11/Applications/Editors
# formerly ftp://ftp.gnome.org/pub/GNOME/stable/sources/go/
Source0:	http://tiger.bioinf.cs.uni-potsdam.de/free/Desktops/Gnome/%{name}-%{version}.tar.gz
# Source0-md5:	ab98f516672c691816c3bce58b191493
Patch0:		%{name}-def.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-plugins.patch
Patch3:		%{name}-make.patch
URL:		http://www-personal.umich.edu/~clahey/software/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.14
BuildRequires:	gtk+-devel >= 1.1.15
BuildRequires:	imlib-devel
BuildRequires:	libhnj-devel >= 0.1.1
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
Requires:	go-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
A word processor for GNOME.

%description -l pl.UTF-8
Procesor tekstu dla środowiska GNOME.

%package plugins
Summary:	Go Plugins
Summary(pl.UTF-8):	Wtyczki Go
Group:		X11/Applications/Editors

%description plugins
This package contains a set of plugins written for Go but used also by
few other editors.

%description plugins -l pl.UTF-8
Ten pakiet zawiera zestaw wtyczek napisanych dla Go, ale używanych
również przez kilka innych edytorów.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Wordprocessors

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README HISTORY THANKS TODO
%attr(755,root,root) %{_bindir}/go
%{_datadir}/hypn
%{_applnkdir}/Office/Wordprocessors/go.desktop

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/go
%dir %{_libdir}/go/plugins
%attr(755,root,root) %{_libdir}/go/plugins/*
