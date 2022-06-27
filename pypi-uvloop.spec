#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-uvloop
Version  : 0.16.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/ab/d9/22bbffa8f8d7e075ccdb29e8134107adfb4710feb10039f9d357db8b589c/uvloop-0.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/d9/22bbffa8f8d7e075ccdb29e8134107adfb4710feb10039f9d357db8b589c/uvloop-0.16.0.tar.gz
Summary  : Fast implementation of asyncio event loop on top of libuv
Group    : Development/Tools
License  : Apache-2.0 CC-BY-4.0 MIT
Requires: pypi-uvloop-filemap = %{version}-%{release}
Requires: pypi-uvloop-lib = %{version}-%{release}
Requires: pypi-uvloop-license = %{version}-%{release}
Requires: pypi-uvloop-python = %{version}-%{release}
Requires: pypi-uvloop-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/github/workflow/status/MagicStack/uvloop/Tests
:target: https://github.com/MagicStack/uvloop/actions?query=workflow%3ATests+branch%3Amaster

%package filemap
Summary: filemap components for the pypi-uvloop package.
Group: Default

%description filemap
filemap components for the pypi-uvloop package.


%package lib
Summary: lib components for the pypi-uvloop package.
Group: Libraries
Requires: pypi-uvloop-license = %{version}-%{release}
Requires: pypi-uvloop-filemap = %{version}-%{release}

%description lib
lib components for the pypi-uvloop package.


%package license
Summary: license components for the pypi-uvloop package.
Group: Default

%description license
license components for the pypi-uvloop package.


%package python
Summary: python components for the pypi-uvloop package.
Group: Default
Requires: pypi-uvloop-python3 = %{version}-%{release}

%description python
python components for the pypi-uvloop package.


%package python3
Summary: python3 components for the pypi-uvloop package.
Group: Default
Requires: pypi-uvloop-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(uvloop)

%description python3
python3 components for the pypi-uvloop package.


%prep
%setup -q -n uvloop-0.16.0
cd %{_builddir}/uvloop-0.16.0
pushd ..
cp -a uvloop-0.16.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363638
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-uvloop
cp %{_builddir}/uvloop-0.16.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-uvloop/0ae67ae6847f6882c04a794ff158ee2152dc9f0c
cp %{_builddir}/uvloop-0.16.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-uvloop/a80e1aed8435e4474f840cd5d13449be8131c17a
cp %{_builddir}/uvloop-0.16.0/vendor/libuv/LICENSE %{buildroot}/usr/share/package-licenses/pypi-uvloop/848f7398f89046426a7ba23cb56cd3c93c030c64
cp %{_builddir}/uvloop-0.16.0/vendor/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/pypi-uvloop/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-uvloop

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-uvloop/0ae67ae6847f6882c04a794ff158ee2152dc9f0c
/usr/share/package-licenses/pypi-uvloop/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/pypi-uvloop/848f7398f89046426a7ba23cb56cd3c93c030c64
/usr/share/package-licenses/pypi-uvloop/a80e1aed8435e4474f840cd5d13449be8131c17a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
