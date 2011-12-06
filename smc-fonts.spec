%define	fontname	smc
%define	fontconf	90-%{fontname}

# Common description
%define common_desc \
The SMC Fonts package contains fonts for the display of\
traditional and new Malayalam Script.

Name:		%{fontname}-fonts
Version:	04.2
Release:	11%{?dist}
Summary:	Open Type Fonts for Malayalam script
Group:		User Interface/X
License:	GPLv3+ with exceptions and GPLv2+ with exceptions and GPLv2+ and  GPLv2 and GPL+
URL:		http://savannah.nongnu.org/projects/smc
Source0:	http://download.savannah.gnu.org/releases-noredirect/smc/fonts/malayalam-fonts-04.2.zip
Source1: 65-0-smc-meera.conf
Source2: 67-smc-anjalioldlipi.conf
Source3: 67-smc-dyuthi.conf
Source4: 67-smc-kalyani.conf
Source5: 67-smc-rachana.conf
Source6: 67-smc-raghumalayalam.conf
Source7: 67-smc-suruma.conf
Source8: AnjaliOldLipi-license-confirmation-email.txt
Source9: http://download.savannah.gnu.org/releases-noredirect/smc/fonts/malayalam-fonts-4.3/Meera/Meera.sfd
Source10: generate.pe
BuildArch:	noarch
BuildRequires: fontforge >= 20080429
BuildRequires:	fontpackages-devel > 1.13
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch1: bug-545683.patch
Patch2: bug-590586.patch
Patch3: bug-555678.patch

%description
%common_desc

%package common
Summary:  Common files for smc-fonts
Group:	User Interface/X
Requires: fontpackages-filesystem

%description common
%common_desc

%package -n %{fontname}-dyuthi-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{fontname}-fonts-dyuthi = %{version}-%{release}
Obsoletes: %{name}-dyuthi < 04.1-4
%description -n %{fontname}-dyuthi-fonts
The Dyuthi font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n dyuthi -f 67-smc-dyuthi.conf Dyuthi*.ttf 

%package -n %{fontname}-meera-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+ with exceptions
Provides: %{fontname}-fonts-meera = %{version}-%{release}
Obsoletes: %{name}-meera < 04.2-1
%description -n %{fontname}-meera-fonts
The Meera font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n meera -f *meera*.conf Meera.ttf


%package -n %{fontname}-rachana-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+
Provides: %{fontname}-fonts-rachana = %{version}-%{release}
Obsoletes: %{name}-rachana < 04.1-4
%description -n %{fontname}-rachana-fonts
The Rachana font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n rachana -f 67-smc-rachana.conf Rachana*.ttf


%package -n %{fontname}-raghumalayalam-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{fontname}-fonts-raghumalayalam = %{version}-%{release}
Obsoletes: %{name}-raghumalayalam < 04.1-4
%description -n %{fontname}-raghumalayalam-fonts
The SMC Malayalam fonts package contains fonts for the display of
new Malayalam Scripts.

%_font_pkg -n raghumalayalam -f 67-smc-raghumalayalam.conf RaghuMalayalamSans*.ttf

%package -n %{fontname}-suruma-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3 with exceptions
Provides: %{fontname}-fonts-suruma = %{version}-%{release}
Obsoletes: %{name}-suruma < 04.1-4
%description -n %{fontname}-suruma-fonts
The Suruma font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n suruma -f 67-smc-suruma.conf suruma*.ttf

%package -n %{fontname}-kalyani-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{fontname}-fonts-kalyani = %{version}-%{release}
Obsoletes: %{name}-kalyani < 04.1-4
%description -n %{fontname}-kalyani-fonts
The Kalyani font package contains fonts for the display of
new Malayalam Scripts.

%_font_pkg -n kalyani -f 67-smc-kalyani.conf Kalyani*.ttf

%package -n %{fontname}-anjalioldlipi-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPL+
Provides: %{fontname}-fonts-anjalioldlipi = %{version}-%{release}
Obsoletes: %{name}-anjalioldlipi < 04.1-4
%description -n %{fontname}-anjalioldlipi-fonts
The Anjali OldLipi package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n anjalioldlipi -f 67-smc-anjalioldlipi.conf AnjaliOldLipi.ttf

#%{_fontdir} is shared by following packages since they all are for malayalam script only

%prep
%setup -q -n malayalam-fonts-04
%patch1 -p1 -b .1-fontconf_priority
%patch2 -p1 -b .2-title-bar-fix
rm Meera*.ttf
cp %{SOURCE8} .
cp %{SOURCE9} .
cp %{SOURCE10} .
%patch3 -p0 -b .2-meera-fonts-fix

%build
./generate.pe Meera.sfd

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf  %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p $RPM_BUILD_DIR/malayalam-fonts-04/malayalam-fonts.conf %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-meera.conf

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/65-0-smc-meera.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-anjalioldlipi.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-dyuthi.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-kalyani.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-rachana.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-raghumalayalam.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-suruma.conf

for fconf in %{fontconf}-meera.conf \
	     67-smc-anjalioldlipi.conf \
	     67-smc-dyuthi.conf \
	     67-smc-kalyani.conf \
	     67-smc-rachana.conf \
	     67-smc-raghumalayalam.conf \
	     67-smc-suruma.conf \
		65-0-smc-meera.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -fr %{buildroot}


%files common
%defattr(-,root,root,-) 
%doc *.txt 
%dir %{_fontdir}

%changelog
* Tue Aug 10 2010 Pravin Satpute <psatpute@redhat.com> 04.2-11
- Resolves: bug 555678
- skipping version 04.2-10 due to make build error

* Mon Jun 28 2010 Pravin Satpute <psatpute@redhat.com> 04.2-9
- Resolves: bug 589906

* Mon Jun 21 2010 Pravin Satpute <psatpute@redhat.com> 04.2-8
- Resolves: bug 563839
- Resolves: bug 590586

* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> 04.2-7
- Resolves: bug 586847
- Resolves: bug 586892

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com> 04.2-6
- Resolves: bug 568709

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com> 04.2-5
- Resolves: bug 568230
- fixed license of suruma and anjali-old-lipi
- done .conf cleanup

* Tue Feb 23 2010 Pravin Satpute <psatpute@redhat.com> 04.2-4
- added .conf file for each subpackage
- fixed source url
- Resolves: bug 567497

* Tue Dec 29 2009 Pravin Satpute <psatpute@redhat.com> 04.2-3
- Resolves: bug 551144

* Wed Oct 14 2009 Pravin Satpute <psatpute@redhat.com> 04.2-2
- bugfix 523454

* Tue Aug 18 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.2-1
- bugfix 484536 for Meera

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 03 2009 Pravin Satpute <psatpute@redhat.com> 04.1-6
- bugfix 493814
- added 'Provides' field for packages

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.1-4
- change descriptions
- fix bug in kalyani font's obsoleting version number
- move _font_pkg macros next to corresponding packages

* Sat Jan 17 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.1-3
- update for new font guidelines

* Tue Jan 06 2009 Pravin Satpute <psatpute@redhat.com> 04.1-2
- bugfix 477458
- updated spec

* Tue Jul 29 2008 Pravin Satpute <psatpute@redhat.com> 04.1-1
- new upstream release
- fontconfig rule for size adjustment of Meera is added
- two new fonts kalyani and anjalioldlipi
- bugfix 448078

* Tue Apr 15 2008 Pravin Satpute <psatpute@redhat.com> 04-6
- corrected meera fonts description it is for traditional script

* Tue Apr 15 2008 Pravin Satpute <psatpute@redhat.com> 04-5
- removed -n {fontname}-fonts from all fields

* Mon Apr 14 2008 Pravin Satpute <psatpute@redhat.com> 04-4
- added comment about sharing directory in spec file
- fontdir will be 'smc' only instead of 'smc-fonts' earlier

* Wed Apr 9 2008 Pravin Satpute <psatpute@redhat.com> 04-3
- defattr now comes after files
- s/malayalam/Malayalam in description
- removed '-fonts' from fontdir variable value

* Fri Apr 4 2008 Pravin Satpute <psatpute@redhat.com> 04-2
- done changes in spec file as suggested in review request
- changed variable name from xfontdir to fontdir
 
* Thu Apr 3 2008 Pravin Satpute <psatpute@redhat.com> 04-1 
- initial packaging
