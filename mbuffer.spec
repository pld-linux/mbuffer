Summary:	Tool for buffering data streams
Summary(pl):	Narz�dzie do buforowania strumieni danych
Name:		mbuffer
Version:	20060421
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.maier-komor.de/software/mbuffer/%{name}-%{version}.tgz
# Source0-md5:	b1e7b6596052e853352321101d9b09d8
URL:		http://www.maier-komor.de/mbuffer.html
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mbuffer is a tool for buffering data streams. Its special feature is
to show the I/O rate and summary to the user. This was firstly the
main reason I developed it. It is especially useful, if you are
writing backups to fast tape drives or libraries. Those drives tend to
stop and rewind if they have a buffer underrun. This so called tape
screwing reduces the lifetime of the motors. mbuffer can prevent
buffer underruns, if used correctly and speed up the whole backup
process. Please read the man page for details, how to use it.

%description -l pl
mbuffer to narz�dzie do buforowania strumieni danych. Jego cech�
szczeg�ln� jest pokazywanie u�ytkownikowi pr�dko�ci we/wy i
podsumowania - by�o to g��wnym celem stworzenia narz�dzia. Jest
szczeg�lnie przydatne przy zapisie kopii zapasowych na szybkie nap�dy
i biblioteki ta�mowe. Nap�dy te maj� tendencje do zatrzymywania si� i
cofania w przypadku opr�nienia bufora. Poprawnie u�yty mbuffer mo�e
zapobiec opr�nieniom bufora (buffer underruns) i przyspiesza ca�y
proces tworzenia kopii zapasowych. Szczeg�y dotycz�ce u�ywania
programu mo�na znale�� w manualu.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-debug

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
