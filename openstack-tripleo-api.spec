%{?!_licensedir:%global license %%doc}

Name:           openstack-tripleo-api
Summary:        A REST API that works on top of the python-tripleo library
Version:        XXX
Release:        XXX
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://github.com/openstack/tripleo

Source0: https://github.com/openstack/tripleo/archive/tripleo-api-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-tripleo


%prep
%autosetup -v -p 1 -n %{name}-%{upstream_version}
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%description
A REST API that works on top of the python-tripleo library

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python2_sitelib}/openstack-tripleo-api*
%exclude %{python2_sitelib}/openstack-tripleo-api/test*


%changelog
