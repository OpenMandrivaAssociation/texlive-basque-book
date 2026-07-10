%global tl_name basque-book
%global tl_revision 32924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	Class for book-type documents written in Basque
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/basque-book
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is derived from the LaTeX book class. The extensions solve
grammatical and numeration issues that occur when book-type documents
are written in Basque. The class is useful for writing books, PhD and
Master Theses, etc., in Basque.

