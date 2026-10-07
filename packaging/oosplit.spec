Name:           oosplit
Version:        0.1.0
Release:        1%{?dist}
Summary:        Splits large datasets into fixed-size byte chunks or line-bounded parts with hashes.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosplit
Source0:        oosplit-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosplit is a sovereign, capability-bounded FILE SPLITTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosplit
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosplit-uninstall

%files
/usr/bin/oosplit
/usr/bin/oosplit-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
