#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-viridisLite
Version  : 0.4.2
Release  : 58
URL      : https://cran.r-project.org/src/contrib/viridisLite_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/viridisLite_0.4.2.tar.gz
Summary  : Colorblind-Friendly Color Maps (Lite Version)
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
common forms of color blindness and/or color vision deficiency. The color 
    maps are also perceptually-uniform, both in regular form and also when 
    converted to black-and-white for printing. This is the 'lite' version of the 
    'viridis' package that also contains 'ggplot2' bindings for discrete and 
    continuous color and fill scales and can be found at

%prep
%setup -q -n viridisLite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683149190

%install
export SOURCE_DATE_EPOCH=1683149190
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/viridisLite/CITATION
/usr/lib64/R/library/viridisLite/DESCRIPTION
/usr/lib64/R/library/viridisLite/INDEX
/usr/lib64/R/library/viridisLite/LICENSE
/usr/lib64/R/library/viridisLite/Meta/Rd.rds
/usr/lib64/R/library/viridisLite/Meta/features.rds
/usr/lib64/R/library/viridisLite/Meta/hsearch.rds
/usr/lib64/R/library/viridisLite/Meta/links.rds
/usr/lib64/R/library/viridisLite/Meta/nsInfo.rds
/usr/lib64/R/library/viridisLite/Meta/package.rds
/usr/lib64/R/library/viridisLite/NAMESPACE
/usr/lib64/R/library/viridisLite/NEWS.md
/usr/lib64/R/library/viridisLite/R/viridisLite
/usr/lib64/R/library/viridisLite/R/viridisLite.rdb
/usr/lib64/R/library/viridisLite/R/viridisLite.rdx
/usr/lib64/R/library/viridisLite/help/AnIndex
/usr/lib64/R/library/viridisLite/help/aliases.rds
/usr/lib64/R/library/viridisLite/help/figures/logo.png
/usr/lib64/R/library/viridisLite/help/figures/maps.png
/usr/lib64/R/library/viridisLite/help/figures/viridis-scales.png
/usr/lib64/R/library/viridisLite/help/paths.rds
/usr/lib64/R/library/viridisLite/help/viridisLite.rdb
/usr/lib64/R/library/viridisLite/help/viridisLite.rdx
/usr/lib64/R/library/viridisLite/html/00Index.html
/usr/lib64/R/library/viridisLite/html/R.css
/usr/lib64/R/library/viridisLite/tests/testthat.R
/usr/lib64/R/library/viridisLite/tests/testthat/test-palettes.R
