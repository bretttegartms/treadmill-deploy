Name:           Treadmill_AWS
Version:        %{_version} 
Release:        %{_release}%{?dist}
Summary:        Treadmill AWS

License:        Apache 2.0
URL:            https://github.com/Morgan-Stanley/treadmill
Prefix:         /opt/treadmill
AutoReqProv:    no


%description
Treadmill (AWS)


%prep


%build


%install
cp -r %{_builddir}/opt %{buildroot}/opt


%post


%files
%defattr(-,root,root,-)
/opt/treadmill/*


%changelog
