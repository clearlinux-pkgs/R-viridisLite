#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-viridisLite
Version  : 0.3.0
Release  : 18
URL      : https://cran.r-project.org/src/contrib/viridisLite_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/viridisLite_0.3.0.tar.gz
Summary  : Default Color Maps from 'matplotlib' (Lite Version)
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
'inferno', and 'cividis' color maps for 'R'. 'viridis', 'magma', 'plasma',

%prep
%setup -q -c -n viridisLite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517769319

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1517769319
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridisLite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridisLite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridisLite
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library viridisLite|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/viridisLite/DESCRIPTION
/usr/lib64/R/library/viridisLite/INDEX
/usr/lib64/R/library/viridisLite/LICENSE
/usr/lib64/R/library/viridisLite/Meta/Rd.rds
/usr/lib64/R/library/viridisLite/Meta/data.rds
/usr/lib64/R/library/viridisLite/Meta/features.rds
/usr/lib64/R/library/viridisLite/Meta/hsearch.rds
/usr/lib64/R/library/viridisLite/Meta/links.rds
/usr/lib64/R/library/viridisLite/Meta/nsInfo.rds
/usr/lib64/R/library/viridisLite/Meta/package.rds
/usr/lib64/R/library/viridisLite/NAMESPACE
/usr/lib64/R/library/viridisLite/R/viridisLite
/usr/lib64/R/library/viridisLite/R/viridisLite.rdb
/usr/lib64/R/library/viridisLite/R/viridisLite.rdx
/usr/lib64/R/library/viridisLite/data/Rdata.rdb
/usr/lib64/R/library/viridisLite/data/Rdata.rds
/usr/lib64/R/library/viridisLite/data/Rdata.rdx
/usr/lib64/R/library/viridisLite/help/AnIndex
/usr/lib64/R/library/viridisLite/help/aliases.rds
/usr/lib64/R/library/viridisLite/help/figures/viridis-scales.png
/usr/lib64/R/library/viridisLite/help/paths.rds
/usr/lib64/R/library/viridisLite/help/viridisLite.rdb
/usr/lib64/R/library/viridisLite/help/viridisLite.rdx
/usr/lib64/R/library/viridisLite/html/00Index.html
/usr/lib64/R/library/viridisLite/html/R.css
