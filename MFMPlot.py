# Analysis of MFM.txt File by Gabriel Natale
var = raw_input("Enter File Name:")
print "File Name:", var
f = open(var, "r")
num_lines = 0
Volume = 0
import math
from ROOT import *
from array import array
canvas = TCanvas('canvas','canvas',800, 400)
g = TGraph()
l = TLegend(0.6,0.6,1.0,1.0)
aux = 0
for line in f:
    num_lines += 1
    a = num_lines
    b = 3
    c = math.fmod(a,b)
    if c == 2:
        aux = line
        rate = float(line) + .71
        average = (rate  + float(aux)) / 2.
        Volume += average * 0.0833333
        svolume = str(Volume)
        TotalV = "Total Volume: " + svolume[0:4] + "sl"
        line1 = float(line)
        
        g.SetPoint(num_lines-1, num_lines,line1)
x = 5.842
Mass = float(svolume) * x
TM = str(Mass)
TotalM = "Total Mass:" + " " + TM[0:4] + "g"
m = TText(68,30,str(TotalM))
t = TText(68,36,str(TotalV))        
h = TH2D('h','h',200,0, 100, 50, -2, 40)
g.SetMarkerStyle(20)
l.SetTextSize(0.04)
l.AddEntry(g,"Rate of Flow","p")
h.GetXaxis().SetTitle("Time (min)")
h.GetYaxis().SetTitle("Rate of Flow(slpm)")
h.Draw() 
g.Draw("p")
l.Draw()
t.Draw()
m.Draw()
varp = str(var)[0:15] 
V1 = varp + ".png"
canvas.SaveAs(V1)

                  
