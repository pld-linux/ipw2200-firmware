Summary:	Firmware for the Intel(R) PRO/Wireless 2200 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2200
Name:		ipw2200-firmware
Version:	2
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://bughost.org/firmware/ipw2200-fw-2.0.tgz
# Source0-md5:	8bdad731fb923a9fe1921358202f4f0f
Source1:	ipw2x00_firmware_licence_Q_A.txt
URL:		http://ipw2200.sourceforge.net/firmware.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains the firmware for the ipw-2200 driver. Usage of
the firmware is subject to the terms contained in
%{sysconfdir}/ipw2200-LICENSE. Please read the license
carefully.

%description -l pl
Ten pakiet zawiera firmware dla sterownika ipw-2200. Mo¿na go u¿ywaæ
na warunkach zawartych w pliku
%{sysconfdir}/ipw2200-LICENSE. Proszê uwa¿nie
przeczytaæ licencjê.

%prep
%setup -q -c
gunzip -c ipw2200-fw-%{version}.tgz | tar -xf -

cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/firmware
install -d $RPM_BUILD_ROOT/lib/firmware

install -p *.fw $RPM_BUILD_ROOT%{_sysconfdir}/firmware
cp -df LICENSE $RPM_BUILD_ROOT%{_sysconfdir}/firmware/ipw2200-LICENSE
cd $RPM_BUILD_ROOT%{_sysconfdir}/firmware
for file in *; do
	ln -s %{_sysconfdir}/firmware/$file $RPM_BUILD_ROOT/lib/firmware
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ipw2x00_firmware_licence_Q_A.txt
%{_sysconfdir}/firmware/ipw2200-LICENSE
%{_sysconfdir}/firmware/*.fw
/lib/firmware/*.fw
