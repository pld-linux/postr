Summary:	A Flickr photo uploader
Name:		postr
Version:	0.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	131f746d00dad31c2634ab14184dc4fb
URL:		http://burtonini.com/blog/computers/postr
%pyrequires_eq	python-libs
Requires:	python-gnome-extras-egg
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
postr is a Flickr uploader.

%package -n nautilus-extension-postr
Summary:	Postr extension for Nautilus
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.16.1
Requires:	nautilus-python

%description -n nautilus-extension-postr
Allows to send files from Nautilus.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%update_desktop_database_post

%postun
%update_icon_cache hicolor

%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/postr
%{py_sitescriptdir}/postr
%{_desktopdir}/postr.desktop
%{_iconsdir}/hicolor/*/apps/*

%files -n nautilus-extension-postr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/python/*
