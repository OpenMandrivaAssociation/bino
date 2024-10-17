%define _disable_rebuild_configure 1

Name:               bino
Version:            1.6.7
Release:            1
Summary:            Video Player with 3D and Multi-Display Video Support
Source0:            https://bino3d.org/releases/%{name}-%{version}.tar.xz
URL:                https://bino3d.org
Group:              Video
License:            GPLv3+
BuildRequires:      qt5-devel
BuildRequires:      glew-devel >= 1.5.0
BuildRequires:      ffmpeg-devel
BuildRequires:      libass-devel
BuildRequires:      openal-devel
BuildRequires:      lirc-devel
BuildRequires:      texinfo

%description
Bino is a video player with the following main features: 

- Support for stereoscopic 3D video, with a wide variety of input and output
formats.
- Support for multi-display video, e.g. for powerwalls, Virtual Reality
installations and other multi-projector setups.

%prep
%setup -q
%autopatch -p1

%build

export CXXFLAGS="%{optflags} -std=c++11"
%configure \
    --disable-silent-rules

%make

%install
%makeinstall_std

%__rm -rf "%{buildroot}%{_datadir}/doc"

%find_lang %{name}

%if %{mdvver} < 201200
%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info
%endif

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/bino
%doc %{_mandir}/man1/bino.1*
%doc %{_infodir}/bino.info*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/bino.*
