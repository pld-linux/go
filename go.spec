Summary:	GO - GNOME word processor
Summary(pl):	GO - Procesor tekstu dla GNOME
Name:		go
Version:	0.1.35
Release:	9
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/go/%{name}-%{version}.tar.gz
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

%define		_prefix		/usr/X11R6
%define		_libexecdir	%{_libdir}

%description
A word processor for GNOME.

%description -l pl
Procesor tekstu dla �rodowiska GNOME.

%package plugins
Summary:	Go Plugins
Summary(pl):	Wtyczki Go
Group:		X11/Applications/Editors

%description plugins
This package contains a set of plugins written for Go but used also by
few other editors.

%description plugins -l pl
Ten pakiet zawiera zestaw wtyczek napisanych dla Go, ale u�ywanych
r�wnie� przez kilka innych edytor�w.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

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
