#
# Conditional build:
%bcond_without	lfs	# disable largefile support (for files larger than 2GB)
#
Summary:	Tool to copy VOB file chapters to file
Summary(pl):	Narz�dzie do kopiowania cz�ci plik�w VOB do pliku
Name:		vobwalker
Version:	0.1
Release:	1
License:	Public Domain
Group:		Applications
Source0:	http://anachronda.homeunix.com:8000/~rivie/vobwalker/vobwalker-0.1.tar
# Source0-md5:	3999274eea9f0968cf705762b5e6fda1
URL:		http://anachronda.homeunix.com:8000/~rivie/vobwalker/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vobwalker walks through a .VOB file containing DVD video, extracting
lists of VOBUs to a set of chapter files. Each file begins with a VOBU
that has no predecessor (i.e., does not point at a preceding VOBU) and
contains the list of VOBUs found by following the successor pointers
along the list. The final VOBU in each file has no successor.

The practical effect of pointing vobwalker at a .VOB file is that you
wind up with a set of smaller .VOB files, each containing a chapter
from the original file. 

%description -l pl
Vobwalker w�druje poprzez plik .VOB zawieraj�cy film DVD, wyci�gaj�c
listy VOBU do zbioru plik�w cz�ci. Ka�dy plik zaczyna si� od VOBU,
kt�ry nie ma poprzednika (tzn. nie ma wskazania na poprzedzaj�cy VOBU)
i zawiera list� VOBU znalezionych poprzez pod��anie za wska�nikami
nast�pnik�w w li�cie. Ko�cowy VOBU w ka�dym pliku nie ma nast�pnika.

Praktycznym efektem wskazania vobwalkera na plik .VOB jest otrzymanie
zbioru mniejszych plik�w .VOB, z kt�rych ka�dy zawiera cz��
oryginalnego pliku.

%prep
%setup -q

%build
./configure.sh \
	%{?with_lfs:--with-lfs}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install vobcopy $RPM_BUILD_ROOT%{_bindir}
install vobcopy.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog TODO Release-Notes *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
