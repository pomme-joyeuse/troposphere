p = arcpy.mp.ArcGISProject('CURRENT')
#Create a layout
lyt = p.createLayout(841, 1189, 'MILLIMETER', 'Portait_A0_case_B')
#Construct a pre-defined rectangle graphic element using a system style item
# and a rectangle function that takes x/y min/max and a width/height
# using the lower left corner as a start location

polyStyle = p.listStyleItems('ArcGIS 2D', 'Polygon','Black Outline (2 pts)')[0]

reca = p.createPredefinedGraphicElement(lyt, arcpy.Point(0, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle logo',
                                       lock_aspect_ratio=False)
reca.elementWidth = 232
reca.elementHeight = 154.67

path = r'C:\Users\noeng\Documents\ArcGIS\Projects\MyProject\LOGO.png'
pic1 = p.createPictureElement(lyt, arcpy.Point(1, 1188), path, 'LOGO')

reco = p.createPredefinedGraphicElement(lyt, arcpy.Point(58, 284.66), 'RECTANGLE',
                                       polyStyle, 'Rectangle O',
                                       lock_aspect_ratio=False)
reco.elementWidth = 608.6
reco.elementHeight = 50

recr = p.createPredefinedGraphicElement(lyt, arcpy.Point(58, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle-1',
                                       lock_aspect_ratio=False)
recr.elementWidth = 75
recr.elementHeight = 50

rec = p.createPredefinedGraphicElement(lyt, arcpy.Point(76.77, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle',
                                       lock_aspect_ratio=False)
rec.elementWidth = 75
rec.elementHeight = 50

rec1 = p.createPredefinedGraphicElement(lyt, arcpy.Point(95.54, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle1',
                                       lock_aspect_ratio=False)
rec1.elementWidth = 75
rec1.elementHeight = 50

rec2 = p.createPredefinedGraphicElement(lyt, arcpy.Point(114.31, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle2',
                                       lock_aspect_ratio=False)
rec2.elementWidth = 75
rec2.elementHeight = 50

rec3 = p.createPredefinedGraphicElement(lyt, arcpy.Point(133.08, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle3',
                                       lock_aspect_ratio=False)
rec3.elementWidth = 75
rec3.elementHeight = 50

rec4 = p.createPredefinedGraphicElement(lyt, arcpy.Point(151.85, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle4',
                                       lock_aspect_ratio=False)
rec4.elementWidth = 75
rec4.elementHeight = 50

rec5 = p.createPredefinedGraphicElement(lyt, arcpy.Point(170.62, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle3',
                                       lock_aspect_ratio=False)
rec5.elementWidth = 80
rec5.elementHeight = 50

rec6 = p.createPredefinedGraphicElement(lyt, arcpy.Point(190.64, 272.15), 'RECTANGLE',
                                       polyStyle, 'Rectangle4',
                                       lock_aspect_ratio=False)
rec6.elementWidth = 78
rec6.elementHeight = 50

recs = p.createPredefinedGraphicElement(lyt, arcpy.Point(58, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_1',
                                       lock_aspect_ratio=False)
recs.elementWidth = 75
recs.elementHeight = 54.5

recs1 = p.createPredefinedGraphicElement(lyt, arcpy.Point(76.77, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_2',
                                       lock_aspect_ratio=False)
recs1.elementWidth = 75
recs1.elementHeight = 54.5

recs2 = p.createPredefinedGraphicElement(lyt, arcpy.Point(95.54, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_3',
                                       lock_aspect_ratio=False)
recs2.elementWidth = 75
recs2.elementHeight = 54.5

recs3 = p.createPredefinedGraphicElement(lyt, arcpy.Point(114.31, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_4',
                                       lock_aspect_ratio=False)
recs3.elementWidth = 75
recs3.elementHeight = 54.5

recs4 = p.createPredefinedGraphicElement(lyt, arcpy.Point(133.08, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_5',
                                       lock_aspect_ratio=False)
recs4.elementWidth = 75
recs4.elementHeight = 54.5

recs5 = p.createPredefinedGraphicElement(lyt, arcpy.Point(151.85, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_6',
                                       lock_aspect_ratio=False)
recs5.elementWidth = 75
recs5.elementHeight = 54.5

recs6 = p.createPredefinedGraphicElement(lyt, arcpy.Point(170.62, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_7',
                                       lock_aspect_ratio=False)
recs6.elementWidth = 80
recs6.elementHeight = 54.5

recs7 = p.createPredefinedGraphicElement(lyt, arcpy.Point(190.64, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle_8',
                                       lock_aspect_ratio=False)
recs7.elementWidth = 78
recs7.elementHeight = 54.5

lyt.openView()