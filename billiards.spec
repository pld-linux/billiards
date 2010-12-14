Summary:	Free cue sports simulator
Summary(pl.UTF-8):	Darmowy symulator bilarda
Name:		billiards
Version:	0.4
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://download.savannah.gnu.org/releases/billiards/%{name}-%{version}.tar.gz
# Source0-md5:	6bcee44199f85a7b6710dc0e06f0db75
URL:		http://www.nongnu.org/billiards/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua51
BuildRequires:	sed >= 4.0
BuildRequires:	techne
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Billiards is a free cue sports simulator. It aims for physical
accuracy and simplicity and should hopefully be useful for practicing
billiards on your own and against your friends when a real pool table
is not available.

%description -l pl.UTF-8
Billiards to darmowy symulator bilarda. Jego celem jest dokładne
odwzorowanie praw fizyki i prostota. Jest przydatny dla osób, które
chcą rozwijać swoje umiejętności bilardowe grając w pojedynkę lub z
przyjaciółmi, gdy prawdziwy stół bilardowy nie jest dostępny.

%prep
%setup -q
%{__sed} -i 's,techne/,,' src/Makefile.am
%{__sed} -i 's,/techne,,;s,@techne@,%{_bindir}/techne.bin,' src/billiards.in
%{__sed} -i 's,billiards/,%{_datadir}/billiards/,' src/billiards.lua

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove symlink
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man6/billiards-browser.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/billiards
%attr(755,root,root) %{_bindir}/billiards-browser
%{_datadir}/%{name}
%{_mandir}/man6/*.6*
