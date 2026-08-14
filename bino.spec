Name:		bino
Version:	2.8
Release:	1
Summary:	Video player with a focus on 3D and Virtual Reality
Source0:	https://bino3d.org/releases/%{name}-%{version}.tar.gz
URL:		https://bino3d.org
Group:		Video
License:	GPLv3+
# 2.x is a Qt6 rewrite using Qt Multimedia; it no longer links FFmpeg directly
BuildSystem:	cmake
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pandoc

%description
Bino is a video player with a focus on 3D and Virtual Reality:

- Support for stereoscopic 3D images and videos in various formats
- Support for 180° and 360° surround images and videos
- Support for 3D displays and Virtual Reality environments

%files
%doc LICENSE.md NEWS.md README.md
%{_bindir}/bino
%{_mandir}/man1/bino.1*
%{_datadir}/applications/org.bino3d.bino.desktop
%{_datadir}/metainfo/org.bino3d.bino.metainfo.xml
%{_iconsdir}/hicolor/*/apps/org.bino3d.bino.*
%{_docdir}/bino/bino-manual.html
%{_docdir}/bino/bino-manual.css
