Name:           %{product}-tools
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Scylla Tools
Group:          Applications/Databases

License:        Apache
URL:            http://www.scylladb.com/
Source0:        %{reloc_pkg}
BuildArch:      noarch
Requires:       %{product}-conf %{product}-tools-core
AutoReqProv:    no
Conflicts:      cassandra

%description

%package core
License:        Apache
URL:            http://www.scylladb.com/
BuildArch:      noarch
Requires:       java-headless
Summary:        Core files for Scylla tools
Version:        %{version}
Release:        %{release}%{?dist}
Requires:       jre-1.8.0-headless python2
# Since RHEL7 and RHEL8 has different pacakge name for pyyaml,
# we need to use a file path to the resolve package name on
# current distribution.
Requires:       /usr/lib64/python2.7/site-packages/yaml/__init__.py

%global __brp_python_bytecompile %{nil}
%global __brp_mangle_shebangs %{nil}

%description core
Core files for scylla tools.

%prep
%setup -q -n scylla-tools


%build

%install
rm -rf $RPM_BUILD_ROOT
./install.sh --root "$RPM_BUILD_ROOT"

%files
%{_sysconfdir}/bash_completion.d/nodetool-completion
/opt/scylladb/share/cassandra/bin/nodetool
/opt/scylladb/share/cassandra/bin/sstableloader
/opt/scylladb/share/cassandra/bin/cqlsh
/opt/scylladb/share/cassandra/bin/cqlsh.py
/opt/scylladb/share/cassandra/bin/cassandra-stress
/opt/scylladb/share/cassandra/bin/cassandra-stressd
/opt/scylladb/share/cassandra/bin/sstabledump
/opt/scylladb/share/cassandra/bin/sstablelevelreset
/opt/scylladb/share/cassandra/bin/sstablemetadata
/opt/scylladb/share/cassandra/bin/sstablerepairedset
%{_bindir}/nodetool
%{_bindir}/sstableloader
%{_bindir}/cqlsh
%{_bindir}/cqlsh.py
%{_bindir}/cassandra-stress
%{_bindir}/cassandra-stressd
%{_bindir}/sstabledump
%{_bindir}/sstablelevelreset
%{_bindir}/sstablemetadata
%{_bindir}/sstablerepairedset
/opt/scylladb/share/cassandra/pylib/*

%files core
%{_sysconfdir}/scylla/cassandra/cassandra-env.sh
%{_sysconfdir}/scylla/cassandra/logback.xml
%{_sysconfdir}/scylla/cassandra/logback-tools.xml
%{_sysconfdir}/scylla/cassandra/jvm*.options
%{_bindir}/scylla-sstableloader
/opt/scylladb/share/cassandra/bin/cassandra.in.sh
/opt/scylladb/share/cassandra/lib/*.jar
/opt/scylladb/share/cassandra/lib/*.zip
/opt/scylladb/share/cassandra/lib/licenses
/opt/scylladb/share/cassandra/doc/cql3/CQL.css
/opt/scylladb/share/cassandra/doc/cql3/CQL.html
/opt/scylladb/share/cassandra/bin/scylla-sstableloader

%changelog
* Fri Aug  7 2015 Takuya ASADA Takuya ASADA <syuu@cloudius-systems.com>
- inital version of scylla-tools.spec