# Introduction

How to parse Nessus XML file(foo_bar.nessus).

This script handle Nessus XML "v2"(`<NessusClientData_v2>`). Nessus 6 and Nessus 7 use this format.

# Sample

To get XML(.nessus) files, get `sample_xml` directory. Result of my various scans are located.

## Risk all lists

Print CSV format as below:
```
risk_factor(Critical/High/Medium/Low/None),port/protocol,pluginID,"pluginName"
```

Use node: 
* `Report -> ReportHost -> ReportItem`
* `Report -> ReportHost -> ReportItem -> risk_factor`

On Web console, you see "Info" field(blue bar). But in XML output, it's displayed as "None".
```
$ ./risk_factor.py sample_xml/wint4_0.nessus 
Critical,139/tcp,34477,MS08-067: Microsoft Windows Server Service Crafted RPC Request Handling Remote Code Execution (958644) (ECLIPSEDWING) (uncredentialed check)
None,139/tcp,106716,Microsoft Windows SMB2 Dialects Supported (remote check)
None,139/tcp,96982,Server Message Block (SMB) Protocol Version 1 Enabled (uncredentialed check)
None,139/tcp,100871,Microsoft Windows SMB Versions Supported (remote check)
None,139/tcp,17651,Microsoft Windows SMB : Obtains the Password Policy
None,139/tcp,10902,Microsoft Windows 'Administrators' Group User List
Medium,139/tcp,56211,SMB Use Host SID to Enumerate Local Users Without Credentials
Medium,139/tcp,56210,Microsoft Windows SMB LsaQueryInformationPolicy Function SID Enumeration Without Credentials
None,139/tcp,10860,SMB Use Host SID to Enumerate Local Users
None,139/tcp,10859,Microsoft Windows SMB LsaQueryInformationPolicy Function SID Enumeration
Critical,139/tcp,35362,MS09-001: Microsoft Windows SMB Vulnerabilities Remote Code Execution (958687) (uncredentialed check)
None,139/tcp,26917,Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry
Medium,139/tcp,26920,Microsoft Windows SMB NULL Session Authentication
None,139/tcp,10395,Microsoft Windows SMB Shares Enumeration
High,139/tcp,22034,MS06-035: Vulnerability in Server Service Could Allow Remote Code Execution (917159) (uncredentialed check)
None,139/tcp,11219,Nessus SYN scanner
None,139/tcp,10394,Microsoft Windows SMB Log In Possible
None,139/tcp,10785,Microsoft Windows SMB NativeLanManager Remote System Information Disclosure
None,139/tcp,11011,Microsoft Windows SMB Service Detection
None,137/udp,10150,Windows NetBIOS / SMB Remote Host Information Disclosure
None,135/tcp,11219,Nessus SYN scanner
None,0/udp,10287,Traceroute Information
None,0/tcp,19506,Nessus Scan Information
Critical,0/tcp,19699,Microsoft Windows NT 4.0 Unsupported Installation Detection
None,0/tcp,45590,Common Platform Enumeration (CPE)
None,0/tcp,54615,Device Type
None,0/tcp,11936,OS Identification
None,0/tcp,35716,Ethernet Card Manufacturer Detection
None,0/tcp,20094,VMware Virtual Machine Detection
None,0/tcp,10916,Microsoft Windows - Local Users Information : Passwords Never Expire
None,0/tcp,10914,Microsoft Windows - Local Users Information : Never Changed Passwords
None,0/tcp,10913,Microsoft Windows - Local Users Information : Disabled Accounts
None,0/tcp,10915,Microsoft Windows - Local Users Information : User Has Never Logged In
None,0/tcp,24786,Nessus Windows Scan Not Performed with Admin Privileges
```
