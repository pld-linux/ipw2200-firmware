#
# TODO:
# - separate old firmware's to some compat subpackage?
#
Summary:	Firmware for the Intel(R) PRO/Wireless 2200 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2200
Name:		ipw2200-firmware
Version:	3.0
Release:	2
License:	distributable
Group:		System Environment/Kernel
Source0:	http://bughost.org/firmware/ipw2200-fw-%{version}.tgz 
# Source0-md5:	34a5ed3702006f5470ebfd513e04d9eb
Source1:	ipw2x00_firmware_licence_Q_A.txt
Source22:	http://bughost.org/firmware/ipw2200-fw-2.2.tgz
# Source22-md5:	6892abab05d5391c08933e19b49b86b5
Source23:	http://bughost.org/firmware/ipw2200-fw-2.3.tgz
# Source23-md5:	487ba63b1bf98bc1e38059b6d3abea44
Source24:	http://bughost.org/firmware/ipw2200-fw-2.4.tgz
# Source24-md5:	a5bc066d23900852a04711c5d33987d4
Source30:	http://bughost.org/firmware/ipw2200-fw-3.0.tgz
# Source30-md5:	34a5ed3702006f5470ebfd513e04d9eb
URL:		http://ipw2200.sourceforge.net/firmware.php
BuildArch:	noarch
Provides:	ipw2200-firmware = 2.2
Provides:	ipw2200-firmware = 2.3
Provides:	ipw2200-firmware = 2.4
Provides:	ipw2200-firmware = 3.0
Obsoletes:	ipw2200-firmware2.2
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
%setup -q -c -a22 -a23 -a24 -a30
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install -p ipw2200-fw-%{version}/*.fw $RPM_BUILD_ROOT/lib/firmware
install -p ipw2200-fw-%{version}/LICENSE.ipw2200-fw $RPM_BUILD_ROOT/lib/firmware/ipw2200-LICENSE

# Firmwares 2.2, 2.3 and 2.4:
install -p *-2.2-*.fw $RPM_BUILD_ROOT/lib/firmware
install -p *-2.3-*.fw $RPM_BUILD_ROOT/lib/firmware
install -p *-2.4-*.fw $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ipw2x00_firmware_licence_Q_A.txt
/lib/firmware/ipw2200-LICENSE
/lib/firmware/*.fw
