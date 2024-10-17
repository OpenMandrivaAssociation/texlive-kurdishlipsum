Name:		texlive-kurdishlipsum
Version:	47518
Release:	2
Summary:	A 'lipsum' package for the Kurdish language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kurdishlipsum
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kurdishlipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kurdishlipsum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides lipsum-like facilities for the Kurdish
language. The package gives you easy access to the Kurdish
poetry and balladry texts of the Diwany Vafaiy, Ahmedy Xani,
Naly, Mahwy,.... The package needs to be run under XeLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/kurdishlipsum
%doc %{_texmfdistdir}/doc/xelatex/kurdishlipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
