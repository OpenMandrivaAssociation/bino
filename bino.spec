Summary:	Video Player with 3D and Multi-Display Video Support
Name:		bino
Version:	1.4.4
Release:	1
License:	GPLv3+
Group:		Video
Url:		http://bino3d.org
Source0:	http://mirror.lihnidos.org/GNU/savannah/bino/%{name}-%{version}.tar.xz

BuildRequires:	ffmpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(openal)
BuildRequires:	texinfo

%description
Bino is a video player with the following main features:
- Support for stereoscopic 3D video, with a wide variety of input and output
formats.
- Support for multi-display video, e.g. for powerwalls, Virtual Reality
installations and other multi-projector setups.

%prep
%setup -q

%build
export PATH=$PATH:%{qt4bin}
export LDFLAGS="%{ldflags} -zmuldefs"
%configure \
	--disable-silent-rules

%make

%install
%makeinstall_std

rm -rf "%{buildroot}%{_datadir}/doc"

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/bino
%doc %{_mandir}/man1/bino.1.*
%doc %{_infodir}/bino.info.*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/bino.*


