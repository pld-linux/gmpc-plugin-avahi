%define		source_name gmpc-avahi
Summary:	Avahi plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka avahi dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-avahi
Version:	0.17.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	62661f32faa32be4a80fd212e36a4c0c
URL:		http://gmpcwiki.sarine.nl/index.php?title=Avahi
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	gmpc-devel >= 0.17.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.17.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avahi plugin auto-detects the presence of MPD servers in the network.
For every found server it adds a profile and updates it when the IP
address of the server changes.

%description -l pl.UTF-8
Wtyczka Avahi automatycznie wykrywa obecność serwerów MPD w sieci. Dla
każdego znalezionego serwera dodaje profil i uaktualnia go, gdy adres
IP serwera ulegnie zmianie.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/avahiplugin.so
