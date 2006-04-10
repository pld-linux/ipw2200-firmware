#
# TODO:		- add the license to the firmware directory
#		- prepare multiversion 2.4 & 3.0 packages or %name24 for out of kernel 
#		  ipw2200 module (the one from 2.6.16.2 needs 2.4 firmware)
#
Summary:	Firmware for the Intel(R) PRO/Wireless 2200 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2200
Name:		ipw2200-firmware
Version:	3.0
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://bughost.org/firmware/ipw2200-fw-%{version}.tgz 
# Source0-md5:	34a5ed3702006f5470ebfd513e04d9eb
Source1:	ipw2x00_firmware_licence_Q_A.txt
URL:		http://ipw2200.sourceforge.net/firmware.php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ipw-2200 driver. Usage of
the firmware is subject to the terms contained in
/lib/firmware/ipw2200-LICENSE. Please read the license carefully.

%description -l pl
Ten pakiet zawiera firmware dla sterownika ipw-2200. Mo¿na go u¿ywaæ
na warunkach zawartych w pliku /lib/firmware/ipw2200-LICENSE. Proszê
uwa¿nie przeczytaæ licencjê.

%prep
%setup -q -c
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install -p ipw2200-fw-3.0/*.fw $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ipw2x00_firmware_licence_Q_A.txt
/lib/firmware/*.fw
