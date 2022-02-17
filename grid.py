# coding:utf-8
import rhinoscriptsyntax as rs

# add point
#point = [600,300,0]
#print(point)1
#print("テスト")
#rs.AddPoint(point)

# add line
#start = [0,0,0]
#end = [300,300,0]
#rs.AddLine(start, end)

# add text
#text = "X0"
#point = [0,0,0]
#height = 20
#font="Arial"
#font_style = 0
#justification = 1 + 262144
#rs.AddText(text, point, height, font, font_style, justification)

# point array
print("start")
xNum = 3
xPitch = 150
for i in range (xNum):
    print(i)
    # point
    pt = [xPitch*i,0,0]
    rs.AddPoint(pt)
    # text
    text = "X{}".format(i)
    #text = "X" + str(i)
    #text = "X%s" % (i)
    point = [xPitch*i,-20,0]
    height = 20
    font="Arial"
    font_style = 0
    justification = 2 + 262144
    rs.AddText(text, point, height, font, font_style, justification)

print("end")    

#print(range(4))

#a = [0,1,2,3]
#print(a)
#b = range(4)
#print(b)