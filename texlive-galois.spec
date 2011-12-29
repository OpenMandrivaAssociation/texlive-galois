# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/galois
# catalog-date 2006-12-02 11:49:32 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-galois
Version:	1.5
Release:	1
Summary:	Typeset Galois connections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/galois
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/galois.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/galois.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/galois.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package deals with connections in two-dimensional style,
optionally in colour.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/galois/galois.sty
%doc %{_texmfdistdir}/doc/latex/galois/README
%doc %{_texmfdistdir}/doc/latex/galois/galois.pdf
#- source
%doc %{_texmfdistdir}/source/latex/galois/Makefile
%doc %{_texmfdistdir}/source/latex/galois/galois.dtx
%doc %{_texmfdistdir}/source/latex/galois/galois.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
