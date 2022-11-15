Name:		texlive-bidi-atbegshi
Version:	62009
Release:	1
Summary:	Bidi-aware shipout macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bidi-atbegshi
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi-atbegshi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi-atbegshi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds some commands to the atbegshi package for
proper placement of background material in the left and right
corners of the output page, in both LTR and RTL modes. The
package only works with xelatex format and should be loaded
before the bidi package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidi-atbegshi
%doc %{_texmfdistdir}/doc/xelatex/bidi-atbegshi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
