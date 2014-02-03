%define		pkgname	excanvas
Summary:	HTML5 Canvas for Internet Explorer
Name:		js-%{pkgname}
Version:	3
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://explorercanvas.googlecode.com/files/excanvas_r%{version}.zip
# Source0-md5:	81a041b98c477f92ed772f2fac0835ad
Source1:	apache.conf
Source2:	lighttpd.conf
URL:		https://code.google.com/p/explorercanvas/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{pkgname}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Modern browsers like Firefox, Safari, Chrome and Opera support the
HTML5 canvas tag to allow 2D command-based drawing. ExplorerCanvas
brings the same functionality to Internet Explorer. To use, web
developers only need to include a single script tag in their existing
web pages.

%package demo
Summary:	Demo for %{pkgname}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{pkgname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{pkgname}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p %{pkgname}.compiled.js $RPM_BUILD_ROOT%{_appdir}/%{pkgname}-%{version}.min.js
ln -s %{pkgname}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{pkgname}.js
cp -p %{pkgname}.js $RPM_BUILD_ROOT%{_appdir}/%{pkgname}-%{version}.src.js
ln -s %{pkgname}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{pkgname}.src.js

install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf
cp -p $RPM_BUILD_ROOT%{_sysconfdir}/{apache,httpd}.conf

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
