# revision 32924
# category Package
# catalog-ctan /macros/latex/contrib/basque-book
# catalog-date 2014-02-03 15:00:17 +0100
# catalog-license lppl1.2
# catalog-version 1.20
Name:		texlive-basque-book
Version:	1.20
Release:	7
Summary:	Class for book-type documents written in Basque
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/basque-book
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is derived from the LaTeX book class. The extensions
solve grammatical and numeration issues that occur when book-
type documents are written in Basque. The class is useful for
writing books, PhD and Master Theses, etc., in Basque.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/basque-book/basque-book.cls
%doc %{_texmfdistdir}/doc/latex/basque-book/README
%doc %{_texmfdistdir}/doc/latex/basque-book/basque-book.pdf
%doc %{_texmfdistdir}/doc/latex/basque-book/basque-book_EUS.pdf
%doc %{_texmfdistdir}/doc/latex/basque-book/basque-book_EUS.tex
#- source
%doc %{_texmfdistdir}/source/latex/basque-book/basque-book.dtx
%doc %{_texmfdistdir}/source/latex/basque-book/basque-book.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
