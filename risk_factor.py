#!/usr/bin/python

from sys import argv
import xml.etree.ElementTree as ET

tree = ET.parse(argv[1])

# XML structure:
# 
# <NessusClientData_v2>
# <Report name="Win NT 4.0" xmlns:cm="http://www.nessus.org/cm">
# <ReportHost name="192.168.2.40">
# ......
# <ReportItem port="139" svc_name="smb" protocol="tcp" severity="4" pluginID="34477" pluginName="MS08-067: Microsoft Windows Server Service Crafted RPC Request Handling Remote Code Execution (958644) (ECLIPSEDWING) (uncredentialed check)" pluginFamily="Windows">
# ......
# <plugin_name>MS08-067: Microsoft Windows Server Service Crafted RPC Request Handling Remote Code Execution (958644) (ECLIPSEDWING) (uncredentialed check)</plugin_name>
# <plugin_publication_date>2008/10/23</plugin_publication_date>
# <plugin_type>local</plugin_type>
# <risk_factor>Critical</risk_factor>
# ......
# <xref>CWE:94</xref>
# </ReportItem>
# <ReportItem port="139" svc_name="smb" protocol="tcp" severity="0" pluginID="106716" pluginName="Microsoft Windows SMB2 Dialects Supported (remote check)" pluginFamily="Windows">
# ......
# </ReportHost>
# </Report>
# </NessusClientData_v2>

for item in tree.findall('Report/ReportHost/ReportItem'):
  risk_factor = item.find('risk_factor').text
  pluginID = item.get('pluginID')
  pluginName = item.get('pluginName')
  port = item.get('port')
  protocol = item.get('protocol')

  print(
    risk_factor + ',' + \
    port + '/' + protocol + ',' + \
    pluginID + ',' + \
    '"' + pluginName + '"'
  )

