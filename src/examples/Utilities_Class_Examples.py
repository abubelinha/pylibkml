#TEST UTILITIES CLASS

import pylibkml
from pylibkml import *
import unittest

class SerializeRawTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_SerializeRaw(self):
        kml = Kml().create_kml()
        retval = Utilities().SerializeRaw(kml)
        self.assertEquals(retval,'<kml/>')
        
class SerializeRawPretty(unittest.TestCase):
    def setUp(self):
        pass

    def test_SerializePretty(self):
        kml = Kml().create_kml()
        retval = Utilities().SerializePretty(kml)
        self.assertEquals(retval,'<kml/>\n')

class AddAltitudeToShape(unittest.TestCase):
    def setUp(self):
        pass
    def test_point(self):
        coordinates = Kml().create_coordinates(10,10,5)
        point = Kml().create_point({'coordinates':coordinates})
        newpoint = Utilities().AddAltitudeToShape(point,10,kmldom.ALTITUDEMODE_RELATIVETOGROUND)
        self.assertEquals(Utilities().SerializeRaw(newpoint),'<Point>'
                            +'<altitudeMode>relativeToGround</altitudeMode>'
                            +'<coordinates>'
                            +'10,10,10\n'
                            +'</coordinates>'
                            +'</Point>')

        
    def test_linearring(self):
        coor = []
        coor.append([0,0,0])
        coor.append([0,1,0])
        coor.append([1,0,0])
        coordinates = Kml().create_coordinates(coor)
        linearring = Kml().create_linearring({'coordinates':coordinates})
        newlinearring = Utilities().AddAltitudeToShape(linearring,10,kmldom.ALTITUDEMODE_RELATIVETOGROUND)
        self.assertEquals(Utilities().SerializeRaw(newlinearring),'<LinearRing>'
                +'<coordinates>'
                +'0,0,10\n'
                +'0,1,10\n'
                +'1,0,10\n'
                +'</coordinates>'
                +'</LinearRing>')

    def test_polygon(self):
        coor = []
        coor.append([0,0,0])
        coor.append([0,1,0])
        coor.append([1,0,0])
        coordinates = Kml().create_coordinates(coor)
        linearring = Kml().create_linearring({'coordinates':coordinates})
        outer = Kml().create_outerboundaryis({'linearring':linearring})
        polygon = Kml().create_polygon({'outerboundaryis':outer})
        newpolygon = Utilities().AddAltitudeToShape(polygon,10,kmldom.ALTITUDEMODE_RELATIVETOGROUND)
        self.assertEquals(Utilities().SerializeRaw(newpolygon),'<Polygon>'
                    +'<outerBoundaryIs>'
                    +'<LinearRing>'
                    +'<coordinates>'
                    +'0,0,10\n'
                    +'0,1,10\n'
                    +'1,0,10\n'
                    +'</coordinates>'
                    +'</LinearRing>'
                    +'</outerBoundaryIs>'
                    +'</Polygon>')

    def test_multiplegeometry(self):
        coor = []
        polygon = []
        coor.append([0,0,0])
        coor.append([0,1,0])
        coor.append([1,0,0])
        coordinates = Kml().create_coordinates(coor)
        linearring = Kml().create_linearring({'coordinates':coordinates})
        outer = Kml().create_outerboundaryis({'linearring':linearring})
        polygon.append(Kml().create_polygon({'outerboundaryis':outer}))
        coor = []
        coor.append([0,0,0])
        coor.append([0,2,0])
        coor.append([2,0,0])
        coordinates = Kml().create_coordinates(coor)
        linearring = Kml().create_linearring({'coordinates':coordinates})
        outer = Kml().create_outerboundaryis({'linearring':linearring})
        polygon.append(Kml().create_polygon({'outerboundaryis':outer}))
        multigeometry = Kml().create_multigeometry({'polygon':polygon})
        newmultigeometry = Utilities().AddAltitudeToShape(multigeometry,10,kmldom.ALTITUDEMODE_ABSOLUTE)
        self.assertEquals(Utilities().SerializeRaw(newmultigeometry),'<MultiGeometry>'
                +'<Polygon>'
                +'<outerBoundaryIs>'
                +'<LinearRing>'
                +'<coordinates>'
                +'0,0,10\n'
                +'0,1,10\n'
                +'1,0,10\n'
                +'</coordinates>'
                +'</LinearRing>'
                +'</outerBoundaryIs>'
                +'</Polygon>'
                +'<Polygon>'
                +'<outerBoundaryIs>'
                +'<LinearRing>'
                +'<coordinates>'
                +'0,0,10\n'
                +'0,2,10\n'
                +'2,0,10\n'
                +'</coordinates>'
                +'</LinearRing>'
                +'</outerBoundaryIs>'
                +'</Polygon>'
                +'</MultiGeometry>')

class RawKMLToLibKMLObjectTest(unittest.TestCase):

    def setUp(self):
        pass
    def test_RawKMLToLibKMLObjectTest(self):
        kmlstring = '<MultiGeometry><Polygon><outerBoundaryIs><LinearRing><coordinates>0,0,10\n0,1,10\n1,0,10</coordinates></LinearRing></outerBoundaryIs></Polygon><Polygon><outerBoundaryIs><LinearRing><coordinates>0,0,10\n0,2,10\n2,0,10</coordinates></LinearRing></outerBoundaryIs></Polygon></MultiGeometry>'
        self.assertEquals(Utilities().SerializeRaw(Utilities().RawKMLToLibKMLObject(kmlstring)),'<MultiGeometry>'
                +'<Polygon>'
                +'<outerBoundaryIs>'
                +'<LinearRing>'
                +'<coordinates>'
                +'0,0,10\n'
                +'0,1,10\n'
                +'1,0,10\n'
                +'</coordinates>'
                +'</LinearRing>'
                +'</outerBoundaryIs>'
                +'</Polygon>'
                +'<Polygon>'
                +'<outerBoundaryIs>'
                +'<LinearRing>'
                +'<coordinates>'
                +'0,0,10\n'
                +'0,2,10\n'
                +'2,0,10\n'
                +'</coordinates>'
                +'</LinearRing>'
                +'</outerBoundaryIs>'
                +'</Polygon>'
                +'</MultiGeometry>')

class CreateKMZTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_create_kmz(self):
        ziplist = []
        ziplist.append('sample.jpg')
        ziplist.append('sample2.jpg')
        Utilities().create_kmz('sample.kml','output.kmz',ziplist)
    
class TestProcessHTML(unittest.TestCase):

    def setUp(self):
        pass
    def test_processhtml(self):
        retVal = Utilities().process_html('test.html')

        self.assertEqual(retVal,'<![CDATA['
            +'<html>\n'
            +'<head>\n'
            +'<title>\n'
            +'Cinematics\n'
            +'</title>\n'
            +'</head>\n'
            +'\n'
            +'<body>\n'
            +'<div class="header">Cinematics</div>\n'
            +'\n'
            +'<table align="center">\n'
            +'<tr valign="top">\n'
            +'<td style="width: 50%;">\n'
            +'<div id="map_div" style="width: 400px; height: 300;"></div>\n'
            +'</td>\n'
            +'<td style="width: 50%;">\n'
            +'<div id="table_div"></div>\n'
            +'</td>\n'
            +'</tr>\n'
            +'<tr>\n'
            +'<td colSpan=2>\n'
            +'<div id="chart_div" style="align: center; width: 700px; height: 300px;"></div>\n'
            +'</td>\n'
            +'</tr>\n'
            +'</table>\n'
            +'\n'
            +'</body>\n'
            +'</html>\n]]>')

if __name__ == '__main__':
    unittest.main()
