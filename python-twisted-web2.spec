%define version 8.1.0
%define rel 2

Summary:        An HTTP/1.1 protocol implementation together with clients and servers
Name:           python-twisted-web2
Version: %version
Release: %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Web2/8.1/TwistedWeb2-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedWeb2
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# removed, cause problem regarding submodule for twisted
#BuildArch:      noarch

%description
An HTTP protocol implementation together with clients and servers, based on 
the twisted python framework.

This version is still experimental.
%prep
%setup -q -n TwistedWeb2-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root %buildroot --install-purelib=%py_platsitedir


%clean
%__rm -rf %buildroot
 
%files
%defattr(0755,root,root,0755)
%defattr(0644,root,root,0755)
%doc LICENSE README 
%if %mdkversion >= 200710
%py_platsitedir/Twisted*egg-info
%endif
%py_platsitedir/twisted/web2/
%py_platsitedir/twisted/plugins/*


