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
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="$CMAKE_PREFIX_PATH" \
        -DCMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd build
make install DESTDIR=%{buildroot}
popd

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)
