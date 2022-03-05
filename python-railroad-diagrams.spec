#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Generate SVG railroad syntax diagrams, like on JSON.org
Summary(pl.UTF-8):	Generowanie diagramów składniowych SVG, jak na JSON.org
Name:		python-railroad-diagrams
Version:	1.1.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/railroad-diagrams/
Source0:	https://files.pythonhosted.org/packages/source/r/railroad-diagrams/railroad-diagrams-%{version}.tar.gz
# Source0-md5:	594e2552106be714d01adbfd4329c274
URL:		https://pypi.org/project/railroad-diagrams/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
# "railroad" dir shadows railroad.py
Conflicts:	python-railroad
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small library for generating railroad diagrams (like what
JSON.org uses) using SVG, with both JS and Python ports.

%description -l pl.UTF-8
Mała biblioteka do generowania diagramów składniowych (podobnych do
tych, których używa JSON.org) przy użyciu SVG, mająca porty w JS i
Pythonie.

%package -n python3-railroad-diagrams
Summary:	Generate SVG railroad syntax diagrams, like on JSON.org
Summary(pl.UTF-8):	Generowanie diagramów składniowych SVG, jak na JSON.org
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
# "railroad" dir shadows railroad.py
Conflicts:	python3-railroad

%description -n python3-railroad-diagrams
This is a small library for generating railroad diagrams (like what
JSON.org uses) using SVG, with both JS and Python ports.

%description -n python3-railroad-diagrams -l pl.UTF-8
Mała biblioteka do generowania diagramów składniowych (podobnych do
tych, których używa JSON.org) przy użyciu SVG, mająca porty w JS i
Pythonie.

%package apidocs
Summary:	API documentation for Python railroad-diagrams module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona railroad-diagrams
Group:		Documentation

%description apidocs
API documentation for Python railroad-diagrams module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona railroad-diagrams.

%prep
%setup -q -n railroad-diagrams-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md README-py.md
%{py_sitescriptdir}/railroad.py[co]
%{py_sitescriptdir}/railroad_diagrams-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-railroad-diagrams
%defattr(644,root,root,755)
%doc README.md README-py.md
%{py3_sitescriptdir}/railroad.py
%{py3_sitescriptdir}/__pycache__/railroad.cpython-*.py[co]
%{py3_sitescriptdir}/railroad_diagrams-%{version}-py*.egg-info
%endif
