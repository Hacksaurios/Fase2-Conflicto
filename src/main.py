#!/usr/bin/env python3
from satelitalAnalysis import Analysis

if __name__ == '__main__':
    analysis = Analysis('../images/test.jpg')
    analysis.get_water_volume()
    analysis.show_results()