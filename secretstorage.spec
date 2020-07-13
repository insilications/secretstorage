#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6646265B586B83CB (mitya57@gmail.com)
#
Name     : secretstorage
Version  : 3.1.2
Release  : 33
URL      : https://files.pythonhosted.org/packages/fd/9f/36197c75d9a09b1ab63f56cb985af6cd858ca3fc41fd9cd890ce69bae5b9/SecretStorage-3.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/9f/36197c75d9a09b1ab63f56cb985af6cd858ca3fc41fd9cd890ce69bae5b9/SecretStorage-3.1.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/fd/9f/36197c75d9a09b1ab63f56cb985af6cd858ca3fc41fd9cd890ce69bae5b9/SecretStorage-3.1.2.tar.gz.asc
Summary  : Python bindings to FreeDesktop.org Secret Service API
Group    : Development/Tools
License  : BSD-3-Clause
Requires: secretstorage-license = %{version}-%{release}
Requires: secretstorage-python = %{version}-%{release}
Requires: secretstorage-python3 = %{version}-%{release}
Requires: cryptography
Requires: jeepney
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : jeepney

%description
.. image:: https://api.travis-ci.org/mitya57/secretstorage.svg
:target: https://travis-ci.org/mitya57/secretstorage
:alt: Travis CI status
.. image:: https://codecov.io/gh/mitya57/secretstorage/branch/master/graph/badge.svg
:target: https://codecov.io/gh/mitya57/secretstorage
:alt: Coverage status
.. image:: https://readthedocs.org/projects/secretstorage/badge/?version=latest
:target: https://secretstorage.readthedocs.io/en/latest/
:alt: ReadTheDocs status

%package license
Summary: license components for the secretstorage package.
Group: Default

%description license
license components for the secretstorage package.


%package python
Summary: python components for the secretstorage package.
Group: Default
Requires: secretstorage-python3 = %{version}-%{release}

%description python
python components for the secretstorage package.


%package python3
Summary: python3 components for the secretstorage package.
Group: Default
Requires: python3-core
Provides: pypi(secretstorage)
Requires: pypi(cryptography)
Requires: pypi(jeepney)

%description python3
python3 components for the secretstorage package.


%prep
%setup -q -n SecretStorage-3.1.2
cd %{_builddir}/SecretStorage-3.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583509244
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/secretstorage
cp %{_builddir}/SecretStorage-3.1.2/LICENSE %{buildroot}/usr/share/package-licenses/secretstorage/b23eb98a71ae4e71270872be9d167f785ad043d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/secretstorage/b23eb98a71ae4e71270872be9d167f785ad043d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
