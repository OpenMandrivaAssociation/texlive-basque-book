Name:		texlive-basque-book
Version:	32924
Release:	1
Summary:	Class for book-type documents written in Basque
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/basque-book
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-book.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
