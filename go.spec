Summary:	GO - GNOME word processor
Summary(pl):	GO - Procesor tekstu dla GNOME
Name:		go
Version:	0.1.35
Release:	3
Copyright:	GPL
Group:		X11/GNOME/Editors
Group(pl):	X11/GNOME/Edytory
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/go/%{name}-%{version}.tar.gz
Patch0:		go-def.patch
Patch1:		go-desktop.patch
Patch2:		go-plugins.patch
URL: 		http://www-personal.umich.edu/~clahey/software/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel
BuildRequires:	libxml-devel
BuildRequires:	imlib-devel
BuildRequires:	libhnj-devel >= 0.1.1
BuildRequires:	zlib-devel
Requires:	go-plugins
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_libexecdir	%{_libdir}
%define		_applnkdir	%{_datadir}/applnk

%description
A word processor for GNOME.

%description -l pl
Procesor tekstu dla ¶rodowiska GNOME.

%package plugins
Summary:	Go Plugins
Summary(pl):	Wtyczki Go
Group:		X11/GNOME/Editors
Group(pl):	X11/GNOME/Edytory

%description plugins
This package contains a set of plugins written for Go but used also by few
other editors.

%description plugins -l pl
Ten pakiet zawiera zestaw wtyczek napisanych dla Go, ale u¿ywanych równie¿
przez kilka innych edytorów.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
automake
LDFLAGS="-s" ; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README HISTORY THANKS TODO

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,HISTORY,THANKS,TODO}.gz
%attr(755,root,root) %{_bindir}/go
%{_datadir}/hypn
%{_applnkdir}/Editors/go.desktop

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/go
%dir %{_libdir}/go/plugins
%attr(755,root,root) %{_libdir}/go/plugins/*
