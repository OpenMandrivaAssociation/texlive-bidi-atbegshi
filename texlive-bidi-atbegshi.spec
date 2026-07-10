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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds some commands to the atbegshi package for proper
placement of background material in the left and right corners of the
output page, in both LTR and RTL modes. The package only works with
xelatex format and should be loaded before the bidi package.

