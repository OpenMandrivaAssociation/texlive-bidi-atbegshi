%global tl_name bidi-atbegshi
%global tl_revision 62009

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Bidi-aware shipout macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bidi-atbegshi
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi-atbegshi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi-atbegshi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds some commands to the atbegshi package for proper
placement of background material in the left and right corners of the
output page, in both LTR and RTL modes. The package only works with
xelatex format and should be loaded before the bidi package.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi
%dir %{_datadir}/texmf-dist/tex/xelatex/bidi-atbegshi
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/README
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/bidi-atbegshi-doc.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/bidi-atbegshi-doc.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-LTR.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-LTR.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-RTL.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-RTL.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-foreground-LTR.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-foreground-LTR.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-foreground-RTL.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidi-atbegshi/test-foreground-RTL.tex
%{_datadir}/texmf-dist/tex/xelatex/bidi-atbegshi/bidi-atbegshi.sty
