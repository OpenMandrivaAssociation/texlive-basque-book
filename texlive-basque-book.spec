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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is derived from the LaTeX book class. The extensions solve
grammatical and numeration issues that occur when book-type documents
are written in Basque. The class is useful for writing books, PhD and
Master Theses, etc., in Basque.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/basque-book
%dir %{_datadir}/texmf-dist/source/latex/basque-book
%dir %{_datadir}/texmf-dist/tex/latex/basque-book
%doc %{_datadir}/texmf-dist/doc/latex/basque-book/README
%doc %{_datadir}/texmf-dist/doc/latex/basque-book/basque-book.pdf
%doc %{_datadir}/texmf-dist/doc/latex/basque-book/basque-book_EUS.pdf
%doc %{_datadir}/texmf-dist/doc/latex/basque-book/basque-book_EUS.tex
%doc %{_datadir}/texmf-dist/source/latex/basque-book/basque-book.dtx
%doc %{_datadir}/texmf-dist/source/latex/basque-book/basque-book.ins
%{_datadir}/texmf-dist/tex/latex/basque-book/basque-book.cls
