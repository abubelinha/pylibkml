# python tests.py
# python tests.py TestDocumentObject
# python tests.py TestDocumentObject.test_create_document

import sys
import unittest
from pylibkml import *


class TestAlias(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_create_alias(self):
        alias = Kml().create_alias()
        self.assertEqual(str(alias.__class__), "<class 'kmldom.Alias'>")
        self.assertEqual(Utilities().SerializeRaw(alias), '<Alias/>')

    def test_create_alias_with_attributes(self):
        alias = Kml().create_alias({'targethref':'test.html',
                                    'sourcehref':'test.html'})
                                    
        self.assertEqual(Utilities().SerializeRaw(alias),'<Alias>'
        +'<targetHref>test.html</targetHref>'
        +'<sourceHref>test.html</sourceHref>'
        +'</Alias>')

class TestAtomAuthor(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_create_atomauthor(self):
        atomauthor = Kml().create_atomauthor()
        
        self.assertEqual(str(atomauthor.__class__), "<class 'kmldom.AtomAuthor'>")
        self.assertEqual(Utilities().SerializeRaw(atomauthor), '<atom:author/>')

    def test_create_atomauthor_with_attributes(self):
        atomauthor = Kml().create_atomauthor({'uri':'www.google.com',
                                            'email':'blizzardhusky@mtu.edu',
                                            'name':'Blizzard'})
                                    
        self.assertEqual(Utilities().SerializeRaw(atomauthor),'<atom:author>'
        +'<atom:name>Blizzard</atom:name>'
        +'<atom:uri>www.google.com</atom:uri>'
        +'<atom:email>blizzardhusky@mtu.edu</atom:email>'
        +'</atom:author>')
        
class TestAtomLink(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_create_atomlink(self):
        atomlink = Kml().create_atomlink()
        
        self.assertEqual(str(atomlink.__class__), "<class 'kmldom.AtomLink'>")
        self.assertEqual(Utilities().SerializeRaw(atomlink), '<atom:link/>')

    def test_create_atomauthor_with_attributes(self):
        atomlink = Kml().create_atomlink({'href':'www.google.com'})
                                    
        self.assertEqual(Utilities().SerializeRaw(atomlink),'<atom:link href="www.google.com"/>')

class TestBalloonStyle(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_balloonstyle(self):
        balloonstyle = Kml().create_balloonstyle()
        self.assertEqual(str(balloonstyle.__class__), "<class 'kmldom.BalloonStyle'>")
        self.assertEqual(Utilities().SerializeRaw(balloonstyle), '<BalloonStyle/>')

    def test_create_balloonstyle_with_attributes(self):        
        balloonstyle = Kml().create_balloonstyle({'id' : 'SampleID',
                                                'bgcolor' : 'ff0000ff',
                                                'textcolor' : 'ffff00ff',
                                                'text' : "Sample Text",
                                                'displaymode' : 'default',
                                                })
        self.assertEqual(Utilities().SerializeRaw(balloonstyle),
            '<BalloonStyle id="SampleID">'
            +'<bgColor>ff0000ff</bgColor>'
            +'<textColor>ffff00ff</textColor>'
            +'<text>Sample Text</text>'
            +'<displayMode>default</displayMode>'
            +'</BalloonStyle>'
            )


class TestCameraObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_camera(self):
        camera = Kml().create_camera()
        self.assertEqual(str(camera.__class__), "<class 'kmldom.Camera'>")
        self.assertEqual(Utilities().SerializeRaw(camera), '<Camera/>')

    def test_create_camera_with_attributes(self):
        camera = Kml().create_camera({'id' : 'SampleID',
                                    'longitude':0,
                                    'latitude':0,
                                    'altitude':0,
                                    'heading':0,
                                    'tilt':0,
                                    'roll':0,
                                    'altitudemode': 'clamptoground',
                                    'gxtimestamp' : Kml().create_gxtimestamp({'id':'SampleID'}),
                                    })
        self.assertEqual(Utilities().SerializeRaw(camera),
            '<Camera id="SampleID">'
            +'<gx:TimeStamp id="SampleID"/>'
            +'<longitude>0</longitude>'
            +'<latitude>0</latitude>'
            +'<altitude>0</altitude>'
            +'<heading>0</heading>'
            +'<tilt>0</tilt>'
            +'<roll>0</roll>'
            +'<altitudeMode>clampToGround</altitudeMode>'
            +'</Camera>'
            )

class TestChangeObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_change(self):
        change = Kml().create_change()
        self.assertEqual(str(change.__class__), "<class 'kmldom.Change'>")
        self.assertEqual(Utilities().SerializeRaw(change), '<Change/>')
        
    def test_create_change_with_attributes(self):
        coordinates = Kml().create_coordinates(-120,40)
        point = Kml().create_point({'coordinates':coordinates})
        change = Kml().create_change({'point':point})
        self.assertEqual(Utilities().SerializeRaw(change),'<Change>'
            +'<Point><coordinates>-120,40,0\n</coordinates></Point>'
            +'</Change>')

class TestCoordinatesObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_coordinates(self):
        coordinates = Kml().create_coordinates(-120,40)

        self.assertEqual(str(coordinates.__class__),
                        "<class 'kmldom.Coordinates'>")
        self.assertEqual(Utilities().SerializeRaw(coordinates), 
                        '<coordinates>-120,40,0\n</coordinates>')

    def test_create_coordinates_with_altitude(self):
        coordinates = Kml().create_coordinates(-120,40,123)

        self.assertEqual(str(coordinates.__class__),
                        "<class 'kmldom.Coordinates'>")
        self.assertEqual(Utilities().SerializeRaw(coordinates), 
                        '<coordinates>-120,40,123\n</coordinates>')

class TestCreateObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_create(self):
        create = Kml().create_create()

        self.assertEqual(str(create.__class__), "<class 'kmldom.Create'>")
        self.assertEqual(Utilities().SerializeRaw(create), '<Create/>')
        
    def test_create_create_with_attributes(self):
        doc = []
        doc.append(Kml().create_document())
        doc.append(Kml().create_document())
        create = Kml().create_create({'document':doc})
        
        self.assertEqual(Utilities().SerializeRaw(create),'<Create>'
            +'<Document/>'
            +'<Document/>'
            +'</Create>')

class TestDataObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_data(self):
        data = Kml().create_data()

        self.assertEqual(str(data.__class__), "<class 'kmldom.Data'>")
        self.assertEqual(Utilities().SerializeRaw(data), '<Data/>')
        
    def test_create_data_with_attributes(self):
        data = Kml().create_data({'name':'Name',
                                    'displayname' : 'Display Name',
                                    'value' : '1'})
        self.assertEqual(Utilities().SerializeRaw(data),'<Data name="Name">'
            +'<displayName>Display Name</displayName>'
            +'<value>1</value>'
            +'</Data>')
            
class TestDeleteObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_delete(self):
        delete = Kml().create_delete()

        self.assertEqual(str(delete.__class__), "<class 'kmldom.Delete'>")
        self.assertEqual(Utilities().SerializeRaw(delete), '<Delete/>')
        
    def test_create_data_with_attributes(self):
        doc = []
        doc.append(Kml().create_document())
        doc.append(Kml().create_document())
        delete = Kml().create_delete({'document':doc})
        
        self.assertEqual(Utilities().SerializeRaw(delete),'<Delete>'
            +'<Document/>'
            +'<Document/>'
            +'</Delete>')

class TestDocumentObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_document(self):
        document = Kml().create_document()

        self.assertEqual(str(document.__class__), "<class 'kmldom.Document'>")
        self.assertEqual(Utilities().SerializeRaw(document), '<Document/>')

    def test_create_document_with_attributes(self):
        document = Kml().create_document({'id' : 'SampleID',
                            'name' : 'SampleName',
                            'visibility' : 1,
                            'open' : 1,
#                            'atomauthor':Kml().create_atomauthor(),
#                            'atomlink':Kml().create_atomlink(),
                            'address':'1060 West Addison',
                            #  <xal:AddressDetails>...</xal:AddressDetails>  <!-- xmlns:xal -->
                            'phonenumber':'867-5309',
                            'snippet': Kml().create_snippet({'maxlines':10,'text':'Sample Text'}),
                            'description' : 'Sample Document',
                            'camera':Kml().create_camera(),
                            'timestamp' : {'when': '2009-05-19'},
                            'styleurl':'#mainstyle',
                            'style':[Kml().create_style(),Kml().create_style()],
                            'stylemap':[Kml().create_stylemap(),Kml().create_stylemap()],
                            'region':Kml().create_region(),
                            'extendeddata':Kml().create_extendeddata({'data':Kml().create_data()}),
                            'schema':[Kml().create_schema(),Kml().create_schema()],
                            'placemark' : Kml().create_placemark({'id':'placemark',}),
                            'networklink' : Kml().create_networklink({'id' : 'networklink',}),
                        })
        self.assertEqual(Utilities().SerializeRaw(document),
                '<Document id="SampleID">'
                + '<name>SampleName</name>'
                + '<visibility>1</visibility>'
                + '<open>1</open>'
#                + '<atom:author/>'
#                + '<atom:link/>'
                + '<address>1060 West Addison</address>'
#                + '<phoneNumber>867-5309</phoneNumber>'
                + '<Snippet maxLines="10">Sample Text</Snippet>'
                + '<description>Sample Document</description>'
                + '<Camera/>'
                + '<TimeStamp><when>2009-05-19</when></TimeStamp>'
                + '<styleUrl>#mainstyle</styleUrl>'
                + '<Style/><Style/>'
                + '<StyleMap/><StyleMap/>'
                + '<Region/>'
                + '<ExtendedData><Data/></ExtendedData>'
                + '<Schema/><Schema/>'
                + '<NetworkLink id="networklink"/>'
                + '<Placemark id="placemark"/>'
                + '</Document>')

    def test_create_document_with_timespan(self):

        document = Kml().create_document({'timespan' : {'begin' : '2005',
                                                        'end'   : '2006'},
                                           })
        self.assertEqual(Utilities().SerializeRaw(document),
                '<Document>'
                + '<TimeSpan>'
                + '<begin>2005</begin>'
                + '<end>2006</end>'
                + '</TimeSpan>'
                + '</Document>')

class TestExtendedDataObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_extendeddata(self):
        extendeddata = Kml().create_extendeddata()

        self.assertEqual(str(extendeddata.__class__), "<class 'kmldom.ExtendedData'>")
        self.assertEqual(Utilities().SerializeRaw(extendeddata), '<ExtendedData/>')

    def test_create_extendeddata_with_data(self):
        
        data = [ Kml().create_data({'name': 'color', 'value': 'red'}),
                Kml().create_data({'name': 'height', 'value': 123}), ]
        extendeddata = Kml().create_extendeddata({'data':data,
                                                    'schemadata':[Kml().create_schemadata(),Kml().create_schemadata()]})

        self.assertEqual(Utilities().SerializeRaw(extendeddata),
                '<ExtendedData>'
                    + '<Data name="color">'
                        + '<value>red</value>'
                    + '</Data>'
                    + '<Data name="height">'
                        + '<value>123</value>'
                    + '</Data>'
                    + '<SchemaData/><SchemaData/>'
                + '</ExtendedData>')


class TestFolderObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_folder(self):
        folder = Kml().create_folder()

        self.assertEqual(str(folder.__class__), "<class 'kmldom.Folder'>")
        self.assertEqual(Utilities().SerializeRaw(folder), '<Folder/>')

    def test_create_folder_with_attributes(self):

        folder = Kml().create_folder({'id' : 'SampleID',
                            'name' : 'SampleName',
                            'visibility' : 1,
                            'open' : 1,
#                            'atomauthor':Kml().create_atomauthor(),
#                            'atomlink':Kml().create_atomlink(),
                            'address':'1060 West Addison',
                            #  <xal:AddressDetails>...</xal:AddressDetails>  <!-- xmlns:xal -->
                            'phonenumber':'867-5309',
                            'snippet': Kml().create_snippet({'maxlines':10,'text':'Sample Snippet'}),
                            'description' : 'Sample Folder',
                            'lookat':Kml().create_lookat(),
                            'timestamp' : {'when': '2009-05-19'},
                            'styleurl':'#mainstyle',
                            'style':Kml().create_style(),
                            'region':Kml().create_region(),
                            'extendeddata':Kml().create_extendeddata({'data':Kml().create_data()}),
                                      #    'document' :
                                      #    'folder' :
                                      #  'overlay' :
                                      #  'placemark' :
                                      #  'network link' :
                                      #  'gx:tour' :
                                     })
        
        self.assertEqual(Utilities().SerializeRaw(folder),
                '<Folder id="SampleID">'
                + '<name>SampleName</name>'
                + '<visibility>1</visibility>'
                + '<open>1</open>'
                + '<address>1060 West Addison</address>'
                + '<Snippet maxLines="10">Sample Snippet</Snippet>'
                + '<description>Sample Folder</description>'
                + '<LookAt/>'
                + '<TimeStamp><when>2009-05-19</when></TimeStamp>'
                + '<styleUrl>#mainstyle</styleUrl>'
                + '<Style/><Region/>'
                + '<ExtendedData><Data/></ExtendedData>'
                + '</Folder>')

    def test_create_folder_with_timespan(self):

        folder = Kml().create_folder({'timespan' : {'begin' : '1/2/03',
                                                    'end' : '1/3/03'},
                                           })
        self.assertEqual(Utilities().SerializeRaw(folder),
                '<Folder>'
                + '<TimeSpan>'
                + '<begin>1/2/03</begin>'
                + '<end>1/3/03</end>'
                + '</TimeSpan>'
                + '</Folder>')


    def test_create_nested_folder(self):

        folder1 = Kml().create_folder({'name' : 'Inner Folder',})
        folder2 = Kml().create_folder({'name' : 'Outer Folder',
                                      'folder':folder1,})
        
        self.assertEqual(Utilities().SerializeRaw(folder2),
                '<Folder><name>Outer Folder</name>'
                + '<Folder><name>Inner Folder</name></Folder>'
                + '</Folder>')


class TestGxTour(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_gxtour(self):
        gxtour = Kml().create_gxtour()

        self.assertEqual(str(gxtour.__class__), "<class 'kmldom.GxTour'>")
        self.assertEqual(Utilities().SerializeRaw(gxtour), '<gx:Tour/>')


class TestHotSpotObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_hotspot(self):
        hotspot = Kml().create_hotspot(
                                        x = 0.5,
                                        y = 100,
                                        xunits = kmldom.UNITS_FRACTION,
                                        yunits = kmldom.UNITS_PIXELS,
                                 )

        self.assertEqual(str(hotspot.__class__), "<class 'kmldom.HotSpot'>")
        self.assertEqual(Utilities().SerializeRaw(hotspot), 
                '<hotSpot x="0.5" xunits="fraction" y="100" yunits="pixels"/>')


    def test_create_hotspot_without_enumerated_types(self):
        hotspot = Kml().create_hotspot(
                                        x = 0.5,
                                        y = 100,
                                        xunits = 'fraction',
                                        yunits = 'pixels',
                                 )

        self.assertEqual(Utilities().SerializeRaw(hotspot), 
                '<hotSpot x="0.5" xunits="fraction" y="100" yunits="pixels"/>')


class TestIconObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_icon(self):
        folder = Kml().create_icon()

        self.assertEqual(str(folder.__class__), "<class 'kmldom.Icon'>")
        self.assertEqual(Utilities().SerializeRaw(folder), '<Icon/>')  

    def test_create_icon_with_attributes(self):
        
        icon = Kml().create_icon({
            'id' : 'sample_id',
            'href' : 'http://sample.com',
            'refreshmode' : 'onchange',
            'refreshinterval' : 4,
            'viewrefreshmode' : 'never',
            'viewboundscale' : 0.8,
            'viewformat' : '[bboxWest],[bboxSouth],[bboxEast],[bboxNorth]',
            'httpquery' : '[clientVersion]',
        })

        self.assertEquals(Utilities().SerializeRaw(icon),
                '<Icon id="sample_id">'
                + '<href>http://sample.com</href>'
                + '<refreshMode>onChange</refreshMode>'
                + '<refreshInterval>4</refreshInterval>'
                + '<viewRefreshMode>never</viewRefreshMode>'
                + '<viewBoundScale>0.8</viewBoundScale>'
                + '<viewFormat>[bboxWest],[bboxSouth],[bboxEast],[bboxNorth]</viewFormat>'
                + '<httpQuery>[clientVersion]</httpQuery>'
                + '</Icon>'
            )  

    def test_create_iconstyle_with_non_enumerated_types(self):
    
        # TODO - write test for the enumerated types
        pass


class TestIconStyleObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_iconstyle(self):
        folder = Kml().create_iconstyle()

        self.assertEqual(str(folder.__class__), "<class 'kmldom.IconStyle'>")
        self.assertEqual(Utilities().SerializeRaw(folder), '<IconStyle/>')  

    def test_create_iconstyle_with_attributes(self):
    
        style = Kml().create_iconstyle({
                        'id' : 'sample_id',
                        'color' : 'ff0000ff',
                        'colormode' : kmldom.COLORMODE_NORMAL,
                        'scale' : 1.5,
                        'heading' : 45,
                        'icon' : Kml().create_iconstyleicon({
                                        'href' : 'Sunset.jpg',
                                    }),
                        'hotspot' : Kml().create_hotspot(
                                        x = 0.5,
                                        y = 100,
                                        xunits = 'fraction',
                                        yunits = 'pixels',
                                 )
                    })

        self.assertEquals(Utilities().SerializeRaw(style),
                    '<IconStyle id="sample_id">'
                    + '<color>ff0000ff</color>'
                    + '<colorMode>normal</colorMode>'
                    + '<scale>1.5</scale>'
                    + '<heading>45</heading>'
                    + '<Icon><href>Sunset.jpg</href></Icon>'
                    + '<hotSpot x="0.5" xunits="fraction" y="100" yunits="pixels"/>'
                    + '</IconStyle>'
                )

    def test_create_iconstyle_with_non_enumerated_types(self):
        
        style = Kml().create_iconstyle({
                        #'color' : kmlbase.Color32(255,0,0,255),
                        'colormode' : 'random',
                    })

        self.assertEquals(Utilities().SerializeRaw(style),
                    '<IconStyle>'
                    #+ '<color>ff0000ff</color>' TODO - allow for HEX colors
                    + '<colorMode>random</colorMode>'
                    + '</IconStyle>'
                )


class TestIconStyleIconObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_iconstyleicon(self):
        iconstyleicon = Kml().create_iconstyleicon()

        self.assertEqual(str(iconstyleicon.__class__), "<class 'kmldom.IconStyleIcon'>")
        self.assertEqual(Utilities().SerializeRaw(iconstyleicon), '<Icon/>')  

    def test_create_iconstyleicon_with_attributes(self):
    
        style = Kml().create_iconstyleicon({
                        'href' : 'Sunset.jpg',
                    })

        self.assertEquals(Utilities().SerializeRaw(style),
                    '<Icon>'
                    + '<href>Sunset.jpg</href>'
                    + '</Icon>'
                )


class TestInnerBoundaryIs(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_linestring(self):
    
        import kmldom;
        in_coord = factory.CreateCoordinates()
        in_coord.add_latlngalt(0,0,0)
        in_coord.add_latlngalt(3,0,0)
        in_coord.add_latlngalt(3,3,0)
        in_coord.add_latlngalt(0,3,0)
        in_coord.add_latlngalt(0,0,0)
        inner = Kml().create_linearring({'coordinates':in_coord,})
        innerboundaryis = Kml().create_innerboundaryis({'linearring':inner},)
        self.assertEqual(str(innerboundaryis.__class__),"<class 'kmldom.InnerBoundaryIs'>")
        self.assertEqual(Utilities().SerializeRaw(innerboundaryis),
            '<innerBoundaryIs>'
            +'<LinearRing>'
            +'<coordinates>0,0,0\n0,3,0\n3,3,0\n3,0,0\n0,0,0\n</coordinates>'
            +'</LinearRing>'
            +'</innerBoundaryIs>')


class TestLinearRingObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_linearring(self):
        linearring = Kml().create_linearring()

        self.assertEqual(str(linearring.__class__),"<class 'kmldom.LinearRing'>")
        self.assertEqual(Utilities().SerializeRaw(linearring),'<LinearRing/>')

    def test_create_linearring_with_attributes(self):

        import kmldom;
        coordinates = factory.CreateCoordinates()
        coordinates.add_latlngalt(0,0,0)
        coordinates.add_latlngalt(0,1,0)
        coordinates.add_latlngalt(1,0,0)
        coordinates.add_latlngalt(0,0,0)

        #import ipdb; ipdb.set_trace()

        linearring = Kml().create_linearring({'id' : 'Sample ID',
                            'extrude': 1,
                            'tessellate': 0,
                            'altitudemode': 'relativetoground',
                            'coordinates': coordinates,
                            })
        self.assertEquals(Utilities().SerializeRaw(linearring),
                    '<LinearRing id="Sample ID">'
                    + '<extrude>1</extrude>'
                    + '<tessellate>0</tessellate>'
                    + '<altitudeMode>relativeToGround</altitudeMode>'
                    + '<coordinates>0,0,0\n1,0,0\n0,1,0\n0,0,0\n</coordinates>'
                    + '</LinearRing>')


class TestLineStringObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_linestring(self):
        linestring = Kml().create_linestring()

        self.assertEqual(str(linestring.__class__),"<class 'kmldom.LineString'>")
        self.assertEqual(Utilities().SerializeRaw(linestring),'<LineString/>')

    def test_create_linestring_with_attributes(self):
    
        import kmldom;
        coordinates = factory.CreateCoordinates()
        coordinates.add_latlngalt(0,0,0)
        coordinates.add_latlngalt(0,1,0)
        
        linestring = Kml().create_linestring({'id' : 'Sample ID',
                            'extrude':1,
                            'tessellate':0,
                            'altitudemode': 'relativetoground',
                            'coordinates': coordinates,})                            
        self.assertEquals(Utilities().SerializeRaw(linestring),
                    '<LineString id="Sample ID">'
                    + '<extrude>1</extrude>'
                    + '<tessellate>0</tessellate>'
                    + '<altitudeMode>relativeToGround</altitudeMode>'
                    + '<coordinates>0,0,0\n1,0,0\n</coordinates>'
                    + '</LineString>')


class TestLineStyleObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_linestyle(self):
        linestyle = Kml().create_linestyle()
        self.assertEqual(str(linestyle.__class__),"<class 'kmldom.LineStyle'>")
        self.assertEqual(Utilities().SerializeRaw(linestyle),'<LineStyle/>')

    def test_create_linestyle_with_attributes(self):
        linestyle = Kml().create_linestyle({'id' : 'SampleID',
                                            'color' : 'ff0000ff',
                                            'colormode' : kmldom.COLORMODE_NORMAL,
                                            'width' : 10,
                                            })
        self.assertEquals(Utilities().SerializeRaw(linestyle),
            '<LineStyle id="SampleID">'
            + '<color>ff0000ff</color>'
            + '<colorMode>normal</colorMode>'
            + '<width>10</width>'
            + '</LineStyle>')


class TestLinkObject(unittest.TestCase):
    def setUp(self):
        pass
    def test_create_link(self):
        link = Kml().create_link()
        self.assertEqual(str(link.__class__),"<class 'kmldom.Link'>")
        self.assertEqual(Utilities().SerializeRaw(link),'<Link/>')
    def test_create_link_with_attributes(self):
        link = Kml().create_link({'id' : 'SampleID',
                                'href' : 'http://www.mtri.org',
                                'refreshmode' : 'onchange', #<refreshModeEnum: onChange, onInterval, or onExpire  
                                'refreshinterval' : 4,
                                'viewrefreshmode' : 'never', #viewRefreshModeEnum: never, onStop, onRequest, onRegion
                                'viewrefreshtime' : 0,
                                'viewboundscale' : 1,
                                #  <viewFormat>BBOX=[bboxWest],[bboxSouth],[bboxEast],[bboxNorth]</viewFormat>
                                'httpquery' : 'http://www.google.com',
                                })
        self.assertEqual(Utilities().SerializeRaw(link),
            '<Link id="SampleID">'
            +'<href>http://www.mtri.org</href>'
            +'<refreshMode>onChange</refreshMode>'
            +'<refreshInterval>4</refreshInterval>'
            +'<viewRefreshMode>never</viewRefreshMode>'
            +'<viewRefreshTime>0</viewRefreshTime>'
            +'<viewBoundScale>1</viewBoundScale>'
            +'<httpQuery>http://www.google.com</httpQuery>'
            +'</Link>')


class TestLookAtObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_lookat(self):
        lookat = Kml().create_lookat()

        self.assertEqual(str(lookat.__class__), "<class 'kmldom.LookAt'>")
        self.assertEqual(Utilities().SerializeRaw(lookat), '<LookAt/>')

    def test_create_lookat_with_attributes(self):
        lookat = Kml().create_lookat({'id' : 'SampleID',
                                    'longitude':0,
                                    'latitude':0,
                                    'altitude':0,
                                    'heading':0,
                                    'tilt':0,
                                    'range':0,
                                    'altitudemode': 'clamptoground',
                                    #'timestamp' : Kml().create_timestamp({'id':'SampleID'}),#Software does not currently support this
                                    })
        self.assertEqual(Utilities().SerializeRaw(lookat),
            '<LookAt id="SampleID">'
            +'<longitude>0</longitude>'
            +'<latitude>0</latitude>'
            +'<altitude>0</altitude>'
            +'<heading>0</heading>'
            +'<tilt>0</tilt>'
            +'<range>0</range>'
            +'<altitudeMode>clampToGround</altitudeMode>'
            +'</LookAt>'
            )


class TestMultiGeometryObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_multigeometry(self):
        multigeometry = Kml().create_multigeometry()
        self.assertEqual(str(multigeometry.__class__),"<class 'kmldom.MultiGeometry'>")
        self.assertEqual(Utilities().SerializeRaw(multigeometry),'<MultiGeometry/>')

    def test_create_multigeometry_complex(self):
            
            coordinates1 = factory.CreateCoordinates()
            coordinates1.add_latlngalt(20,40,0)
            coordinates1.add_latlngalt(90,70,0)
            linestring1 = Kml().create_linestring({'coordinates':coordinates1,})
            coordinates2 = factory.CreateCoordinates()
            coordinates2.add_latlngalt(-230,5874,0)
            coordinates2.add_latlngalt(2,27,0)
            linestring2 = Kml().create_linestring({'coordinates':coordinates2,})

            multigeometry = Kml().create_multigeometry({'linestring':[linestring1,linestring2]})
    
            self.assertEqual(Utilities().SerializeRaw(multigeometry),
                '<MultiGeometry>'
                +'<LineString>'
                +'<coordinates>40,20,0\n70,90,0\n</coordinates>'
                +'</LineString>'
                +'<LineString>'
                +'<coordinates>5874,-230,0\n27,2,0\n</coordinates>'
                +'</LineString>'
                +'</MultiGeometry>')


class TestNetworkLinkObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_networklink(self):
        networklink = Kml().create_networklink()
        self.assertEqual(str(networklink.__class__),"<class 'kmldom.NetworkLink'>")
        self.assertEqual(Utilities().SerializeRaw(networklink),'<NetworkLink/>')

    def test_create_networklink_with_attributes(self):
        networklink = Kml().create_networklink({'id':'SampleID',
                                    'name':'SampleName',
                                    'visibility':1,
                                    'open':1,
                                    #  <atom:author>...<atom:author>         <!-- xmlns:atom -->
                                    #  <atom:link>...</atom:link>            <!-- xmlns:atom -->
                                    #  <address>...</address>                <!-- string -->
                                    #  <xal:AddressDetails>...</xal:AddressDetails>  <!-- xmlns:xal -->
                                    #  <phoneNumber>...</phoneNumber>        <!-- string -->
                                    #  <Snippet maxLines="2">...</Snippet>   <!-- string -->
                                    'description':'This is a test NetworkLink',
                                    #  <AbstractView>...</AbstractView>      <!-- Camera or LookAt -->
                                    'timestamp' : {'when': '5/19/2009'},
                                    #  <styleUrl>...</styleUrl>              <!-- anyURI -->
                                    #  <StyleSelector>...</StyleSelector>
                                    #  <Region>...</Region>
                                    #  <Metadata>...</Metadata>              <!-- deprecated in KML 2.2 -->
                                    #  <ExtendedData>...</ExtendedData>      <!-- new in KML 2.2 -->
                                    'refreshvisibility':1,
                                    'flytoview':1,
                                    'link':Kml().create_link({'href':'http://www.google.com'}),
                                    })
        Utilities().SerializeRaw(networklink)

        self.assertEqual(Utilities().SerializeRaw(networklink),
                '<NetworkLink id="SampleID">'
                + '<name>SampleName</name>'
                + '<visibility>1</visibility>'
                + '<open>1</open>'
                + '<description>This is a test NetworkLink</description>'
                + '<TimeStamp><when>5/19/2009</when></TimeStamp>'
                + '<refreshVisibility>1</refreshVisibility>'
                + '<flyToView>1</flyToView>'
                + '<Link><href>http://www.google.com</href></Link>'
                + '</NetworkLink>')

    def test_create_networklink_with_timespan(self):

        networklink = Kml().create_networklink({'timespan' : {'begin' : '1/2/03',
                                                    'end' : '1/3/03'},
                                           })
        self.assertEqual(Utilities().SerializeRaw(networklink),
                '<NetworkLink>'
                + '<TimeSpan>'
                + '<begin>1/2/03</begin>'
                + '<end>1/3/03</end>'
                + '</TimeSpan>'
                + '</NetworkLink>')


class TestOuterBoundaryIs(unittest.TestCase):
    def setUp(self):
        pass
    def test_create_linestring(self):
    
        import kmldom;
        out_coord = factory.CreateCoordinates()
        out_coord.add_latlngalt(0,0,0)
        out_coord.add_latlngalt(3,0,0)
        out_coord.add_latlngalt(3,3,0)
        out_coord.add_latlngalt(0,3,0)
        out_coord.add_latlngalt(0,0,0)
        outer = Kml().create_linearring({'coordinates':out_coord,})
        outerboundaryis = Kml().create_outerboundaryis({'linearring':outer},)
        self.assertEqual(str(outerboundaryis.__class__),"<class 'kmldom.OuterBoundaryIs'>")
        self.assertEqual(Utilities().SerializeRaw(outerboundaryis),
            '<outerBoundaryIs>'
            +'<LinearRing>'
            +'<coordinates>0,0,0\n0,3,0\n3,3,0\n3,0,0\n0,0,0\n</coordinates>'
            +'</LinearRing>'
            +'</outerBoundaryIs>')


class TestPairObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_pair(self):
    
        pair = Kml().create_pair()

        self.assertEqual(str(pair.__class__), "<class 'kmldom.Pair'>")
        self.assertEqual(Utilities().SerializeRaw(pair), '<Pair/>')
    def test_create_pair_with_attributes(self):
    
        pair = Kml().create_pair({'id' : 'SampleID',
                                'key':1,
                                'styleUrl':'http://www.mtri.org',
                                })
        self.assertEqual(Utilities().SerializeRaw(pair),
            '<Pair id="SampleID">'
            + '<key>highlight</key>'
            + '<styleUrl>http://www.mtri.org</styleUrl>'
            + '</Pair>')


class TestPlacemarkObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_placemark(self):
    
        placemark = Kml().create_placemark()

        self.assertEqual(str(placemark.__class__), "<class 'kmldom.Placemark'>")
        self.assertEqual(Utilities().SerializeRaw(placemark), '<Placemark/>')

    def test_create_placemark_with_attributes(self):

        placemark = Kml().create_placemark({'id' : 'sampleID',
                                      'name' : 'Placemark Name',
                                      'visibility' : False,
                                      'open' : True,
                                      #'atom:author'
                                      #'atom:link'
                                      #'address'
                                      #'xal:address details'
                                      #'phone number'
                                      'snippet' : Kml().create_snippet({'maxlines':10,'text':'Sample Snippet'}),
                                      'description' : 'Sample Description',
                                      #'abstract view' (abstract)        
                                      #  'camera' :
                                      #  'lookat' :
                                      #'time primitive' (abstract)
#                                      'timespan' : {'begin' : '1/2/03',
#                                                    'end' : '1/3/03'},
                                      'timestamp' : {'when': '5/19/2009'},
                                      'styleurl' : 'http://style.sample.com',
                                      #'style selector' (abstract)
                                      #  'style' :
                                      #  'style map' :
                                      #'region' :
                                      #'extended data' :
                                      #'feature' (abstract)
                                      #  'feature Container (abstract)
                                      #    'document' :
                                      #    'folder' :
                                      #  'overlay' :
                                      #  'placemark' :
                                      #  'network link' :
                                      #  'gx:tour' :
                                        })
        
        self.assertEqual(Utilities().SerializeRaw(placemark),
                '<Placemark id="sampleID">'
                + '<name>Placemark Name</name>'
                + '<visibility>0</visibility>'
                + '<open>1</open>'
                + '<Snippet maxLines="10">Sample Snippet</Snippet>'
                + '<description>Sample Description</description>'
                + '<TimeStamp><when>5/19/2009</when></TimeStamp>'
                + '<styleUrl>http://style.sample.com</styleUrl>'
                + '</Placemark>')

    def test_create_placemark_with_geometry(self):

        # generate a placemark using libkml
        placemark1 = factory.CreatePlacemark()
        placemark1.set_name('Placemark Name')
        snip = factory.CreateSnippet()
        snip.set_text('Sample Snippet')
        snip.set_maxlines(10)
        placemark1.set_snippet(snip)
        placemark1.set_description('Sample Description'.encode())
        timestamp = factory.CreateTimeStamp()
        timestamp.set_when('5/19/2009')
        placemark1.set_timeprimitive(timestamp)
        coordinates = factory.CreateCoordinates()
        coordinates.add_latlng(40, -120) 
        point = factory.CreatePoint()
        point.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
        point.set_extrude(100)
        point.set_coordinates(coordinates)
        placemark1.set_geometry(point)

        # generate a placemark using pylibkml
        placemark2 = Kml().create_placemark({
                        'name' : 'Placemark Name',
                        'snippet' : Kml().create_snippet({'maxlines':10,'text':'Sample Snippet'}),
                        'description' : 'Sample Description',
                        'timestamp' : {'when': '5/19/2009'},
                        'point' :  Kml().create_point({
                            'extrude' : 100,
                            'altitudemode' : 'relativetoground',
                            'coordinates' : Kml().create_coordinates(-120,40),
                            })
                         })

        self.assertEqual(Utilities().SerializeRaw(placemark1),
                         Utilities().SerializeRaw(placemark2))


    def test_create_placemark_with_timespan(self):

        placemark = Kml().create_placemark({'timespan' : {'begin' : '1/2/03',
                                                            'end' : '1/3/03'},
                                           })
        self.assertEqual(Utilities().SerializeRaw(placemark),
                '<Placemark>'
                + '<TimeSpan>'
                + '<begin>1/2/03</begin>'
                + '<end>1/3/03</end>'
                + '</TimeSpan>'
                + '</Placemark>')


class TestPointObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_point(self):
        point = Kml().create_point()

        self.assertEqual(str(point.__class__), "<class 'kmldom.Point'>")
        self.assertEqual(Utilities().SerializeRaw(point), '<Point/>')  

    def test_create_point_with_attributes(self):
        point = Kml().create_point({
            'id' : 'Sample ID',
                        'extrude' : 100,
                        'altitudemode' : 'relativetoground',
                        'coordinates' : Kml().create_coordinates(-120,40),
                    })

        self.assertEquals(Utilities().SerializeRaw(point),
                    '<Point id="Sample ID">'
                    + '<extrude>1</extrude>'
                    + '<altitudeMode>relativeToGround</altitudeMode>'
                    + '<coordinates>-120,40,0\n</coordinates>'
                    + '</Point>'
                )


class TestPolygonObject(unittest.TestCase):

    def setUp(self):
        pass

        
    def test_create_polygon(self):
        polygon = Kml().create_polygon()

        self.assertEqual(str(polygon.__class__), "<class 'kmldom.Polygon'>")
        self.assertEqual(Utilities().SerializeRaw(polygon), '<Polygon/>')

    def test_create_polygon_with_attributes(self):

        import kmldom;
        out_coord = factory.CreateCoordinates()
        out_coord.add_latlngalt(0,0,0)
        out_coord.add_latlngalt(3,0,0)
        out_coord.add_latlngalt(3,3,0)
        out_coord.add_latlngalt(0,3,0)
        out_coord.add_latlngalt(0,0,0)

        outer = Kml().create_linearring({'coordinates':out_coord,})

        in_coord = factory.CreateCoordinates()
        in_coord.add_latlngalt(1,1,0)
        in_coord.add_latlngalt(2,1,0)
        in_coord.add_latlngalt(2,2,0)
        in_coord.add_latlngalt(1,2,0)
        in_coord.add_latlngalt(1,1,0)

        inner = Kml().create_linearring({'coordinates':in_coord,})
        
        outerBound = Kml().create_outerboundaryis({'linearring':outer,})
        innerBound = Kml().create_innerboundaryis({'linearring':inner,})

        polygon = Kml().create_polygon({'id' : 'Sample ID',
                            'extrude':1,
                            'tessellate':0,
                            'altitudemode':'relativetoground',
                            'outerboundaryis':outerBound,
                            #'innerboundaryis':innerBound, #error  in libkml, waiting for update
                            })

        self.assertEquals(Utilities().SerializeRaw(polygon),
                '<Polygon id="Sample ID">'
                + '<extrude>1</extrude>'
                + '<tessellate>0</tessellate>'
                + '<altitudeMode>relativeToGround</altitudeMode>'
                + '<outerBoundaryIs><LinearRing><coordinates>0,0,0\n0,3,0\n3,3,0\n3,0,0\n0,0,0\n</coordinates></LinearRing></outerBoundaryIs>'
                #+ '<innerBoundaryIs>0,0,0\n1,0,0\n0,1,0\n0,0,0\n</innerBoundaryIs>'
                + '</Polygon>')


class TestPolyStyleObject(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_polystyle(self):
        polystyle = Kml().create_polystyle()
        self.assertEqual(str(polystyle.__class__),"<class 'kmldom.PolyStyle'>")
        self.assertEqual(Utilities().SerializeRaw(polystyle),'<PolyStyle/>')

    def test_create_polystyle_with_attributes(self):
        polystyle = Kml().create_polystyle({'id' : 'SampleID',
                                            'color' : 'ff0000ff',
                                            'colormode' : 'normal',
                                            'fill' : 1,
                                            'outline' : 1,
                                            })
        self.assertEquals(Utilities().SerializeRaw(polystyle),
            '<PolyStyle id="SampleID">'
            + '<color>ff0000ff</color>'
            + '<colorMode>normal</colorMode>'
            + '<fill>1</fill>'
            + '<outline>1</outline>'
            + '</PolyStyle>')


class TestStyleMap(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_stylemap(self):
        stylemap = Kml().create_stylemap()
        self.assertEqual(str(stylemap.__class__), "<class 'kmldom.StyleMap'>")
        self.assertEqual(Utilities().SerializeRaw(stylemap), '<StyleMap/>')

    def test_create_stylemap_with_attributes(self):
        
        pair = Kml().create_pair({'key':0,})
        
        stylemap = Kml().create_stylemap({'id':'SampleID',
                                        'pair':pair,})
        self.assertEquals(Utilities().SerializeRaw(stylemap),
            '<StyleMap id="SampleID">'
            + '<Pair><key>normal</key></Pair>'
            + '</StyleMap>')


class TestStyleObject(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_create_style(self):
        
        style = Kml().create_style({'id' : 'sample_id'})

        self.assertEquals(Utilities().SerializeRaw(style),'<Style id="sample_id"/>')

#    def test_create_balloonstyle(self):
#        id_= 'sample_id'
#        bgcolor=kmlbase.Color32(255,0,0,255)   aBGR
#        testcolor=kmlbase.Color32(255,255,0,255)   aBGR
#        text='Sample text'
#        displaymode=kmldom.DISPLAYMODE_DEFAULT
#        
#        style = Kml().create_style({
#                            'id' : 'sample_id',
#                         })
#        style = shortcuts.create_balloonstyle(
#                id_=id_,
#                bgcolor=bgcolor,
#                textcolor=testcolor,
#                text=text,
#                displaymode=displaymode,
#            )
#        self.assertEquals(Utilities().SerializeRaw(style),
#                '<BalloonStyle id="sample_id">'
#                '<bgColor>ff0000ff</bgColor>'
#                '<textColor>ffff00ff</textColor>'
#                '<text>Sample text</text>'
#                '<displayMode>default</displayMode>'
#                '</BalloonStyle>')


class TestTimeSpan(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_create_timespan(self):
        timespan = Kml().create_timespan()
        self.assertEqual(str(timespan.__class__), "<class 'kmldom.TimeSpan'>")
        self.assertEqual(Utilities().SerializeRaw(timespan), '<TimeSpan/>')
    def test_create_timespan_with_attributes(self):
        timespan = Kml().create_timespan({'id' : 'SampleID',
                                        'begin': '1986',
                                        'end' : '2009',
                                        })
        self.assertEquals(Utilities().SerializeRaw(timespan),
            '<TimeSpan id="SampleID">'
            +'<begin>1986</begin>'
            +'<end>2009</end>'
            +'</TimeSpan>')


class TestTimeStamp(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_create_timestamp(self):
        timestamp = Kml().create_timestamp()
        self.assertEqual(str(timestamp.__class__), "<class 'kmldom.TimeStamp'>")
        self.assertEqual(Utilities().SerializeRaw(timestamp), '<TimeStamp/>')

    def test_create_timestamp_with_attributes(self):
        timestamp = Kml().create_timestamp({'id' : 'SampleID',
                                        'when' : '2009',
                                        })
        self.assertEquals(Utilities().SerializeRaw(timestamp),
            '<TimeStamp id="SampleID">'
            +'<when>2009</when>'
            +'</TimeStamp>')


class TestCompositeTests(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_nested_folders_with_pylibkml(self):
           
        import kmldom
        import pylibkml
                            
        nested_folder = Kml().create_folder(
                            {'name'  : 'Outer Folder',
                            'open'   : True,
                            'folder' : [Kml().create_folder(
                                            {'name' : 'Inner Folder 1',
                                            }),
                                        Kml().create_folder(
                                            {'name' : 'Inner Folder 2',
                                             'visibility' : False,
                                             'snippet' : Kml().create_snippet({'maxlines':10,'text':'Sample Snippet'}),
                                             'description' : '<h1>Hello World!</h1>', 
                                            })],
                            })
        #print Utilities().SerializeRaw(nested_folder)
        
        self.assertEquals(Utilities().SerializeRaw(nested_folder),
                    '<Folder>'
                        + '<name>Outer Folder</name>'
                        + '<open>1</open>'
                        + '<Folder>'
                            + '<name>Inner Folder 1</name>'
                        + '</Folder>'
                        + '<Folder>'
                            + '<name>Inner Folder 2</name>'
                            + '<visibility>0</visibility>'
                            + '<Snippet maxLines="10">Sample Snippet</Snippet>'
                            + '<description><![CDATA[<h1>Hello World!</h1>]]></description>'
                        + '</Folder>'
                    + '</Folder>')

    def test_nested_folders_without_pylibkml(self):
        
        import kmldom
        factory = kmldom.KmlFactory_GetFactory()
        
        nested_folder = factory.CreateFolder()
        nested_folder.set_name('Outer Folder')
        nested_folder.set_open(True)

        inner_folder_1 = factory.CreateFolder()
        inner_folder_1.set_name('Inner Folder 1')
        nested_folder.add_feature(inner_folder_1)
        
        inner_folder_2 = factory.CreateFolder()
        inner_folder_2.set_name('Inner Folder 2')
        inner_folder_2.set_visibility(False)
        snip = factory.CreateSnippet()
        snip.set_text('Sample Snippet')
        inner_folder_2.set_snippet(snip)
        inner_folder_2.set_description('<h1>Hello World!</h1>')
        nested_folder.add_feature(inner_folder_2)
        
        self.assertEquals(Utilities().SerializeRaw(nested_folder),
            '<Folder>'
                + '<name>Outer Folder</name>'
                + '<open>1</open>'
                + '<Folder>'
                    + '<name>Inner Folder 1</name>'
                + '</Folder>'
                + '<Folder>'
                    + '<name>Inner Folder 2</name>'
                    + '<visibility>0</visibility>'
                    + '<Snippet>Sample Snippet</Snippet>'
                    + '<description><![CDATA[<h1>Hello World!</h1>]]></description>'
                + '</Folder>'
            + '</Folder>')


class TestComplex(unittest.TestCase):

    def test_1(self):
    
        point1 = Kml().create_point({
                        'id' : 'SamplePoint1ID',
                        'extrude' : '1',
                        'altitudemode' : kmldom.ALTITUDEMODE_ABSOLUTE,
                        'coordinates' : Kml().create_coordinates(-120,40),
                    })
        point2 = Kml().create_point({
                        'id' : 'SamplePoint2ID',
                        'extrude' : '1',
                        'altitudemode' : kmldom.ALTITUDEMODE_RELATIVETOGROUND,
                        'coordinates' : Kml().create_coordinates(40,-120),
                    })
        
        multi1 = Kml().create_multigeometry({'point' : [point1,point2], })

        place1 = Kml().create_placemark({
                        'id' : 'SamplePlaceMark1ID',
                        'name' : 'Google Earth - New Placemark 1',
                        'description' : 'This is my first placemark',
                        'multigeometry' : multi1,
                    })
                                            
        coordinates1 = factory.CreateCoordinates()
        coordinates1.add_latlngalt(20,40,0)
        coordinates1.add_latlngalt(90,70,0)
        linestring1 = Kml().create_linestring({'coordinates':coordinates1,})
        coordinates2 = factory.CreateCoordinates()
        coordinates2.add_latlngalt(-230,5874,0)
        coordinates2.add_latlngalt(2,27,0)
        linestring2 = Kml().create_linestring({'coordinates':coordinates2,})
        multi2 = Kml().create_multigeometry({
                        'linestring':linestring2,
                        'linestring':linestring1,
                    })
        
        place2 = Kml().create_placemark({
                        'id' : 'SamplePlaceMark2ID',
                        'name' : 'Google Earth - New Placemark 2',
                        'description' : 'This is my second placemark',
                        'multigeometry' : multi2,
                    })
        folder = Kml().create_folder({
                        'id' : 'SampleFolderID',
                        'name' : 'Test',
                        'open' : 1,
                        'placemark' : [place1,place2]
                    })
        document = Kml().create_document({
                        'id' : 'SampleDocID',
                        'name' : 'LineString.kml',
                        'open' : 1,
                        'folder' : folder,
                    })
        #print Utilities().SerializeRaw(document)

#class TestRonsApartment(unittest.TestCase):
#    def test:
#    
#        document = Kml().create_document({'name':
#        
#                                        })

if __name__ == '__main__':
    unittest.main()

