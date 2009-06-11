%define base_name	mozart
%define name		%{base_name}-std
%define version     1.4.0
%define date        20080704
%define release		%mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Mozart standard library
License:	    Mozart License
Url:		    http://www.mozart-oz.org/
Group:		    Development/Other
Source0:	    ftp://ftp.mozart-oz.org/pub/%{version}/tar/%{base_name}-%{version}.%{date}-std.tar.gz
Patch0:		    %{name}-1.3.1.20040616.fhs.patch.bz2
BuildRequires:	mozart = %{version}
Requires:	    mozart = %{version}
ExclusiveArch:  %{ix86}
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This is the standard library for the Mozart Programming System. It currently
includes modules for common abstract datatypes, QTk (Window programming) and an
XML Parser.

%prep
%setup -q -n %{base_name}-%{version}.%{date}-std
%patch0 -p1

%build
%configure --prefix=%{_datadir}/%{base_name}
%make

%install
rm -rf %{buildroot}

# generic install
make PREFIX=%{buildroot}%{_datadir}/%{base_name} install

# move binaries to their proper places
install -d -m 755 %{buildroot}%{_bindir}
for f in ozmake; do \
	mv %{buildroot}%{_datadir}/%{base_name}/bin/$f %{buildroot}%{_bindir}
done

# install man pages
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 ozmake/ozmake.1 %{buildroot}%{_mandir}/man1

# move the documentation and the examples 
install -d -m 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{base_name}/doc \
	%{buildroot}%{_docdir}/%{name}
install -m 644 README %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{base_name}/cache/x-oz/system/*
%{_docdir}/%{name}
