#!/usr/bin/python

from sys import argv
import xml.etree.ElementTree as ET

tree = ET.parse(argv[1])

for risk in tree.findall('Report/ReportHost/ReportItem/risk_factor'):
  print(risk.text)
