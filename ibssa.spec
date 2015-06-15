# TODO: PLDize init script
Summary:	InfiniBand SSA service
Summary(pl.UTF-8):	Usługa InfiniBand SSA
Name:		ibssa
Version:	0.0.8
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	https://www.openfabrics.org/downloads/management/ssa/%{name}-%{version}.tar.gz
# Source0-md5:	d287b22ee37dee7ba385fade87b0b422
URL:		https://www.openfabrics.org/
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	libibumad-devel >= 1.3.10
BuildRequires:	libibverbs-devel >= 1.1.8
BuildRequires:	librdmacm-devel >= 1.0.21
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.2
Requires:	libibumad >= 1.3.10
Requires:	libibverbs >= 1.1.8
Requires:	librdmacm >= 1.0.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The InfiniBand SSA service provides a user space implementation of a
distributed SA currently resolving path record lookups.

%description -l pl.UTF-8
Usługa InfiniBand SSA dostarcza implementację przestrzeni użytkownika
rozproszonego SA, obecnie odpowiadającego na zapytania o rekordy
ścieżek.

%prep
%setup -q

%build
%configure \
	rdmascript=rdma \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d
%{__mv} $RPM_BUILD_ROOT/etc/init.d $RPM_BUILD_ROOT/etc/rc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ibssa_opts.cfg ssa_release_notes.txt
%attr(755,root,root) %{_sbindir}/ibssa
#%attr(754,root,root) /etc/rc.d/init.d/ibssa
