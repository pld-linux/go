Summary:	GO - GNOME word processor
Summary(pl):	GO - Procesor tekstu dla GNOME
Name:		go
Version:	0.1.35
Release:	2
Copyright:	GPL
Group:		X11/GNOME/Editors
Group(pl):	X11/GNOME/Edytory
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/go/%{name}-%{version}.tar.gz
Patch0:		go-def.patch
Patch1:		go-desktop.patch
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
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_libexecdir	%{_libdir}

%description
A word processor for GNOME.

%description -l pl
Procesor tekstu dla ¶rodowiska GNOME.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
LDFLAGS="-s" ; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README HISTORY THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,HISTORY,THANKS,TODO}.gz
%attr(755,root,root) %{_bindir}/go

%dir %{_libdir}/go
%dir %{_libdir}/go/plugins
%attr(755,root,root) %{_libdir}/go/plugins/*

%{_libdir}/*.a
%{_datadir}/hypn/*
%{_datadir}/applnk/Editors/go.desktop
