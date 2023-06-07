Summary:	A Flickr photo uploader
Summary(pl.UTF-8):	Narzędzie do umieszczania zdjęć na Flickr
Name:		postr
Version:	0.12.5
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/postr/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	e0e50fc64ba749cd4999015dc30c1ad9
Patch0:		nautilus-ext-dir.patch
Patch1:		%{name}-nautilus4.patch
URL:		http://projects.gnome.org/postr/
BuildRequires:	nautilus-python-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
%pyrequires_eq	python-libs
Requires:	python-gnome-gconf
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk >= 2:2.0
Requires:	python-twisted
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
Requires:	nautilus >= 43
Requires:	nautilus-python >= 4.0

%description -n nautilus-extension-postr
Allows to send files to Flickr from Nautilus.

%description -n nautilus-extension-postr -l pl.UTF-8
To rozszerzenie pozwala wysyłać pliki na serwis Flickr z Nautilusa.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix} \
	--install-purelib=%{py_sitescriptdir} \
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
%doc README
%attr(755,root,root) %{_bindir}/postr
%{py_sitescriptdir}/postr
%{py_sitescriptdir}/postr-%{version}-py*.egg-info
%{_desktopdir}/postr.desktop
%{_iconsdir}/hicolor/*x*/apps/postr.png
%{_iconsdir}/hicolor/scalable/apps/postr.svg

%files -n nautilus-extension-postr
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/nautilus-python/extensions/postrExtension.py
