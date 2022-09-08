Summary:       Babel
Name:          python3-babel
Version:       0
Release:       1
License:       BSD and Unicode
Source0:       %{name}-%{version}.tar.gz
Source1:       cldr-common-41.0.zip
URL:           https://github.com/sailfishos/python3-babel

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytz

%description
Python Internationalization Library

%package -n babel
Summary: Tools for internationalizing Python applications
Requires: %{name} = %{version}-%{release}

%description -n babel
Tools for internationalizing Python applications

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
cp %{SOURCE1} cldr/
%python3 ./setup.py import_cldr
%py3_build

%install
%py3_install

%files
%defattr (-,root,root,-)
%license LICENSE cldr/cldr-common-*/LICENSE.txt
%{python3_sitelib}/babel/
%{python3_sitelib}/*.egg-info

%files -n babel
%defattr (-,root,root,-)
%{_bindir}/pybabel
