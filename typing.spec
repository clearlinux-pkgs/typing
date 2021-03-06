#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing
Version  : 3.7.4.1
Release  : 34
URL      : https://files.pythonhosted.org/packages/67/b0/b2ea2bd67bfb80ea5d12a5baa1d12bda002cab3b6c9b48f7708cd40c34bf/typing-3.7.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/67/b0/b2ea2bd67bfb80ea5d12a5baa1d12bda002cab3b6c9b48f7708cd40c34bf/typing-3.7.4.1.tar.gz
Summary  : Type Hints for Python
Group    : Development/Tools
License  : Python-2.0
Requires: typing-license = %{version}-%{release}
Requires: typing-python = %{version}-%{release}
Requires: typing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

NOTE: in Python 3.5 and later, the typing module lives in the stdlib,
and installing this package has NO EFFECT.  To get a newer version of
the typing module in Python 3.5 or later, you have to upgrade to a
newer Python (bugfix) version.  For example, typing in Python 3.6.0 is
missing the definition of 'Type' -- upgrading to 3.6.2 will fix this.

Also note that most improvements to the typing module in Python 3.7
will not be included in this package, since Python 3.7 has some
built-in support that is not present in older versions (See PEP 560.)

%package license
Summary: license components for the typing package.
Group: Default

%description license
license components for the typing package.


%package python
Summary: python components for the typing package.
Group: Default
Requires: typing-python3 = %{version}-%{release}

%description python
python components for the typing package.


%package python3
Summary: python3 components for the typing package.
Group: Default
Requires: python3-core
Provides: pypi(typing)

%description python3
python3 components for the typing package.


%prep
%setup -q -n typing-3.7.4.1
cd %{_builddir}/typing-3.7.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582907884
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typing
cp %{_builddir}/typing-3.7.4.1/LICENSE %{buildroot}/usr/share/package-licenses/typing/7ad627868f90ad068bd06801aab97ec1ca34b890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typing/7ad627868f90ad068bd06801aab97ec1ca34b890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
