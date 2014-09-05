Name:           ros-indigo-random-numbers
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS random_numbers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/random_numbers
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin

%description
This library contains wrappers for generating floating point values, integers,
quaternions using boost libraries. The constructor of the wrapper is guaranteed
to be thread safe and initialize its random number generator to a random seed.
Seeds are obtained using a separate and different random number generator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Sep 05 2014 Ioan Sucan <isucan@willowgarage.com> - 0.3.0-0
- Autogenerated by Bloom

