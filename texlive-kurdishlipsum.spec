%global tl_name kurdishlipsum
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A lipsum package for the Kurdish language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/kurdishlipsum
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kurdishlipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kurdishlipsum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides lipsum-like facilities for the Kurdish language.
The package gives you easy access to the Kurdish poetry and balladry
texts of the Diwany Vafaiy, Ahmedy Xani, Naly, Mahwy,.... The package
needs to be run under XeLaTeX.

