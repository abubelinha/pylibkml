
import unittest
from pylibkml import *

class DescriptiveHTML(unittest.TestCase):
    def setUp(self):
        pass

    def test_descriptiveHTML(self):
        
        cdata = '<![CDATA[Click on the blue link!<br><br>Placemark descriptions can be enriched by using many standard HTML tags.<br>For example:<hr>Styles:<br><i>Italics</i>,<b>Bold</b>,<u>Underlined</u>,<s>Strike Out</s>,subscript<sub>subscript</sub>,superscript<sup>superscript</sup>,<big>Big</big>,<small>Small</small>,<tt>Typewriter</tt>,<em>Emphasized</em>,<strong>Strong</strong>,<code>Code</code><hr>Fonts:<br><font color="red">red by name</font>,<font color="#408010">leaf green by hexadecimal RGB</font><br><font size=1>size 1</font>,<font size=2>size 2</font>,<font size=3>size 3</font>,<font size=4>size 4</font>,<font size=5>size 5</font>,<font size=6>size 6</font>,<font size=7>size 7</font><br><font face=times>Times</font>,<font face=verdana>Verdana</font>,<font face=arial>Arial</font><br><hr>Links:<br><a href="http://earth.google.com/">Google Earth!</a><br> or:  Check out our website at www.google.com<hr>Alignment:<br><p align=left>left</p><p align=center>center</p><p align=right>right</p><hr>Ordered Lists:<br><ol><li>First</li><li>Second</li><li>Third</li></ol><ol type="a"><li>First</li><li>Second</li><li>Third</li></ol><ol type="A"><li>First</li><li>Second</li><li>Third</li></ol><hr>Unordered Lists:<br><ul><li>A</li><li>B</li><li>C</li></ul><ul type="circle"><li>A</li><li>B</li><li>C</li></ul><ul type="square"><li>A</li><li>B</li><li>C</li></ul><hr>Definitions:<br><dl><dt>Google:</dt><dd>The best thing since sliced bread</dd></dl><hr>Centered:<br><center>Time present and time past<br>Are both perhaps present in time future,<br>And time future contained in time past.<br>If all time is eternally present<br>All time is unredeemable.<br></center><hr>Block Quote:<br><blockquote>We shall not cease from exploration<br>And the end of all our exploring<br>Will be to arrive where we started<br>And know the place for the first time.<br><i>-- T.S. Eliot</i></blockquote><br><hr>Headings:<br><h1>Header 1</h1><h2>Header 2</h2><h3>Header 3</h3><h3>Header 4</h4><h3>Header 5</h5><hr>Images:<br><i>Remote image</i><br><img src="http://kml-samples.googlecode.com/svn/trunk/resources/googleSample.png"><br><i>Scaled image</i><br><img src="http://kml-samples.googlecode.com/svn/trunk/resources/googleSample.png" width=100><br><hr>Simple Tables:<br><table border="1" padding="1"><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr></table>]]>'
        coor = Kml().create_coordinates(-122.0822035425683,37.42228990140251,0)
        point = Kml().create_point({'coordinates':coor})
        placemark = Kml().create_placemark({'name':'Descriptive HTML',
                                            'visibility' : 1,
                                            'description' : cdata,
                                            'point' : point,
                                            })
        kml = Kml().create_kml({'placemark':placemark})

        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
        +'<Placemark>'
        +'<name>Descriptive HTML</name>'
        +'<visibility>1</visibility>'
        +'<description><![CDATA[Click on the blue link!<br><br>Placemark descriptions can be enriched by using many standard HTML tags.<br>For example:<hr>Styles:<br><i>Italics</i>,<b>Bold</b>,<u>Underlined</u>,<s>Strike Out</s>,subscript<sub>subscript</sub>,superscript<sup>superscript</sup>,<big>Big</big>,<small>Small</small>,<tt>Typewriter</tt>,<em>Emphasized</em>,<strong>Strong</strong>,<code>Code</code><hr>Fonts:<br><font color="red">red by name</font>,<font color="#408010">leaf green by hexadecimal RGB</font><br><font size=1>size 1</font>,<font size=2>size 2</font>,<font size=3>size 3</font>,<font size=4>size 4</font>,<font size=5>size 5</font>,<font size=6>size 6</font>,<font size=7>size 7</font><br><font face=times>Times</font>,<font face=verdana>Verdana</font>,<font face=arial>Arial</font><br><hr>Links:<br><a href="http://earth.google.com/">Google Earth!</a><br> or:  Check out our website at www.google.com<hr>Alignment:<br><p align=left>left</p><p align=center>center</p><p align=right>right</p><hr>Ordered Lists:<br><ol><li>First</li><li>Second</li><li>Third</li></ol><ol type="a"><li>First</li><li>Second</li><li>Third</li></ol><ol type="A"><li>First</li><li>Second</li><li>Third</li></ol><hr>Unordered Lists:<br><ul><li>A</li><li>B</li><li>C</li></ul><ul type="circle"><li>A</li><li>B</li><li>C</li></ul><ul type="square"><li>A</li><li>B</li><li>C</li></ul><hr>Definitions:<br><dl><dt>Google:</dt><dd>The best thing since sliced bread</dd></dl><hr>Centered:<br><center>Time present and time past<br>Are both perhaps present in time future,<br>And time future contained in time past.<br>If all time is eternally present<br>All time is unredeemable.<br></center><hr>Block Quote:<br><blockquote>We shall not cease from exploration<br>And the end of all our exploring<br>Will be to arrive where we started<br>And know the place for the first time.<br><i>-- T.S. Eliot</i></blockquote><br><hr>Headings:<br><h1>Header 1</h1><h2>Header 2</h2><h3>Header 3</h3><h3>Header 4</h4><h3>Header 5</h5><hr>Images:<br><i>Remote image</i><br><img src="http://kml-samples.googlecode.com/svn/trunk/resources/googleSample.png"><br><i>Scaled image</i><br><img src="http://kml-samples.googlecode.com/svn/trunk/resources/googleSample.png" width=100><br><hr>Simple Tables:<br><table border="1" padding="1"><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr></table>]]></description>'
        +'<Point>'
        +'<coordinates>-122.082203542568,37.4222899014025,0\n</coordinates>'
        +'</Point>'
        +'</Placemark>'
        +'</kml>'
        )

class Extruded(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_extruded(self):
        lookat = Kml().create_lookat({'longitude':-122.0857667006183,
                                        'latitude' : 37.42156927867553,
                                        'altitude' : 50,
                                        'heading' : 0,
                                        'tilt' : 45,
                                        'range' : 50,
                                        'altitudemode' : 'relativetoground',
                                        })
        icon = Kml().create_iconstyleicon({'href':'http://maps.google.com/mapfiles/kml/pal3/icon19.png'})
        iconstyle = Kml().create_iconstyle({'icon':icon})
        linestyle = Kml().create_linestyle({'width':2})
        style = Kml().create_style({'iconstyle':iconstyle,
                                    'linestyle':linestyle
                                    })
        coor = Kml().create_coordinates(-122.0857667006183,37.42156927867553,50)
        point = Kml().create_point({'extrude':1,
                                    'altitudemode':'relativetoground',
                                    'coordinates':coor
                                    })
        
        placemark = Kml().create_placemark({'name':'Extruded placemark',
                                            'visibility' : 1,
                                            'description': 'Tethered to the ground by a customizable "tail"',
                                            'lookat':lookat,
                                            'style':style,
                                            'point':point,        
                                            })
        kml = Kml().create_kml({'placemark':placemark})
        
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Placemark>'
            +'<name>Extruded placemark</name>'
            +'<visibility>1</visibility>'
            +'<description><![CDATA[Tethered to the ground by a customizable "tail"]]></description>'
            +'<LookAt>'
            +'<longitude>-122.085766700618</longitude>'
            +'<latitude>37.4215692786755</latitude>'
            +'<altitude>50</altitude>'
            +'<heading>0</heading>'
            +'<tilt>45</tilt>'
            +'<range>50</range>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'</LookAt>'
            +'<Style>'
            +'<IconStyle>'
            +'<Icon>'
            +'<href>http://maps.google.com/mapfiles/kml/pal3/icon19.png</href>'
            +'</Icon>'
            +'</IconStyle>'
            +'<LineStyle>'
            +'<width>2</width>'
            +'</LineStyle>'
            +'</Style>'
            +'<Point>'
            +'<extrude>1</extrude>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'<coordinates>-122.085766700618,37.4215692786755,50\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'</kml>')

class Floating(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_floating(self):
    
        lookat = Kml().create_lookat({'longitude':-122.084075,
                                        'latitude' : 37.4220033612141,
                                        'altitude' : 45,
                                        'heading' : 0,
                                        'tilt' : 90,
                                        'range' : 100,
                                        'altitudemode' : 'relativetoground',
                                        })
        icon = Kml().create_iconstyleicon({'href':'http://maps.google.com/mapfiles/kml/pal4/icon28.png'})
        iconstyle = Kml().create_iconstyle({'icon':icon})
        style = Kml().create_style({'iconstyle':iconstyle})
        coor = Kml().create_coordinates(-122.084075,37.4220033612141,50)
        point = Kml().create_point({'altitudemode':'relativetoground',
                                    'coordinates':coor
                                    })
        
        placemark = Kml().create_placemark({'name':'Floating placemark',
                                            'visibility' : 1,
                                            'description': 'Floats a defined distance above the ground.',
                                            'lookat':lookat,
                                            'style':style,
                                            'point':point,        
                                            })
        kml = Kml().create_kml({'placemark':placemark})
        
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Placemark>'
            +'<name>Floating placemark</name>'
            +'<visibility>1</visibility>'
            +'<description>Floats a defined distance above the ground.</description>'
            +'<LookAt>'
            +'<longitude>-122.084075</longitude>'
            +'<latitude>37.4220033612141</latitude>'
            +'<altitude>45</altitude>'
            +'<heading>0</heading>'
            +'<tilt>90</tilt>'
            +'<range>100</range>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'</LookAt>'
            +'<Style>'
            +'<IconStyle>'
            +'<Icon>'
            +'<href>http://maps.google.com/mapfiles/kml/pal4/icon28.png</href>'
            +'</Icon>'
            +'</IconStyle>'
            +'</Style>'
            +'<Point>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'<coordinates>-122.084075,37.4220033612141,50\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'</kml>')

class Simple(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_simple(self):
        coor = Kml().create_coordinates(-122.0822035425683,37.42228990140251,0)
        point = Kml().create_point({'coordinates':coor})
        placemark = Kml().create_placemark({'name':'Simple placemark',
                                            'description':'Attached to the ground. Intelligently places itself at the height of the underlying terrain.',
                                            'point' : point})
        kml = Kml().create_kml({'placemark':placemark})
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Placemark>'
            +'<name>Simple placemark</name>'
            +'<description>Attached to the ground. Intelligently places itself at the height of the underlying terrain.</description>'
            +'<Point>'
            +'<coordinates>-122.082203542568,37.4222899014025,0\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'</kml>')
            
class Absolute_Lines(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_absolute_lines(self):
        coor = []
        coor.append([-112.265654928602,36.09447672602546,2357])
        coor.append([-112.2660384528238,36.09342608838671,2357])
        coor.append([-112.2668139013453,36.09251058776881,2357])
        coor.append([-112.2677826834445,36.09189827357996,2357])
        coor.append([-112.2688557510952,36.0913137941187,2357])
        coor.append([-112.2694810717219,36.0903677207521,2357])
        coor.append([-112.2695268555611,36.08932171487285,2357])
        coor.append([-112.2690144567276,36.08850916060472,2357])
        coor.append([-112.2681528815339,36.08753813597956,2357])
        coor.append([-112.2670588176031,36.08682685262568,2357])
        coor.append([-112.2657374587321,36.08646312301303,2357])
        coordinates = Kml().create_coordinates(0,0,0,coor)
        linestring = Kml().create_linestring({'tessellate':1,
                                                'altitudemode':'absolute',
                                                'coordinates':coordinates,
                                                })
        placemark = Kml().create_placemark({'name':'Absolute',
                                            'visibility':1,
                                            'description':'Transparent purple line',
                                            'styleurl':'#transPurpleLineGreenPoly',
                                            'linestring':linestring
                                            })
        linestyle = Kml().create_linestyle({'color':'7fff00ff',
                                            'width':4
                                            })
        polystyle = Kml().create_polystyle({'color':'7f00ff00'})
        style = Kml().create_style({'id':'transPurpleLineGreenPoly',
                                    'linestyle':linestyle,
                                    'polystyle':polystyle
                                    })
        document = Kml().create_document({'name':'KmlFile',
                                            'style':style,
                                            'placemark':placemark,
                                            })
        kml = Kml().create_kml({'document':document})
        
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
                    +'<Document>'
                    +'<name>KmlFile</name>'
                    +'<Style id="transPurpleLineGreenPoly">'
                    +'<LineStyle>'
                    +'<color>7fff00ff</color>'
                    +'<width>4</width>'
                    +'</LineStyle>'
                    +'<PolyStyle>'
                    +'<color>7f00ff00</color>'
                    +'</PolyStyle>'
                    +'</Style>'
                    +'<Placemark>'
                    +'<name>Absolute</name>'
                    +'<visibility>1</visibility>'
                    +'<description>Transparent purple line</description>'
                    +'<styleUrl>#transPurpleLineGreenPoly</styleUrl>'
                    +'<LineString>'
                    +'<tessellate>1</tessellate>'
                    +'<altitudeMode>absolute</altitudeMode>'
                    +'<coordinates>'
                    +'-112.265654928602,36.0944767260255,2357\n'
                    +'-112.266038452824,36.0934260883867,2357\n'
                    +'-112.266813901345,36.0925105877688,2357\n'
                    +'-112.267782683444,36.09189827358,2357\n'
                    +'-112.268855751095,36.0913137941187,2357\n'
                    +'-112.269481071722,36.0903677207521,2357\n'
                    +'-112.269526855561,36.0893217148729,2357\n'
                    +'-112.269014456728,36.0885091606047,2357\n'
                    +'-112.268152881534,36.0875381359796,2357\n'
                    +'-112.267058817603,36.0868268526257,2357\n'
                    +'-112.265737458732,36.086463123013,2357\n'
                    +'</coordinates>'
                    +'</LineString>'
                    +'</Placemark>'
                    +'</Document>'
                    +'</kml>')
                    
class AbsoluteExtruded_Lines(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_absoluteextruded_lines(self):
        coor = []
        coor.append([-112.2550785337791,36.07954952145647,2357])
        coor.append([-112.2549277039738,36.08117083492122,2357])
        coor.append([-112.2552505069063,36.08260761307279,2357])
        coor.append([-112.2564540158376,36.08395660588506,2357])
        coor.append([-112.2580238976449,36.08511401044813,2357])
        coor.append([-112.2595218489022,36.08584355239394,2357])
        coor.append([-112.2608216347552,36.08612634548589,2357])
        coor.append([-112.262073428656,36.08626019085147,2357])
        coor.append([-112.2633204928495,36.08621519860091,2357])
        coor.append([-112.2644963846444,36.08627897945274,2357])
        coor.append([-112.2656969554589,36.08649599090644,2357])
        coordinates = Kml().create_coordinates(0,0,0,coor)
        linestring = Kml().create_linestring({'extrude':1,
                                                'tessellate':1,
                                                'altitudemode':'absolute',
                                                'coordinates':coordinates,
                                                })
        placemark = Kml().create_placemark({'name':'Absolute Extruded',
                                            'visibility':1,
                                            'description':'Transparent green wall with yellow outlines',
                                            'styleurl':'#yellowLineGreenPoly',
                                            'linestring':linestring
                                            })
        linestyle = Kml().create_linestyle({'color':'7f00ffff',
                                            'width':4
                                            })
        polystyle = Kml().create_polystyle({'color':'7f00ff00'})
        style = Kml().create_style({'id':'yellowLineGreenPoly',
                                    'linestyle':linestyle,
                                    'polystyle':polystyle
                                    })
        document = Kml().create_document({'name':'KmlFile',
                                            'style':style,
                                            'placemark':placemark,
                                            })
        kml = Kml().create_kml({'document':document})
        
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Document>'
            +'<name>KmlFile</name>'
            +'<Style id="yellowLineGreenPoly">'
            +'<LineStyle>'
            +'<color>7f00ffff</color>'
            +'<width>4</width>'
            +'</LineStyle>'
            +'<PolyStyle>'
            +'<color>7f00ff00</color>'
            +'</PolyStyle>'
            +'</Style>'
            +'<Placemark>'
            +'<name>Absolute Extruded</name>'
            +'<visibility>1</visibility>'
            +'<description>Transparent green wall with yellow outlines</description>'
            +'<styleUrl>#yellowLineGreenPoly</styleUrl>'
            +'<LineString>'
            +'<extrude>1</extrude>'
            +'<tessellate>1</tessellate>'
            +'<altitudeMode>absolute</altitudeMode>'
            +'<coordinates>'
            +'-112.255078533779,36.0795495214565,2357\n'
            +'-112.254927703974,36.0811708349212,2357\n'
            +'-112.255250506906,36.0826076130728,2357\n'
            +'-112.256454015838,36.0839566058851,2357\n'
            +'-112.258023897645,36.0851140104481,2357\n'
            +'-112.259521848902,36.0858435523939,2357\n'
            +'-112.260821634755,36.0861263454859,2357\n'
            +'-112.262073428656,36.0862601908515,2357\n'
            +'-112.26332049285,36.0862151986009,2357\n'
            +'-112.264496384644,36.0862789794527,2357\n'
            +'-112.265696955459,36.0864959909064,2357\n'
            +'</coordinates>'
            +'</LineString>'
            +'</Placemark>'
            +'</Document>'
            +'</kml>')
            
class AbsoluteExtruded_Polygon(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_absoluteextruded_polygon(self):
        coor = []
        coor.append([-112.3396586818843,36.14637618647505,1784])
        coor.append([-112.3380597654315,36.14531751871353,1784])
        coor.append([-112.3368254237788,36.14659596244607,1784])
        coor.append([-112.3384555043203,36.14762621763982,1784])
        coor.append([-112.3396586818843,36.14637618647505,1784])
        coordinates = Kml().create_coordinates(0,0,0,coor)
        linearring = Kml().create_linearring({'coordinates':coordinates})
        outerboundaryis = Kml().create_outerboundaryis({'linearring':linearring})
        polygon = Kml().create_polygon({'extrude':1,
                                        'tessellate':1,
                                        'altitudemode':'absolute',
                                        'outerboundaryis':outerboundaryis,
                                        })
        placemark = Kml().create_placemark({'name':'Absolute Extruded',
                                            'visibility':1,
                                            'styleurl':'#transRedPoly',
                                            'polygon':polygon,
                                            })
        linestyle = Kml().create_linestyle({'width':1.5})
        polystyle = Kml().create_polystyle({'color':'7d0000ff'})
        style = Kml().create_style({'id':'transRedPoly',
                                    'linestyle':linestyle,
                                    'polystyle':polystyle,
                                    })
        document = Kml().create_document({'name':'KmlFile',
                                            'style':style,
                                            'placemark':placemark
                                            })
        kml = Kml().create_kml({'document':document})
                                    
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
                +'<Document>'
                +'<name>KmlFile</name>'
                +'<Style id="transRedPoly">'
                +'<LineStyle>'
                +'<width>1.5</width>'
                +'</LineStyle>'
                +'<PolyStyle>'
                +'<color>7d0000ff</color>'
                +'</PolyStyle>'
                +'</Style>'
                +'<Placemark>'
                +'<name>Absolute Extruded</name>'
                +'<visibility>1</visibility>'
                +'<styleUrl>#transRedPoly</styleUrl>'
                +'<Polygon>'
                +'<extrude>1</extrude>'
                +'<tessellate>1</tessellate>'
                +'<altitudeMode>absolute</altitudeMode>'
                +'<outerBoundaryIs>'
                +'<LinearRing>'
                +'<coordinates>'
                +'-112.339658681884,36.1463761864751,1784\n'
                +'-112.338059765431,36.1453175187135,1784\n'
                +'-112.336825423779,36.1465959624461,1784\n'
                +'-112.33845550432,36.1476262176398,1784\n'
                +'-112.339658681884,36.1463761864751,1784\n'
                +'</coordinates>'
                +'</LinearRing>'
                +'</outerBoundaryIs>'
                +'</Polygon>'
                +'</Placemark>'
                +'</Document>'
                +'</kml>')

class SharedTextures(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_sharedtextures(self):
        placemark=[]
        lookat = Kml().create_lookat({'longitude':-122.4517133643085,
                                        'latitude':37.80565962914491,
                                        'altitude':0,
                                        'heading':-82.34248730008207,
                                        'tilt':54.9531454664821,
                                        'range':25.90180128676323
                                        })
        building_lookat = Kml().create_lookat({'longitude':-122.4517356100782,
                                        'latitude':37.80563618786606,
                                        'altitude':0,
                                        'heading':-45.66107020637173,
                                        'tilt':62.13449005947708,
                                        'range':26.3902309532964
                                        })
        building_location = Kml().create_location({'longitude':-122.451703589982,
                                                    'latitude':37.80564180933
                                                    })
        building_link = Kml().create_link({'href':'http://kml-samples.googlecode.com/svn/trunk/resources/bldg.dae'})
        building_alias = []
        building_alias.append(Kml().create_alias({'targethref':'textures/stone0noCulling.jpg',
                                                'sourcehref':'../images/stone0noCulling.jpg'
                                                }))
        building_alias.append(Kml().create_alias({'targethref':'textures/wood0noCulling.jpg',
                                                'sourcehref':'../images/wood0noCulling.jpg'
                                                }))
        building_resourcemap = Kml().create_resourcemap({'alias':building_alias})
        building_model = Kml().create_model({'location':building_location,
                                                'link':building_link,
                                                'resourcemap':building_resourcemap})
        placemark.append(Kml().create_placemark({'id':'building',
                                                    'name' : 'Building',
                                                    'lookat':building_lookat,
                                                    'model' : building_model
                                                    }))
        wall_lookat = Kml().create_lookat({'longitude':-122.4516467177083,
                                        'latitude':37.80570794130989,
                                        'altitude':0,
                                        'heading':152.8404649459777,
                                        'tilt':54.95314560624531,
                                        'range':16.04792753907824
                                        })
        wall_location = Kml().create_location({'longitude':-122.451703589982,
                                                    'latitude':37.80564180933
                                                    })
        wall_link = Kml().create_link({'href':'http://kml-samples.googlecode.com/svn/trunk/resources/wall.dae'})
        wall_alias = []
        wall_alias.append(Kml().create_alias({'targethref':'textures/wood0noCulling.jpg',
                                                'sourcehref':'../images/stone0noCulling.jpg'
                                                }))
        wall_alias.append(Kml().create_alias({'targethref':'textures/stone0noCulling.jpg',
                                                'sourcehref':'../images/wood0noCulling.jpg'
                                                }))
        wall_resourcemap = Kml().create_resourcemap({'alias':wall_alias})
        wall_model = Kml().create_model({'location':wall_location,
                                                'link':wall_link,
                                                'resourcemap':wall_resourcemap})
        placemark.append(Kml().create_placemark({'id':'wall',
                                                    'name' : 'Wall',
                                                    'lookat':wall_lookat,
                                                    'model' : wall_model
                                                    }))
        folder = Kml().create_folder({'name':'Building and Wall',
                                        'description':'Building and Wall share textures',
                                        'lookat':lookat,
                                        'placemark':placemark,
                                        })
        kml = Kml().create_kml({'folder':folder})

        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
                +'<Folder>'
                +'<name>Building and Wall</name>'
                +'<description>Building and Wall share textures</description>'
                +'<LookAt>'
                +'<longitude>-122.451713364309</longitude>'
                +'<latitude>37.8056596291449</latitude>'
                +'<altitude>0</altitude>'
                +'<heading>-82.3424873000821</heading>'
                +'<tilt>54.9531454664821</tilt>'
                +'<range>25.9018012867632</range>'
                +'</LookAt>'
                +'<Placemark id="building">'
                +'<name>Building</name>'
                +'<LookAt>'
                +'<longitude>-122.451735610078</longitude>'
                +'<latitude>37.8056361878661</latitude>'
                +'<altitude>0</altitude>'
                +'<heading>-45.6610702063717</heading>'
                +'<tilt>62.1344900594771</tilt>'
                +'<range>26.3902309532964</range>'
                +'</LookAt>'
                +'<Model>'
                +'<Location>'
                +'<longitude>-122.451703589982</longitude>'
                +'<latitude>37.80564180933</latitude>'
                +'</Location>'
                +'<Link>'
                +'<href>http://kml-samples.googlecode.com/svn/trunk/resources/bldg.dae</href>'
                +'</Link>'
                +'<ResourceMap>'
                +'<Alias>'
                +'<targetHref>textures/stone0noCulling.jpg</targetHref>'
                +'<sourceHref>../images/stone0noCulling.jpg</sourceHref>'
                +'</Alias>'
                +'<Alias>'
                +'<targetHref>textures/wood0noCulling.jpg</targetHref>'
                +'<sourceHref>../images/wood0noCulling.jpg</sourceHref>'
                +'</Alias>'
                +'</ResourceMap>'
                +'</Model>'
                +'</Placemark>'
                +'<Placemark id="wall">'
                +'<name>Wall</name>'
                +'<LookAt>'
                +'<longitude>-122.451646717708</longitude>'
                +'<latitude>37.8057079413099</latitude>'
                +'<altitude>0</altitude>'
                +'<heading>152.840464945978</heading>'
                +'<tilt>54.9531456062453</tilt>'
                +'<range>16.0479275390782</range>'
                +'</LookAt>'
                +'<Model>'
                +'<Location>'
                +'<longitude>-122.451703589982</longitude>'
                +'<latitude>37.80564180933</latitude>'
                +'</Location>'
                +'<Link>'
                +'<href>http://kml-samples.googlecode.com/svn/trunk/resources/wall.dae</href>'
                +'</Link>'
                +'<ResourceMap>'
                +'<Alias>'
                +'<targetHref>textures/wood0noCulling.jpg</targetHref>'
                +'<sourceHref>../images/stone0noCulling.jpg</sourceHref>'
                +'</Alias>'
                +'<Alias>'
                +'<targetHref>textures/stone0noCulling.jpg</targetHref>'
                +'<sourceHref>../images/wood0noCulling.jpg</sourceHref>'
                +'</Alias>'
                +'</ResourceMap>'
                +'</Model>'
                +'</Placemark>'
                +'</Folder>'
                +'</kml>')

class CrossHairs(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_crosshairs(self):
        icon = Kml().create_icon({'href':'http://kml-samples.googlecode.com/svn/trunk/resources/crosshairs.png'})
        overlayxy = Kml().create_overlayxy({'x':0.5,
                                            'xunits':'fraction',
                                            'y':0.5,
                                            'yunits':'fraction',
                                            })
        screenxy = Kml().create_screenxy({'x':0.5,
                                            'y':0.5,
                                            'xunits':'fraction',
                                            'yunits':'fraction',
                                            })
        rotationxy = Kml().create_rotationxy({'x':0.5,
                                            'y':0.5,
                                            'xunits':'fraction',
                                            'yunits':'fraction',
                                            })
        size = Kml().create_size({'x':0,
                                    'y':0,
                                    'xunits':'pixels',
                                    'yunits':'pixels',
                                    })
        screenoverlay = Kml().create_screenoverlay({'name':'Simple crosshairs',
                                                    'visibility':1,
                                                    'description':'This screen overlay uses fractional positioning to put the image in the exact center of the screen',
                                                    'icon':icon,
                                                    'overlayxy':overlayxy,
                                                    'screenxy':screenxy,
                                                    'rotationxy':rotationxy,
                                                    'size':size,
                                                    })
        kml = Kml().create_kml({'screenoverlay':screenoverlay,})
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
                +'<ScreenOverlay>'
                +'<name>Simple crosshairs</name>'
                +'<visibility>1</visibility>'
                +'<description>This screen overlay uses fractional positioning to put the image in the exact center of the screen</description>'
                +'<Icon>'
                +'<href>http://kml-samples.googlecode.com/svn/trunk/resources/crosshairs.png</href>'
                +'</Icon>'
                +'<overlayXY x="0.5" xunits="fraction" y="0.5" yunits="fraction"/>'
                +'<screenXY x="0.5" xunits="fraction" y="0.5" yunits="fraction"/>'
                +'<rotationXY x="0.5" xunits="fraction" y="0.5" yunits="fraction"/>'
                +'<size x="0" xunits="pixels" y="0" yunits="pixels"/>'
                +'</ScreenOverlay>'
                +'</kml>')

class CompleteTouringDemo(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_completetouringdemo(self):
        gxlist = []
        camera1 = Kml().create_camera({'longitude':170.157,
                                          'latitude':-43.671,
                                          'altitude':9700,
                                          'heading':-6.333,
                                          'tilt':33.5,
                                          })
        gxlist.append(Kml().create_gxflyto({'gxduration':5.0,
                                            'camera':camera1
                                            }))
        gxlist.append(Kml().create_gxwait({'gxduration':1.0,}))
        camera2= Kml().create_camera({'longitude':174.063,
                                          'latitude':-39.663,
                                          'altitude':18275,
                                          'heading':-4.921,
                                          'tilt':65,
                                          'altitudemode':'absolute',
                                          })
        gxlist.append(Kml().create_gxflyto({'gxduration':6.0,
                                            'camera':camera2
                                            }))
        lookat1 = Kml().create_lookat({'longitude':174.007,
                                          'latitude':-39.279,
                                          'altitude':0,
                                          'heading':112.817,
                                          'tilt':68.065,
                                          'range':6811.884,
                                          'altitudemode':'relativetoground',
                                          })
        gxlist.append(Kml().create_gxflyto({'gxduration':3.0,
                                            'gxflytomode':'smooth',
                                            'camera':lookat1
                                            }))
        lookat2 = Kml().create_lookat({'longitude':174.064,
                                          'latitude':-39.321,
                                          'altitude':0,
                                          'heading':-48.463,
                                          'tilt':67.946,
                                          'range':4202.579,
                                          'altitudemode':'relativetoground',
                                          })
        gxlist.append(Kml().create_gxflyto({'gxduration':3.0,
                                            'gxflytomode':'smooth',
                                            'lookat':lookat2,
                                            }))
        lookat3 = Kml().create_lookat({'longitude':175.365,
                                          'latitude':-36.523,
                                          'altitude':0,
                                          'heading':-95,
                                          'tilt':65,
                                          'range':2500,
                                          'altitudemode':'relativetoground',
                                          })
        gxlist.append(Kml().create_gxflyto({'gxduration':5.0,
                                            'lookat':lookat3,
                                            }))
        gxplace = Kml().create_placemark({'targetid':'pin2',
                                            'gxballoonvisibility':1,
                                            })
        change = Kml().create_change({'placemark':gxplace})
        update = Kml().create_update({'targethref':'',
                                        'change':change,
                                        })
        gxlist.append(Kml().create_gxanimatedupdate({'gxduration':0.0,
                                                        'update':update,
                                                        }))
        gxlist.append(Kml().create_gxwait({'gxduration':6.0,}))
        gxplaylist = Kml().create_gxplaylist({'gxflyto':gxlist})
        gxtour = Kml().create_gxtour({'name':'Play me!',
                                        'gxplaylist':gxplaylist})

        icon = Kml().create_iconstyleicon({'href':'http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png',})
        iconstyle = Kml().create_iconstyle({'icon':icon})
        style = Kml().create_style({'id':'pushpin',
                                    'iconstyle':iconstyle
                                    })
        placemark = []
        point1 = Kml().create_point({'coordinates':Kml().create_coordinates(170.144,-43.605,0)})
        placemark.append(Kml().create_placemark({'id':'mountainpin1',
                                                'name':"New Zealand's Southern Alps",
                                                'styleurl':'#pushpin',
                                                'point':point1
                                                }))
        point2 = Kml().create_point({'coordinates':Kml().create_coordinates(175.370,-36.526,0)})
        placemark.append(Kml().create_placemark({'id':'pin2',
                                                'name':"The End",
                                                'description':'Learn more at http://code.google.com/apis/kml/documentation',
                                                'styleurl':'#pushpin',
                                                'point':point2
                                                }))
        coor = []
        coor.append([175.365,-36.522,0])
        coor.append([175.366,-36.530,0])
        coor.append([175.369,-36.529,0])
        coor.append([175.366,-36.521,0])
        coor.append([175.365,-36.522,0])
        linearring = Kml().create_linearring({'coordinates':Kml().create_coordinates(0,0,0,coor)})
        outerboundaryis = Kml().create_outerboundaryis({'linearring':linearring})
        polygon = Kml().create_polygon({'tessellate':1,
                                        'outerboundaryis':outerboundaryis
                                        })
        placemark.append(Kml().create_placemark({'id':'polygon1',
                                                    'name':'Polygon',
                                                    'polygon':polygon,
                                                    }))
        folder = Kml().create_folder({'name':'Points and polygons',
                                        'style':style,
                                        'placemark':placemark
                                        })
        document = Kml().create_document({'name':'A tour and some features',
                                            'open':1,
                                            'gxtour':gxtour,
                                            'folder':folder,
                                        })
        kml = Kml().create_kml({'document':document})
        
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Document>'
            +'<name>A tour and some features</name>'
            +'<open>1</open>'
            +'<gx:Tour>'
            +'<name>Play me!</name>'
            +'<gx:Playlist>'
            +'<gx:FlyTo>'
            +'<gx:duration>5</gx:duration>'
            +'<Camera>'
            +'<longitude>170.157</longitude>'
            +'<latitude>-43.671</latitude>'
            +'<altitude>9700</altitude>'
            +'<heading>-6.333</heading>'
            +'<tilt>33.5</tilt>'
            +'</Camera>'
            +'</gx:FlyTo>'
            +'<gx:Wait>'
            +'<gx:duration>1</gx:duration>'
            +'</gx:Wait>'
            +'<gx:FlyTo>'
            +'<gx:duration>6</gx:duration>'
            +'<Camera>'
            +'<longitude>174.063</longitude>'
            +'<latitude>-39.663</latitude>'
            +'<altitude>18275</altitude>'
            +'<heading>-4.921</heading>'
            +'<tilt>65</tilt>'
            +'<altitudeMode>absolute</altitudeMode>'
            +'</Camera>'
            +'</gx:FlyTo>'
            +'<gx:FlyTo>'
            +'<gx:duration>3</gx:duration>'
            +'<gx:flyToMode>smooth</gx:flyToMode>'
            +'<LookAt>'
            +'<longitude>174.007</longitude>'
            +'<latitude>-39.279</latitude>'
            +'<altitude>0</altitude>'
            +'<heading>112.817</heading>'
            +'<tilt>68.065</tilt>'
            +'<range>6811.884</range>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'</LookAt>'
            +'</gx:FlyTo>'
            +'<gx:FlyTo>'
            +'<gx:duration>3</gx:duration>'
            +'<gx:flyToMode>smooth</gx:flyToMode>'
            +'<LookAt>'
            +'<longitude>174.064</longitude>'
            +'<latitude>-39.321</latitude>'
            +'<altitude>0</altitude>'
            +'<heading>-48.463</heading>'
            +'<tilt>67.946</tilt>'
            +'<range>4202.579</range>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'</LookAt>'
            +'</gx:FlyTo>'
            +'<gx:FlyTo>'
            +'<gx:duration>5</gx:duration>'
            +'<LookAt>'
            +'<longitude>175.365</longitude>'
            +'<latitude>-36.523</latitude>'
            +'<altitude>0</altitude>'
            +'<heading>-95</heading>'
            +'<tilt>65</tilt>'
            +'<range>2500</range>'
            +'<altitudeMode>relativeToGround</altitudeMode>'
            +'</LookAt>'
            +'</gx:FlyTo>'
            +'<gx:AnimatedUpdate>'
            +'<gx:duration>0</gx:duration>'
            +'<Update>'
            +'<targetHref/>'
            +'<Change>'
            +'<Placemark targetId="pin2">'
            +'<gx:balloonVisibility>1</gx:balloonVisibility>'
            +'</Placemark>'
            +'</Change>'
            +'</Update>'
            +'</gx:AnimatedUpdate>'
            +'<gx:Wait>'
            +'<gx:duration>6</gx:duration>'
            +'</gx:Wait>'
            +'</gx:Playlist>'
            +'</gx:Tour>'
            +'<Folder>'
            +'<name>Points and polygons</name>'
            +'<Style id="pushpin">'
            +'<IconStyle>'
            +'<Icon>'
            +'<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>'
            +'</Icon>'
            +'</IconStyle>'
            +'</Style>'
            +'<Placemark id="mountainpin1">'
            +'<name><![CDATA[New Zealand\'s Southern Alps]]></name>'
            +'<styleUrl>#pushpin</styleUrl>'
            +'<Point>'
            +'<coordinates>170.144,-43.605,0\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'<Placemark id="pin2">'
            +'<name>The End</name>'
            +'<description>'
            +'Learn more at http://code.google.com/apis/kml/documentation'
            +'</description>'
            +'<styleUrl>#pushpin</styleUrl>'
            +'<Point>'
            +'<coordinates>175.37,-36.526,0\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'<Placemark id="polygon1">'
            +'<name>Polygon</name>'
            +'<Polygon>'
            +'<tessellate>1</tessellate>'
            +'<outerBoundaryIs>'
            +'<LinearRing>'
            +'<coordinates>'
            +'175.365,-36.522,0\n'
            +'175.366,-36.53,0\n'
            +'175.369,-36.529,0\n'
            +'175.366,-36.521,0\n'
            +'175.365,-36.522,0\n'
            +'</coordinates>'
            +'</LinearRing>'
            +'</outerBoundaryIs>'
            +'</Polygon>'
            +'</Placemark>'
            +'</Folder>'
            +'</Document>'
            +'</kml>')

class Styles_Rollover(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_styles_rollover(self):
        iconstyleicon = Kml().create_iconstyleicon({'href':'http://maps.google.com/mapfiles/kml/paddle/wht-blank.png'})
        iconstyle = Kml().create_iconstyle({'icon':iconstyleicon})
        labelstyle = Kml().create_labelstyle({'color':'7fffffff',
                                                'colormode':'normal'})
        style = Kml().create_style({'iconstyle':iconstyle,
                                    'labelstyle':labelstyle})
        pair = []
        pair.append(Kml().create_pair({'key':'normal',
                                        'style':style
                                        }))
        iconstyleicon = Kml().create_iconstyleicon({'href':'http://maps.google.com/mapfiles/kml/paddle/red-stars.png'})
        iconstyle = Kml().create_iconstyle({'icon':iconstyleicon})
        labelstyle = Kml().create_labelstyle({'color':'ff8888ff',
                                                'colormode':'normal'})
        style = Kml().create_style({'iconstyle':iconstyle,
                                    'labelstyle':labelstyle})
        pair.append(Kml().create_pair({'key':'highlight',
                                        'style':style
                                        }))
        stylemap = Kml().create_stylemap({'id':'exampleStyleMap',
                                            'pair':pair,
                                        })
        point = Kml().create_point({'coordinates':Kml().create_coordinates(-122.0856545755255,37.42243077405461,0)})
        placemark = Kml().create_placemark({'name':'Roll over this icon',
                                            'visibility':1,
                                            'styleurl':'#exampleStyleMap',
                                            'point':point
                                            })
        document = Kml().create_document({'name':'Highlighted Icon',
                                            'description':'Place your mouse over the icon to see it display the new icon',
                                            'stylemap':stylemap,
                                            'placemark':placemark
                                            })
        kml = Kml().create_kml({'document':document})
        self.assertEqual(Kml().SerializeRaw(kml),'<kml>'
            +'<Document>'
            +'<name>Highlighted Icon</name>'
            +'<description>Place your mouse over the icon to see it display the new icon</description>'
            +'<StyleMap id="exampleStyleMap">'
            +'<Pair>'
            +'<key>normal</key>'
            +'<Style>'
            +'<IconStyle>'
            +'<Icon>'
            +'<href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href>'
            +'</Icon>'
            +'</IconStyle>'
            +'<LabelStyle>'
            +'<color>7fffffff</color>'
            +'<colorMode>normal</colorMode>'
            +'</LabelStyle>'
            +'</Style>'
            +'</Pair>'
            +'<Pair>'
            +'<key>highlight</key>'
            +'<Style>'
            +'<IconStyle>'
            +'<Icon>'
            +'<href>http://maps.google.com/mapfiles/kml/paddle/red-stars.png</href>'
            +'</Icon>'
            +'</IconStyle>'
            +'<LabelStyle>'
            +'<color>ff8888ff</color>'
            +'<colorMode>normal</colorMode>'
            +'</LabelStyle>'
            +'</Style>'
            +'</Pair>'
            +'</StyleMap>'
            +'<Placemark>'
            +'<name>Roll over this icon</name>'
            +'<visibility>1</visibility>'
            +'<styleUrl>#exampleStyleMap</styleUrl>'
            +'<Point>'
            +'<coordinates>-122.085654575525,37.4224307740546,0\n</coordinates>'
            +'</Point>'
            +'</Placemark>'
            +'</Document>'
            +'</kml>')


if __name__ == '__main__':
    unittest.main()
