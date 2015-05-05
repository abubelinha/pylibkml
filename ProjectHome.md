### This project is no longer being actively developed. If you are interested in generating KML using Python, visit http://code.google.com/p/pykml/ ###

pylibkml is Python wrapper for Google's [libkml](http://code.google.com/p/libkml/) library that allows for creating valid [KML](http://code.google.com/apis/kml/documentation/kmlreference.html) documents using a more 'pythonic' syntax than the SWIG-generated Python bindings provided by libkml.

For example, the following code generates a placemark object using **pylibkml**:
```
from pylibkml import Kml
placemark = Kml().create_placemark({
                'name' : 'Placemark Name',
                'snippet' : 'Sample Snippet',
                'description' : 'Sample Description',
                'timestamp' : {'when': '5/19/2009'},
                'point' :  Kml().create_point({
                    'extrude' : True,
                    'altitudemode' : 'relativetoground',
                    'coordinates' : Kml().create_coordinates(-120,40),
                    })
                 })
```

This is equivalent to the following code, which generates a placemark object using **libkml**:
```
import kmldom
factory = kmldom.KmlFactory_GetFactory()
placemark = factory.CreatePlacemark()
placemark.set_name('Placemark Name')
snip = factory.CreateSnippet()
snip.set_text('Sample Snippet')
placemark.set_snippet(snip)
placemark.set_description('Sample Description'.encode())
timestamp = factory.CreateTimeStamp()
timestamp.set_when('5/19/2009')
placemark.set_timeprimitive(timestamp)
coordinates = factory.CreateCoordinates()
coordinates.add_latlng(40, -120) 
point = factory.CreatePoint()
point.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
point.set_extrude(True)
point.set_coordinates(coordinates)
placemark.set_geometry(point)
```

Both code blocks result in the following KML text (once serialized using `kmldom.SerializeRaw(placemark)`):

```
<Placemark>
  <name>Placemark Name</name>
  <Snippet>Sample Snippet</Snippet>
  <description>Sample Description</description>
  <TimeStamp>
    <when>5/19/2009</when>
  </TimeStamp>
  <Point>
    <extrude>1</extrude>
    <altitudeMode>relativeToGround</altitudeMode>
    <coordinates>-120,40,0\n</coordinates>
  </Point>
</Placemark>
```