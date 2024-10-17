Name: xdman
Version: 5.0.74
Release: 1
Summary: Xtreme Download Manager
License: GPLv2
Group:	Networking/File transfer
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}.zip
BuildArch: noarch
Requires: java-1.8.0-openjdk
BuildRequires: xdg-utils
URL: https://sourceforge.net/projects/xdman/

%description
Xtreme Download Manager is powerful tool to increase download speed up-to 500%.

%prep

%setup -c -n %{name}-%{version}

%build

%install
mkdir -p tmp/%{_bindir}
mkdir -p tmp/%{_datadir}/%{name}

unzip -d tmp/%{_datadir}/%{name} %SOURCE0 

#binary
cat << EOF > tmp%{_bindir}/xdman
#!/bin/sh
java -jar /usr/share/xdman/xdman.jar
EOF

chmod +x tmp%{_bindir}/xdman

#desktop entry
cat << EOF > %{name}-%{name}.desktop
[Desktop Entry]
Version=%{version}
Encoding=UTF-8
Name=XDMan
GenericName=Xtreme Download Managers
Type=Application
Categories=Internet
Terminal=false
StartupNotify=true
Exec="java -jar /usr/share/xdman/xdm.jar"
Icon=/usr/share/xdman/icon.png
EOF

xdg-desktop-menu install %{name}-%{name}.desktop

cp -axv tmp/* %{buildroot}/

%files
%defattr(-,root,root)
%{_bindir}/xdman
%{_datadir}/%{name}/*
