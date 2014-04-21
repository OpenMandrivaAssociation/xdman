Name: xdman
Version: 3.0.3
Release: 1
Summary: Xtreme Download Manager
License: GPLv2
Group:	Networking/File transfer
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}_all_linux.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: java-1.7.0-openjdk
URL: http://sourceforge.net/projects/xdman/

%description
Xtreme Download Manager is powerful tool to increase download speed up-to 500%.

%prep

%setup -c -n %{name}-%{version}

%build

%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}
mkdir ${RPM_BUILD_DIR}/%{name}-%{version}/tmp
mkdir ${RPM_BUILD_DIR}/%{name}-%{version}/tmp/usr/
mkdir ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_bindir}
mkdir ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_datadir}
mkdir ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_datadir}/%{name}

tar -xzf ${RPM_BUILD_DIR}/%{name}-%{version}/%{name}.tar.gz -C ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_datadir}

#binary
cat << EOF > ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_bindir}/xdman
#!/bin/sh
java -jar /usr/share/xdman/xdman.jar
EOF

chmod +x ${RPM_BUILD_DIR}/%{name}-%{version}/tmp%{_bindir}/xdman

#desktop entry
cat << EOF > ${RPM_BUILD_DIR}/%{name}-%{version}/%{name}-%{name}.desktop
[Desktop Entry]
Version=3.0.3
Encoding=UTF-8
Name=XDMan
GenericName=Xtreme Download Managers
Type=Application
Categories=Internet
Terminal=false
StartupNotify=true
Exec="java -jar /usr/share/xdman/xdman.jar"
Icon=/usr/share/xdman/icon.png
EOF

xdg-desktop-menu install ${RPM_BUILD_DIR}/%{name}-%{version}/%{name}-%{name}.desktop

cp -axv ${RPM_BUILD_DIR}/%{name}-%{version}/tmp ${RPM_BUILD_ROOT}/

%files
%defattr(-,root,root)
%{_bindir}/xdman
%{_datadir}/%{name}/*
