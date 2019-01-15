Name:           ros-kinetic-message-runtime
Version:        0.4.12
Release:        0
Summary:        ROS message-runtime package
Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/message_runtime
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin
Requires:       ros-kinetic-cpp-common
Requires:       ros-kinetic-roscpp-traits
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-rostime

%description
Package modeling the run-time dependencies for language bindings of messages.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__ros_setup}
%{__ros_build}

%install
%{__ros_setup}
%{__ros_install}

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)
