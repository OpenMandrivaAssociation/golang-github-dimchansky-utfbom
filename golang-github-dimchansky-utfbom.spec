# Run tests in check section
%bcond_without check

%global goipath         github.com/dimchansky/utfbom
%global commit          6c6132ff69f0f6c088739067407b5d32c52e1d0f

%global common_description %{expand:
The package utfbom implements the detection of the BOM (Unicode Byte Order 
Mark) and removing as necessary. It can also return the encoding detected 
by the BOM.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Detection of the BOM and removing as necessary
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6c6132f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git6c6132f
- First package for Fedora

