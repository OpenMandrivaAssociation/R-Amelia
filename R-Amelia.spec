%global packname Amelia
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.7.2 
Release:          1
Summary:          Amelia II: A Program for Missing Data
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-core >= 2.15.3 R-foreign R-utils R-Rcpp >= 0.10.0.4 R-RcppArmadillo
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-core >= 2.15.3 R-foreign R-utils R-Rcpp >= 0.10.0.4 R-RcppArmadillo

%description
Amelia II multiply imputes missing data in a single
cross-section (such as a survey), from a time series (like
variables collected for each year in a country), or from a
time-series-cross-sectional data set (such as collected by
years for each of several countries). Amelia II implements our
bootstrapping-based algorithm that gives essentially the same
answers as the standard IP or EMis approaches, is usually
considerably faster than existing approaches and can handle
many more variables. Unlike Amelia I and other statistically
rigorous imputation software, it virtually never crashes (but
please let us know if you ﬁnd to the contrary!). The program
also generalizes existing approaches by allowing for trends in
time series across observations within a crosssectional unit,
as well as priors that allow experts to incorporate beliefs
they have about the values of missing cells in their data.
Amelia II also includes useful diagnostics of the ﬁt of
multiple imputation models. The program works from the R
command line or via a graphical user interface that does not
require users to know R.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/gui
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/test
