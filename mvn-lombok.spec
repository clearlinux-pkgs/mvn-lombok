#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-lombok
Version  : 1.16.20
Release  : 1
URL      : https://github.com/rzwitserloot/lombok/archive/v1.16.20.tar.gz
Source0  : https://github.com/rzwitserloot/lombok/archive/v1.16.20.tar.gz
Source1  : https://repo1.maven.org/maven2/org/projectlombok/lombok/1.16.20/lombok-1.16.20.jar
Source2  : https://repo1.maven.org/maven2/org/projectlombok/lombok/1.16.20/lombok-1.16.20.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-lombok-data = %{version}-%{release}
Requires: mvn-lombok-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Project Lombok makes java a spicier language by adding 'handlers' that know how to build and compile simple, boilerplate-free, not-quite-java code.
See LICENSE for the Project Lombok license.

%package data
Summary: data components for the mvn-lombok package.
Group: Data

%description data
data components for the mvn-lombok package.


%package license
Summary: license components for the mvn-lombok package.
Group: Default

%description license
license components for the mvn-lombok package.


%prep
%setup -q -n lombok-1.16.20

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-lombok
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-lombok/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20/lombok-1.16.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20/lombok-1.16.20.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20/lombok-1.16.20.jar
/usr/share/java/.m2/repository/org/projectlombok/lombok/1.16.20/lombok-1.16.20.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-lombok/LICENSE
