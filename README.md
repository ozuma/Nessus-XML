# Introduction

Here is some sample scripts to parse Nessus XML file(e.g. foo_bar.nessus).

This script handle Nessus XML "v2"(`<NessusClientData_v2>`). Nessus 6 and Nessus 7 use this format.

# Sample

I put some Sample XML(.nessus) files in `/sample_xml` directory.

## View CSV format

Print CSV format as below:
```
ipaddr,risk_factor(Critical/High/Medium/Low/None),port/protocol,pluginID,"pluginName"
```

Use node: 
* `Report -> ReportHost -> HostProperties` (Get IP address of targets)
* `Report -> ReportHost -> ReportItem`
* `Report -> ReportHost -> ReportItem -> risk_factor`

On Web console, you see "Info" field(blue bar). But in XML output, it's displayed as "None".
```
$ ./risk_factor.py sample_xml/wint4_0.nessus 
192.168.2.40,Critical,139/tcp,34477,"MS08-067: Microsoft Windows Server Service Crafted RPC Request Handling Remote Code Execution (958644) (ECLIPSEDWING) (uncredentialed check)"
192.168.2.40,None,139/tcp,106716,"Microsoft Windows SMB2 Dialects Supported (remote check)"
192.168.2.40,None,139/tcp,96982,"Server Message Block (SMB) Protocol Version 1 Enabled (uncredentialed check)"
192.168.2.40,None,139/tcp,100871,"Microsoft Windows SMB Versions Supported (remote check)"
192.168.2.40,None,139/tcp,17651,"Microsoft Windows SMB : Obtains the Password Policy"
192.168.2.40,None,139/tcp,10902,"Microsoft Windows 'Administrators' Group User List"
192.168.2.40,Medium,139/tcp,56211,"SMB Use Host SID to Enumerate Local Users Without Credentials"
192.168.2.40,Medium,139/tcp,56210,"Microsoft Windows SMB LsaQueryInformationPolicy Function SID Enumeration Without Credentials"
192.168.2.40,None,139/tcp,10860,"SMB Use Host SID to Enumerate Local Users"
192.168.2.40,None,139/tcp,10859,"Microsoft Windows SMB LsaQueryInformationPolicy Function SID Enumeration"
192.168.2.40,Critical,139/tcp,35362,"MS09-001: Microsoft Windows SMB Vulnerabilities Remote Code Execution (958687) (uncredentialed check)"
192.168.2.40,None,139/tcp,26917,"Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry"
192.168.2.40,Medium,139/tcp,26920,"Microsoft Windows SMB NULL Session Authentication"
192.168.2.40,None,139/tcp,10395,"Microsoft Windows SMB Shares Enumeration"
192.168.2.40,High,139/tcp,22034,"MS06-035: Vulnerability in Server Service Could Allow Remote Code Execution (917159) (uncredentialed check)"
192.168.2.40,None,139/tcp,11219,"Nessus SYN scanner"
192.168.2.40,None,135/tcp,11219,"Nessus SYN scanner"
192.168.2.40,None,0/udp,10287,"Traceroute Information"
192.168.2.40,None,0/tcp,19506,"Nessus Scan Information"
192.168.2.40,Critical,0/tcp,19699,"Microsoft Windows NT 4.0 Unsupported Installation Detection"
....
```

### count risks by Severity

Here is an sample code. In case of exporting output XML to single `.nessus` file with many hosts, to summarize risks by it's severity level:

1. Save risk_factor.py output(CSV) as "nessus_result.csv".
2. Following awk command line:
```
$ awk 'BEGIN{FS=",";OFS=","} /^Critical,/ {count[$4]++} END{for(i in count)print count[i], i}' nessus_result.csv > crit.csv
$ awk 'BEGIN{FS=",";OFS=","} /^High,/ {count[$4]++} END{for(i in count)print count[i], i}' nessus_result.csv > high.csv
$ awk 'BEGIN{FS=",";OFS=","} /^Medium,/ {count[$4]++} END{for(i in count)print count[i], i}' nessus_result.csv > medium.csv
$ awk 'BEGIN{FS=",";OFS=","} /^Low,/ {count[$4]++} END{for(i in count)print count[i], i}' nessus_result.csv > low.csv
```

Output example(Medium):
```
$ cat medium.csv 
8,"Microsoft Windows Remote Desktop Protocol Server Man-in-the-Middle Weakness"
94,"SSL Certificate Cannot Be Trusted"
3,"SMB Use Host SID to Enumerate Local Users Without Credentials"
3,"Microsoft Windows SMB LsaQueryInformationPolicy Function SID Enumeration Without Credentials"
48,"SSL Medium Strength Cipher Suites Supported"
9,"Terminal Services Encryption Level is Medium or Low"
11,"SSL Certificate Signed Using Weak Hashing Algorithm"
5,"Microsoft Windows SMB NULL Session Authentication"
132,"SSL Self-Signed Certificate"
```

