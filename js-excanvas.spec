%define		pkgname	excanvas
Summary:	HTML5 Canvas for Internet Explorer
Name:		js-%{pkgname}
Version:	3
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://explorercanvas.googlecode.com/files/excanvas_r%{version}.zip
# Source0-md5:	81a041b98c477f92ed772f2fac0835ad
URL:		https://code.google.com/p/explorercanvas/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{pkgname}

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
