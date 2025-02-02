%define	debug_package	%nil

Summary:        An HTTP/1.1 protocol implementation together with clients and servers
Name:           python-twisted-web2
Version:        8.1.0
Release:        7
Source0:        http://tmrc.mit.edu/mirror/twisted/Web2/8.1/TwistedWeb2-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            https://twistedmatrix.com/trac/wiki/TwistedWeb2
BuildRequires:	python-devel
BuildRequires:  python3egg(twisted)
Requires:       python3dist(twisted)
Patch0:		TwistedWeb2-8.1.0-sagemath.patch
# removed, cause problem regarding submodule for twisted
#BuildArch:      noarch

%description
An HTTP protocol implementation together with clients and servers, based on 
the twisted python framework.

This version is still experimental.
%prep
%setup -q -n TwistedWeb2-%version
%patch0	-p1

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot --install-purelib=%py_platsitedir

%files
%doc LICENSE README 
%py_platsitedir/Twisted*egg-info
%py_platsitedir/twisted/web2/
%py_platsitedir/twisted/plugins/*
