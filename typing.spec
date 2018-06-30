#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing
Version  : 3.6.4
Release  : 18
URL      : http://pypi.debian.net/typing/typing-3.6.4.tar.gz
Source0  : http://pypi.debian.net/typing/typing-3.6.4.tar.gz
Summary  : Type Hints for Python
Group    : Development/Tools
License  : Python-2.0
Requires: typing-python3
Requires: typing-license
Requires: typing-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
This is a backport of the standard library typing module to Python
        versions older than 3.5.  (See note below for newer versions.)
        
        Typing defines a standard notation for Python function and variable
        type annotations. The notation can be used for documenting code in a
        concise, standard format, and it has been designed to also be used by
        static and runtime type checkers, static analyzers, IDEs and other
        tools.

%package legacypython
Summary: legacypython components for the typing package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the typing package.


%package license
Summary: license components for the typing package.
Group: Default

%description license
license components for the typing package.


%package python
Summary: python components for the typing package.
Group: Default
Requires: typing-python3

%description python
python components for the typing package.


%package python3
Summary: python3 components for the typing package.
Group: Default
Requires: python3-core

%description python3
python3 components for the typing package.


%prep
%setup -q -n typing-3.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530377913
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530377913
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/typing
cp LICENSE %{buildroot}/usr/share/doc/typing/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/typing/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
