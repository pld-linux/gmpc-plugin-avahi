%define		source_name gmpc-avahi
Summary:	Avahi plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka avahi dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-avahi
Version:	11.8.16
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	255dfb9694503a2892f1c25314c29907
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_AVAHI
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	avahi
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
