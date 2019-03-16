#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-promises
Version  : 1.0.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/promises_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/promises_1.0.1.tar.gz
Summary  : Abstractions for Promise-Based Asynchronous Programming
Group    : Development/Tools
License  : MIT
Requires: R-promises-lib
Requires: R-Rcpp
Requires: R-future
Requires: R-later
Requires: R-purrr
BuildRequires : R-Rcpp
BuildRequires : R-future
BuildRequires : R-later
BuildRequires : R-purrr
BuildRequires : clr-R-helpers

%description
in R using promises. Asynchronous programming is useful for allowing a single
    R process to orchestrate multiple tasks in the background while also attending
    to something else. Semantics are similar to 'JavaScript' promises, but with a
    syntax that is idiomatic R.

%package lib
Summary: lib components for the R-promises package.
Group: Libraries

%description lib
lib components for the R-promises package.


%prep
%setup -q -c -n promises

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526837773

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1526837773
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library promises
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library promises
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library promises
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library promises|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/promises/DESCRIPTION
/usr/lib64/R/library/promises/INDEX
/usr/lib64/R/library/promises/LICENSE
/usr/lib64/R/library/promises/Meta/Rd.rds
/usr/lib64/R/library/promises/Meta/features.rds
/usr/lib64/R/library/promises/Meta/hsearch.rds
/usr/lib64/R/library/promises/Meta/links.rds
/usr/lib64/R/library/promises/Meta/nsInfo.rds
/usr/lib64/R/library/promises/Meta/package.rds
/usr/lib64/R/library/promises/Meta/vignette.rds
/usr/lib64/R/library/promises/NAMESPACE
/usr/lib64/R/library/promises/NEWS.md
/usr/lib64/R/library/promises/R/promises
/usr/lib64/R/library/promises/R/promises.rdb
/usr/lib64/R/library/promises/R/promises.rdx
/usr/lib64/R/library/promises/doc/combining.Rmd
/usr/lib64/R/library/promises/doc/combining.html
/usr/lib64/R/library/promises/doc/futures.Rmd
/usr/lib64/R/library/promises/doc/futures.html
/usr/lib64/R/library/promises/doc/index.html
/usr/lib64/R/library/promises/doc/intro.Rmd
/usr/lib64/R/library/promises/doc/intro.html
/usr/lib64/R/library/promises/doc/motivation.Rmd
/usr/lib64/R/library/promises/doc/motivation.html
/usr/lib64/R/library/promises/doc/overview.Rmd
/usr/lib64/R/library/promises/doc/overview.html
/usr/lib64/R/library/promises/doc/shiny.Rmd
/usr/lib64/R/library/promises/doc/shiny.html
/usr/lib64/R/library/promises/help/AnIndex
/usr/lib64/R/library/promises/help/aliases.rds
/usr/lib64/R/library/promises/help/paths.rds
/usr/lib64/R/library/promises/help/promises.rdb
/usr/lib64/R/library/promises/help/promises.rdx
/usr/lib64/R/library/promises/html/00Index.html
/usr/lib64/R/library/promises/html/R.css
/usr/lib64/R/library/promises/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/promises/libs/promises.so
/usr/lib64/R/library/promises/libs/promises.so.avx2
/usr/lib64/R/library/promises/libs/promises.so.avx512
