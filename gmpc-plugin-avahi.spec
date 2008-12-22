# TODO:
# - desc

%define		source_name gmpc-avahi
Summary:	Stopbutton plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka avahi dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-avahi
Version:	0.16.96
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	b28c4936ab9cf37bbd1a21a1a0fd3cfb
URL:		http://www.sarine.nl//gmpc-plugins
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.16.96
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.16.96
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The plugin allows you to generate a playlist based on a set of rules,
f.e. "Genre contains 'jazz' and artist doesn't contain 'Jones'".

%description -l pl.UTF-8
Ta wtyczka pozwala generować playlisty w oparciu o zbiór reguł, na
przykład "Gatunek zawiera 'jazz' i wykonawca nie zawiera 'Jones'".

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

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
