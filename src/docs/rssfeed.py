import urllib2
from string import replace,atoi
from pylibkml import Kml,Utilities

#Predefine location, names, and capacities of all parking garages
#This data is respective to each other (they line up.)
latlon = [[42.282299,-83.749086],[42.278461,-83.747741],[42.274165,-83.733802],
          [42.280579,-83.747749],[42.278669,-83.742378],[42.280275,-83.742815],
          [42.278380,-83.746108],[42.281423,-83.749745],[42.278638,-83.749451]]
parking = ['Ann and Ashley', '4th and William', 'Forest', '4th and Washington',
'Maynard','Liberty Square', 'Library Lot', 'First and Huron', 'South Ashley']
capacities = [789,947,834,272,770,573,186,162,128]

def main():
    #Define the location of the rss feed
    url = 'http://a2dda.org/parking-rss.php'
    #Grab the RSS feed
    webFile = urllib2.urlopen(url)
    #Process all of the lines in the feed and put them into a list
    site_strings = webFile.readlines()
    #Close the RSS feed
    webFile.close()
    #Grab out the titles and number of cars in each complex
    title = [];description=[];
    for i in range(0,len(site_strings)):
        if site_strings[i].count('\t\t<title>')>0:
            site_strings[i] = replace(site_strings[i],'\t\t<title>','')
            site_strings[i] = replace(site_strings[i],'</title>\n','')
            if parking.index(site_strings[i])>-1:
                title.append(site_strings[i])
            else:
                print 'Error -> '+site_strings[i]
        elif site_strings[i].count('\t\t<description>')>0:
            site_strings[i] = replace(site_strings[i],'\t\t<description> ','')
            site_strings[i] = replace(site_strings[i],'</description>\n','')
            description.append(atoi(site_strings[i]))

    placemark = [];style=[];
    for i in range(0,len(title)):
        #Find the max capacity of the parking structure
        cap = capacities[parking.index(title[i])]
        #Find the location of the parking structure
        lat,lng = latlon[parking.index(title[i])]
        #Define the <Placemark> title
        title_str = title[i]+'\n '+str(description[i])+'/'+str(cap)
        #Create the <coordinate> object
        coordinate = Kml().create_coordinates(lng,lat)
        #Create the <Point> object
        point = Kml().create_point({'coordinates':coordinate})
        #Create the <Placemark> object
        placemark.append(Kml().create_placemark({'name':title_str,
                                                'point':point,
                                                'styleurl':'#style-'+title[i],
                                                }))
        #Make the <Icon> use a "Google-o-Meter" to display capacity
        icon = Kml().create_iconstyleicon({'href':'http://chart.apis.google.com/'
            +'chart?'
            +'cht=gom'
            +'&chs=225x125'
            +'&chd=t:'+str(((cap-description[i])*100)/cap)
            +'&chco=00FF00,FFFF00,FF0000'
            +'&chf=bg,s,FFFFFF00'
            })
        #Create the <IconStyle>
        iconstyle = Kml().create_iconstyle({'icon':icon,
            'scale':1.5})
        #Create the <Style>
        style.append(Kml().create_style({'id':'style-'+title[i],
                                            'iconstyle':iconstyle}))
    #Create the <Folder> object
    folder = Kml().create_folder({'name':'Ann Arbor Parking Structures',
                                    'placemark':placemark})

    #Put everything in a <Document> object
    document = Kml().create_document({'folder':folder,
                                        'style':style})
    #Create the final <Kml> object
    kml = Kml().create_kml({'document':document})
    #Write the Kml object to tutorial.kml
    toFile = open('rss_tutorial.kml','w')
    toFile.write(Utilities().SerializePretty(kml))
    toFile.close()
if __name__ == '__main__':
    main()
