#
# spec file for package python-prometheus_client
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%global srcname prometheus_client
%global sum Python client for the Prometheus monitoring system

%bcond_without test
Name:           python-%{srcname}
Version:        0.0.20
Release:        1%{?dist}
License:        Apache-2.0
Summary:        %{sum}
Url:            https://github.com/prometheus/client_python
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/prometheus_client/%{srcname}-%{version}.tar.gz
BuildRequires:  python2-devel python%{python3_pkgversion}-devel
BuildRequires:  python2-setuptools python%{python3_pkgversion}-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This library provides an API for exporting metrics from a Python application.
It provides classes for the metric types, and an HTTP server to expose the
metrics to Prometheus.

When using Linux, the process CPU, RAM, file descriptor usage and start time
will also be exported.

Along with the HTTP server to expose metrics, you can also write the metrics
to a text file to be exported by the prometheus-node-exporter, or push them to
the prometheus-pushgateway.

This library also includes support for re-exporting Graphite metrics to
Prometheus, custom collectors to proxy metrics for other systems and a parser
for the Prometheus text format.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
%description -n python2-%{srcname}
This library provides an API for exporting metrics from a Python application.
It provides classes for the metric types, and an HTTP server to expose the
metrics to Prometheus.

When using Linux, the process CPU, RAM, file descriptor usage and start time
will also be exported.

Along with the HTTP server to expose metrics, you can also write the metrics
to a text file to be exported by the prometheus-node-exporter, or push them to
the prometheus-pushgateway.

This library also includes support for re-exporting Graphite metrics to
Prometheus, custom collectors to proxy metrics for other systems and a parser
for the Prometheus text format.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
This library provides an API for exporting metrics from a Python application.
It provides classes for the metric types, and an HTTP server to expose the
metrics to Prometheus.

When using Linux, the process CPU, RAM, file descriptor usage and start time
will also be exported.

Along with the HTTP server to expose metrics, you can also write the metrics
to a text file to be exported by the prometheus-node-exporter, or push them to
the prometheus-pushgateway.

This library also includes support for re-exporting Graphite metrics to
Prometheus, custom collectors to proxy metrics for other systems and a parser
for the Prometheus text format.


%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%defattr(-,root,root,-)
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog

