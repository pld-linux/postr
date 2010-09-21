Summary:	A Flickr photo uploader
Summary(pl.UTF-8):	Narzędzie do umieszczania zdjęć na Flickr
Name:		postr
Version:	0.12.4
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/postr/0.12/%{name}-%{version}.tar.bz2
# Source0-md5:	83031103239108bfedb1b99ae1091c19
URL:		http://projects.gnome.org/postr/
BuildRequires:	rpm-pythonprov
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires:	hicolor-icon-theme
%pyrequires_eq	python-libs
Requires:	python-gnome-extras-egg
Requires:	python-gnome-gconf
Requires:	python-pygtk-gtk >= 2:2.0
Requires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
postr is a Flickr uploader.

%description -l pl.UTF-8
postr to narzędzie do umieszczania zdjęć na serwisie Flickr.

%package -n nautilus-extension-postr
Summary:	Postr extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie postr dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.16.1
Requires:	nautilus-python

%description -n nautilus-extension-postr
Allows to send files to Flickr from Nautilus.

%description -n nautilus-extension-postr -l pl.UTF-8
To rozszerzenie pozwala wysyłać pliki na serwis Flickr z Nautilusa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

if [ "%{_libdir}" != "/usr/lib" ]; then
	mv $RPM_BUILD_ROOT{/usr/lib,%{_libdir}}
fi

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
%{py_sitescriptdir}/Postr-%{version}-py*.egg-info
%{py_sitescriptdir}/postr
%{_desktopdir}/postr.desktop
%{_iconsdir}/hicolor/*/apps/*

%files -n nautilus-extension-postr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/python/*
