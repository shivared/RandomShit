#!/usr/bin/env python
import sys
import os
import BuildStats as stats
import ExtractMaps as maps
import numpy as np
import pandas as pa
import seaborn as sb
import FailStats as fstat
#This file generates a build report in TEX for the Omni tester
mapFilter = '3400'
#mapFilter = 'csv'
class PLOTCONTACTRES:
    def __init__(self, inFolder = '', outFolder = '' ):
        self.inFolder = inFolder

        self.outFolder = outFolder
        self.dataSrc = fstat.FACTORY()

    def readInputData(self):
        self.dataSrc = fstat.FACTORY(outputDir=self.outFolder)
        self.dataSrc.readInputData(self.inFolder,'csv')


    def generateDUTMaps(self):
        rows = ['A','C','D','E','F','G']
        cols = range(0,72/2)
        for dut in self.dataSrc.dutDict.keys():
            fm = open(os.path.join(self.outFolder,dut+'_resMapMean.csv'),'w')
            fs = open(os.path.join(self.outFolder,dut+'_resMapStd.csv'),'w')
            panel = self.dataSrc.dutDict[dut]
            if len(panel.passRuns) == 0:
                continue
            for c in cols:
                fm.write(','+str(c*2+1))
                fs.write(','+str(c*2+1))
            fm.write('\n')
            fs.write('\n')
            for r in rows:
                fm.write(r)
                fs.write(r)
                for c in cols:
                    vals = []
                    header = r+str(c*2+1) + "-" + r+str(c*2+2)
                    for run in panel.passRuns:
                        vals.append(float(run[header]))
                    fm.write(',' + "%0.2f" % np.mean(vals))
                    fs.write(',' + "%0.2f" % np.std(vals))
                fm.write('\n')
                fs.write('\n')
            fm.close()
            fs.close()

            data = pa.read_csv(os.path.join(self.outFolder, dut + '_resMapMean.csv'), header=0, index_col=0)
            pt = sb.heatmap(data, square=True, vmax=90, vmin=10)
            for item in pt.get_xticklabels():
                item.set_rotation(90)
            fig = pt.get_figure()
            fig.savefig(os.path.join(self.outFolder, dut + '_resMapMean.png'))
            fig.clear()

            data = pa.read_csv(os.path.join(self.outFolder, dut + '_resMapStd.csv'), header=0, index_col=0)
            pt = sb.heatmap(data, square=True, vmax=40, vmin=0, xticklabels=True)
            for item in pt.get_xticklabels():
                item.set_rotation(90)

            fig = pt.get_figure()

            fig.savefig(os.path.join(self.outFolder, dut + '_resMapStd.png'))
            fig.clear()

    def generatePanelMaps(self):
        rows = ['A','C','D','E','F','G']
        cols = range(0,72/2)
        for pan in self.dataSrc.panelDict.keys():
            panel = self.dataSrc.panelDict[pan]
            fm = open(os.path.join(self.outFolder, pan + '_resMapMean.csv'), 'w')
            fs = open(os.path.join(self.outFolder, pan + '_resMapStd.csv'), 'w')
            for c in cols:
                fm.write(',' + str(c * 2 + 1))
                fs.write(',' + str(c * 2 + 1))
            fm.write('\n')
            fs.write('\n')
            for r in rows:
                fm.write(r)
                fs.write(r)
                for c in cols:
                    vals = []
                    header = r + str(c * 2 + 1) + "-" + r + str(c * 2 + 2)
                    for dut in panel.keys():
                        for run in panel[dut].passRuns:
                            vals.append(float(run[header]))
                    fm.write(',' + "%0.2f"%np.mean(vals))
                    fs.write(',' + "%0.2f"%np.std(vals))
                fm.write('\n')
                fs.write('\n')
            fm.close()
            fs.close()

            data = pa.read_csv(os.path.join(self.outFolder, pan + '_resMapMean.csv'), header=0, index_col=0)
            pt = sb.heatmap(data, square=True, vmax=90, vmin=10)
            for item in pt.get_xticklabels():
                item.set_rotation(90)
            fig = pt.get_figure()
            fig.savefig(os.path.join(self.outFolder, pan + '_resMapMean.png'))
            fig.clear()

            data = pa.read_csv(os.path.join(self.outFolder, pan + '_resMapStd.csv'), header=0, index_col=0)
            pt = sb.heatmap(data, square=True, vmax=40, vmin=0, xticklabels=True)
            for item in pt.get_xticklabels():
                item.set_rotation(90)

            fig = pt.get_figure()

            fig.savefig(os.path.join(self.outFolder, pan + '_resMapStd.png'))
            fig.clear()

    def generateLocationMaps(self):
        snSubs = ['G01','D01','G05','D05','G09','D09']

        rows = ['A', 'C', 'D', 'E', 'F', 'G']
        cols = range(0, 72 / 2)
        for sns in snSubs:
            fm = open(os.path.join(self.outFolder, sns + '_resMapMean.csv'), 'w')
            fs = open(os.path.join(self.outFolder, sns + '_resMapStd.csv'), 'w')
            for c in cols:
                header = str(c * 2 + 1) + "-"  + str(c * 2 + 2)
                fm.write(',' + header)
                fs.write(',' + header)
            fm.write('\n')
            fs.write('\n')
            for r in rows:
                fm.write(r)
                fs.write(r)
                for c in cols:
                    vals = []
                    header = r + str(c * 2 + 1) + "-" + r + str(c * 2 + 2)

                    for dut in self.dataSrc.dutDict.keys():
                        if sns not in dut:
                            continue
                        panel = self.dataSrc.dutDict[dut]
                        for run in panel.passRuns:
                            vals.append(float(run[header]))
                    fm.write(',' + "%0.2f" % np.mean(vals))
                    fs.write(',' + "%0.2f" % np.std(vals))
                fm.write('\n')
                fs.write('\n')
            fm.close()
            fs.close()
            data = pa.read_csv(os.path.join(self.outFolder, sns + '_resMapMean.csv'),header=0, index_col=0)
            pt = sb.heatmap(data, square=True,vmax=90, vmin=10)
            for item in pt.get_xticklabels():
                item.set_rotation(90)
            fig = pt.get_figure()
            fig.savefig(os.path.join(self.outFolder, sns + '_resMapMean.png'))
            fig.clear()


            data = pa.read_csv(os.path.join(self.outFolder, sns + '_resMapStd.csv'), header=0, index_col=0)
            pt = sb.heatmap(data, square=True,vmax=40, vmin=0, xticklabels=True)
            for item in pt.get_xticklabels():
                item.set_rotation(90)

            fig = pt.get_figure()

            fig.savefig(os.path.join(self.outFolder, sns + '_resMapStd.png'))
            fig.clear()

if len(sys.argv) > 1:
    rootDir = sys.argv[1]
    outputDir = ''
    if len(sys.argv) > 2:
        outputDir = sys.argv[2]


    report = PLOTCONTACTRES(rootDir, outputDir)
    report.readInputData()
    report.generateDUTMaps()
    report.generatePanelMaps()
    report.generateLocationMaps()

else:
    print 'Usage: PlotResMap.py <log file folder> <tex output folder>\n'
    exit(1)


