#Import necessary libraries
from pylibkml import Kml, Utilities
from csv import reader
from string import atof, replace
import urllib2

def process_datetime(datestr):
    '''
    Takes the string value and processes it into something that Google Earth
    can use in its <TimeStamp>
    
    Keyword arguments:
    datestr -- (string) The DateTime string
    '''
    #Get rid of the extra space between the day and month
    datestr = replace(datestr,'  ',' ')
    #Get rid of the commas
    datestr = replace(datestr,',','')
    #Turn the string into a list
    datestr = datestr.split(' ')
    #Create a list of months to search though
    month = ['January','February','March','April','May','June',
        'July','August','September','October','November','December']
    #Find the numerical value of the month
    month_index = month.index(datestr[1])+1
    #Create the string for the <TimeStamp>
    retstring = datestr[3]+'-'+str(month_index).zfill(2)+'-'+datestr[2].zfill(2)
    return retstring+'T'+datestr[4]+'Z'
    
def main():
    '''
    A basic tutorial explaining pylibkml
    
    Extracts from a .csv file and makes a tutorial.kml file
    '''
    
    #Code required to grab file from website and save it
    url = 'http://earthquake.usgs.gov/eqcenter/catalogs/eqs7day-M1.txt'
    webFile = urllib2.urlopen(url)
    localFile = open(url.split('/')[-1], 'w')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()

    inputfile = reader(file(url.split('/')[-1]), delimiter=',')
    inputfile.next() # Get rid of the header information
    
    #Initialize the Data Lists
    Eqid = [];DateTime = [];Lat=[];Lon=[];Mag=[];Depth=[];NST=[];Location=[]
    #Cycle through the .csv file and extract all necessary data to populate
    #the data lists
    for line in inputfile:
        Eqid.append(line[1])
        DateTime.append(line[3])
        Lat.append(line[4])
        Lon.append(line[5])
        Mag.append(line[6])
        Depth.append(line[7])
        NST.append(line[8])
        Location.append(line[9])
    
    #Create the placemarks with the necessary data
    placemark = []
    for i in range(0,len(Lat)):
        #Create a <coordinate> object
        coordinate = Kml().create_coordinates(atof(Lon[i]),atof(Lat[i]))
        #Create a <Point> object
        point = Kml().create_point({'coordinates':coordinate})
        #Modify the datestring so that it works with the .kml file
        datestr = process_datetime(DateTime[i])
        #Create the <TimeStamp> object
        timestamp = Kml().create_timestamp({'when':datestr})
        #Create the <Data> objects and place them in <ExtendedData>
        data = []
        data.append(Kml().create_data({'name':'eqid','value':Eqid[i]}))
        data.append(Kml().create_data({'name':'datetime','value':DateTime[i]}))
        data.append(Kml().create_data({'name':'lat','value':Lat[i]}))
        data.append(Kml().create_data({'name':'lon','value':Lon[i]}))
        data.append(Kml().create_data({'name':'mag','value':Mag[i]}))
        data.append(Kml().create_data({'name':'depth','value':Depth[i]}))
        data.append(Kml().create_data({'name':'nst','value':NST[i]}))
        data.append(Kml().create_data({'name':'location','value':Location[i]}))
        extendeddata = Kml().create_extendeddata({'data':data})
        #Create the <Placemark> object
        placemark.append(Kml().create_placemark({'name':Eqid[i],
                                                'point':point,
                                                'timestamp':timestamp,
                                                'extendeddata':extendeddata,
                                                'styleurl':'#primary-style'}))
    #Create the <Icon> object for the <IconStyle>
    icon_href = 'http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
    iconstyleicon = Kml().create_iconstyleicon({'href': icon_href})
    #Create the <IconStyle> object
    iconstyle = Kml().create_iconstyle({'color':'ff0400ff',
                                        'scale' : 1.2,
                                        'colormode': 'normal',
                                        'icon':iconstyleicon})
    #Create the <BalloonStyle> object
    balloon_txt = '<![CDATA[<BODY bgcolor="ff0004">\n<h3>USGS Earthquake Data'+\
        '<TABLE BORDER=1>\n'+\
        '<tr><td><b>Earthquake ID</b></td><td>$[eqid]</td></tr>\n'+\
        '<tr><td><b>Date/Time</b></td><td>$[datetime]</td></tr>\n'+\
        '<tr><td><b>Latitude,Longitude</b></td><td>$[lat],$[lon]</td></tr>\n'+\
        '<tr><td><b>Magnitude</b></td><td>$[mag]</td></tr>\n'+\
        '<tr><td><b>Depth</b></td><td>$[depth]</td></tr>\n'+\
        '<tr><td><b>NST</b></td><td>$[nst]</td></tr>\n'+\
        '<tr><td><b>Location</b></td><td>$[location]</td></tr>\n'+\
        '</TABLE>\n</BODY>\n]]>'
    balloonstyle = Kml().create_balloonstyle({'text':balloon_txt,
                                                'bgcolor':'ff0400ff'})
    #Create the <Style> object with <IconStyle> and <BalloonStyle>
    style = []
    style.append(Kml().create_style({'id':'primary-style',
                                'balloonstyle':balloonstyle,
                                'iconstyle':iconstyle}))
                                
    #Put the Placemarks in a <Folder> object
    folder = []
    folder.append(Kml().create_folder({'name':'USGS Earthquakes',
                                    'placemark':placemark}))
    
    #Demonstrating a Doughnut shaped Polygon
    coord_out = [(-122.366278,37.818844,30),
            (-122.365248,37.819267,30),
            (-122.365640,37.819861,30),
            (-122.366669,37.819429,30),
            (-122.366278,37.818844,30)]
    coord_out = Kml().create_coordinates(coord_out)
    outer_ring = Kml().create_linearring({'coordinates':coord_out})
    outerboundary = Kml().create_outerboundaryis({'linearring':outer_ring})
    coord_in = [(-122.366212,37.818977,30),
            (-122.365424,37.819294,30),
            (-122.365704,37.819731,30),
            (-122.366488,37.819402,30),
            (-122.366212,37.818977,30)]
    coord_in = Kml().create_coordinates(coord_in)
    inner_ring = Kml().create_linearring({'coordinates':coord_in})
    innerboundary = Kml().create_innerboundaryis({'linearring':inner_ring})
    polygon = Kml().create_polygon({'extrude':1,
                                    'altitudemode':'relativetoground',
                                    'innerboundaryis':innerboundary,
                                    'outerboundaryis':outerboundary})
    placemark = Kml().create_placemark({'name':'Sample Doughnut Polygon',
                                        'polygon':polygon,
                                        'styleurl':'#poly-style'})
    folder.append(Kml().create_folder({'name':'Sample Polygons',
                                        'placemark':placemark}))
    #<Style> for the <Polygon> demonstration
    polystyle = Kml().create_polystyle({'color':'ffff0000',
                                        'fill':1,
                                        'outline':1})
    style.append(Kml().create_style({'id':'poly-style',
                                        'polystyle':polystyle}))

    #Put everything in a <Document> object
    document = Kml().create_document({'folder':folder,
                                        'style':style})
    #Create the final <Kml> object
    kml = Kml().create_kml({'document':document})
    #Write the Kml object to tutorial.kml
    toFile = open('tutorial.kml','w')
    toFile.write(Utilities().SerializePretty(kml))
    toFile.close()
if __name__ == '__main__':
    main()
