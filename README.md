# Introduction

How to parse Nessus XML file.

This script handle Nessus XML "v2"(`<NessusClientData_v2>`). Nessus 6 and Nessus 7 use this format.

# Sample

Use sample_xml/wint4_0.nessus.

## Only select risk_factor(Critical/High/Medium/Low/None)

Use node `Report -> ReportHost -> ReportItem -> risk_factor`.

On Web console, you see "Info" field(blue bar). But in XML output, it's displayed as "None".
```
$ ./risk_factor.py sample_xml/wint4_0.nessus
Critical
None
None
None
None
None
Medium
Medium
None
None
Critical
None
Medium
None
High
None
None
None
None
None
None
None
None
Critical
None
None
None
None
None
None
None
None
None
None
```
