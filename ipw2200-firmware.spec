Summary:	Firmware for the Intel(R) PRO/Wireless 2200 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2200
Name:		ipw2200-firmware
Version:	2.3
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	ipw2200-fw-%{version}.tgz
# Source0-md5:	487ba63b1bf98bc1e38059b6d3abea44
Source1:	ipw2x00_firmware_licence_Q_A.txt
URL:		http://ipw2200.sourceforge.net/firmware.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains the firmware for the ipw-2200 driver. Usage of
the firmware is subject to the terms contained in /%{_lib}/ipw2200-LICENSE.
Please read the license carefully.

%description -l pl
Ten pakiet zawiera firmware dla sterownika ipw-2200. Mo¿na go u¿ywaæ
na warunkach zawartych w pliku /%{_lib}/ipw2200-LICENSE.
Proszê uwa¿nie przeczytaæ licencjê.

%prep
%setup -q -c
gunzip -c ipw2200-fw-%{version}.tgz | tar -xf -

cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/firmware

install -p *.fw $RPM_BUILD_ROOT/%{_lib}/firmware
cp -df LICENSE $RPM_BUILD_ROOT/%{_lib}/firmware/ipw2200-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ipw2x00_firmware_licence_Q_A.txt
/%{_lib}/firmware/ipw2200-LICENSE
/%{_lib}/firmware/*.fw
