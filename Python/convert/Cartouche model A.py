#coef magique 3,9951573849878934624697336561743 (diviser longueur pour avoir position)
p = arcpy.mp.ArcGISProject('CURRENT')
#Create a layout
lyt = p.createLayout(841, 1189, 'MILLIMETER', 'Portait_A0_case')
#Construct a pre-defined rectangle graphic element using a system style item
# and a rectangle function that takes x/y min/max and a width/height
# using the lower left corner as a start location

polyStyle = p.listStyleItems('ArcGIS 2D', 'Polygon','Black Outline (2 pts)')[0]

reca = p.createPredefinedGraphicElement(lyt, arcpy.Point(0, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle logo',
                                       lock_aspect_ratio=False)
reca.elementWidth = 232
reca.elementHeight = 155

path = r'C:\Users\noeng\Documents\ArcGIS\Projects\MyProject\LOGO.png'
pic1 = p.createPictureElement(lyt, arcpy.Point(1, 1188), path, 'LOGO')

reco = p.createPredefinedGraphicElement(lyt, arcpy.Point(58, 282.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle Titre',
                                       lock_aspect_ratio=False)
reco.elementWidth = 450.5
reco.elementHeight = 59

recr = p.createPredefinedGraphicElement(lyt, arcpy.Point(58, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle-1',
                                       lock_aspect_ratio=False)
recr.elementWidth = 75
recr.elementHeight = 50

rec = p.createPredefinedGraphicElement(lyt, arcpy.Point(76.77, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle',
                                       lock_aspect_ratio=False)
rec.elementWidth = 75
rec.elementHeight = 50

rec1 = p.createPredefinedGraphicElement(lyt, arcpy.Point(95.54, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle1',
                                       lock_aspect_ratio=False)
rec1.elementWidth = 75
rec1.elementHeight = 50

rec2 = p.createPredefinedGraphicElement(lyt, arcpy.Point(114.31, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle2',
                                       lock_aspect_ratio=False)
rec2.elementWidth = 75
rec2.elementHeight = 50

rec3 = p.createPredefinedGraphicElement(lyt, arcpy.Point(133.08, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle3',
                                       lock_aspect_ratio=False)
rec3.elementWidth = 75
rec3.elementHeight = 50

rec4 = p.createPredefinedGraphicElement(lyt, arcpy.Point(151.85, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle4',
                                       lock_aspect_ratio=False)
rec4.elementWidth = 75
rec4.elementHeight = 50

recarrow = p.createPredefinedGraphicElement(lyt, arcpy.Point(170.67, 258.5), 'RECTANGLE',
                                       polyStyle, 'Rectangle Arrow',
                                       lock_aspect_ratio=False)
recarrow.elementWidth = 159
recarrow.elementHeight = 155


lyt.openView()