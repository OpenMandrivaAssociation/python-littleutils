%define module littleutils

Name:		python-littleutils
Version:	0.2.4
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/l/littleutils/%{module}-%{version}.tar.gz
Summary:	Small personal collection of python utility functions
URL:		https://pypi.org/project/littleutils/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
Small personal collection of python utility functions

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.*-info
%license LICENSE
