# Introduction #

This is a sample program grabbing a simple RSS feed and using it to automatically update the data in the KML file. To see the full source code, download it at [rssfeed.py](http://pylibkml.googlecode.com/hg/src/docs/rssfeed.py).


# Getting Started #
This tutorial will assume you went through the BasicTutorial on the Wiki of this page. If not, start there because we will not go through as of detail as before.

In comparison, this is a much smaller and simpler example that will builds off what we have already learned. Like before, the hardest part is trying to figure out how to parse the data (it isn't a neat .csv file like before.) The current data set is a [Parking RSS Feed - Ann Arbor](http://a2dda.org/parking-rss.php). It keeps a live update of how many parking spots are available in the parking complexes in Ann Arbor, MI. The RSS feed data looks like:

```
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>Parking Feed - Ann Arbor Downtown Development Authority</title>
    <link>http://a2dda.org/</link>
    <atom:link href="http://a2dda.org/parking-rss.php" rel="self" type="application/rss+xml" />
    <description>Parking Feed for the Ann Arbor Downtown Development Authority</description>
    <language>en-us</language>
    <item>
        <title>Ann and Ashley</title>
        <link>http://a2dda.org/downloads/Parking/AnnAshley.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 311</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=1</guid>
    </item>
    <item>
        <title>4th and William</title>
        <link>http://a2dda.org/downloads/Parking/4thWilliam.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 312</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=2</guid>
    </item>
    <item>
        <title>Forest</title>
        <link>http://a2dda.org/downloads/Parking/Forest.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 181</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=3</guid>
    </item>
    <item>
        <title>4th and Washington</title>
        <link>http://a2dda.org/downloads/Parking/4thWashington.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 81</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=4</guid>
    </item>
    <item>
        <title>Maynard</title>
        <link>http://a2dda.org/downloads/Parking/Maynard.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 215</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=5</guid>
    </item>
    <item>
        <title>Library Lot</title>
        <link>http://a2dda.org/downloads/Parking/LibraryLot.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 55</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=6</guid>
    </item>
    <item>
        <title>First and Huron</title>
        <link>http://a2dda.org/downloads/Parking/FirstHuron.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 59</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=7</guid>
    </item>
    <item>
        <title>South Ashley</title>
        <link>http://a2dda.org/downloads/Parking/SouthAshley.pdf</link>
        <pubDate>Mon, 10 Aug 09 15:22:05 -0400</pubDate>
        <description> 66</description>
        <category>Parking</category>
        <guid isPermaLink="false">/parking-rss.php?id=8</guid>
    </item>
</channel>
</rss>
```

In each one of the `<item>` objects, there are six different data sets for the parking structure. To make this simple, we are only going to concern ourselves with the `<title>` and the `<description>` (contains the available number of spots) objects. The following code will parse through the RSS feed data and store it into two lists (one for the name of the parking complex and the second containing the number of parking spaces available):

```
def main():
    url = 'http://a2dda.org/parking-rss.php'
    webFile = urllib2.urlopen(url)
    site_strings = webFile.readlines()
    webFile.close()
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

if __name__ == '__main__':
    main()
```

Essentially, this code is going line by line and seeing if the tags we want exist that line. If it doesn't, we move on. If the tag exists, we pull the line apart and remove all unnecessary information from it. When we peeled everything away except for the data, we push that onto the list.

The next block of code takes this data and turns it into the `<Placemark>` objects. The difference between this tutorial and the BasicTutorial is that we have to build a `<Style>` for each `<Placemark>`. Therefore, we have to carefully line each `<Placemark>` `<styleUrl>` and `<Style>` `<id>`. First of all, we need to predefine all Latitude,Longitude placements and the max capacities for all parking structures:

```
latlon = [[42.282299,-83.749086],[42.278461,-83.747741],[42.274165,-83.733802],
          [42.280579,-83.747749],[42.278669,-83.742378],[42.280275,-83.742815],
          [42.278380,-83.746108],[42.281423,-83.749745],[42.278638,-83.749451]]
parking = ['Ann and Ashley', '4th and William', 'Forest', '4th and Washington',
'Maynard','Liberty Square', 'Library Lot', 'First and Huron', 'South Ashley']
capacities = [789,947,834,272,770,573,186,162,128]
```

We need to predefine these values because the data doesn't exist in the RSS feed. We also predefine the `parking` structures names because there are times where extra parking structures' get added and other times where some disappear. These nine structures are every possible data set, but we keep track of them because we don't necessarily know the order. All of the data is respective; that is, they all line up (i.e. Ann and Ashley are located at 42.282299,-83.749086 and have a max capacity of 789.) Next, we build all of the `<Placemark>` and `<Style>` objects:

```
placemark = [];style=[];
    for i in range(0,len(title)):
        cap = capacities[parking.index(title[i])]
        lat,lng = latlon[parking.index(title[i])]
        title_str = title[i]+'\n '+str(description[i])+'/'+str(cap)
        coordinate = Kml().create_coordinates(lng,lat)
        point = Kml().create_point({'coordinates':coordinate})
        placemark.append(Kml().create_placemark({'name':title_str,
                                                'point':point,
                                                'styleurl':'#style-'+title[i],
                                                }))
        icon = Kml().create_iconstyleicon({'href':'http://chart.apis.google.com/'
            +'chart?'
            +'cht=gom'
            +'&chs=225x125'
            +'&chd=t:'+str(((cap-description[i])*100)/cap)
            +'&chco=00FF00,FFFF00,FF0000'
            +'&chf=bg,s,FFFFFF00'
            })

        iconstyle = Kml().create_iconstyle({'icon':icon,
            'scale':1.5})
        style.append(Kml().create_style({'id':'style-'+title[i],
                                            'iconstyle':iconstyle}))
```

We use the `parking.index(title[i](i.md)) to identify the location of the parking structure so that we can match it with the capacity and location.

The next important thing to note is the `'styleurl':'#style-'+title[i]` line. We are making custom `<styleUrl>` tags for each `<Placemark>` and making them unique by adding the name into the url.

The next important part to explain is:
```
        icon = Kml().create_iconstyleicon({'href':'http://chart.apis.google.com/'
            +'chart?'
            +'cht=gom'
            +'&chs=225x125'
            +'&chd=t:'+str(((cap-description[i])*100)/cap)
            +'&chco=00FF00,FFFF00,FF0000'
            +'&chf=bg,s,FFFFFF00'
            })
```

This is using the [Google Chart Application](http://code.google.com/apis/chart/). The chart chosen will be a custom made gauge that will help illustrate (on the icon) how many parking spaces are available. This chart is built by modifying the query string and changing the values. The `cht=gom` argument makes this a Google-O-Meter. The `&chs=225x125` argument makes this png image 225 by 125 pixels. The `&chd=t:'+str(((cap-description[i])*100)/cap)` argument needs to be in the range of 0-100 (a percentage of the max capacity in this case.) The `&chco=00FF00,FFFF00,FF0000` argument makes the color scheme run from green to yellow to red (as it travels down the gauge.) Finally, the `&chf=bg,s,FFFFFF00` argument makes the background look opaque (so it looks nice.)

The final image looks a little something like this:<br />
![http://chart.apis.google.com/chart?cht=gom&chs=225x125&chd=t:70&chco=00FF00,FFFF00,FF0000&chf=bg,s,FFFFFF00.png](http://chart.apis.google.com/chart?cht=gom&chs=225x125&chd=t:70&chco=00FF00,FFFF00,FF0000&chf=bg,s,FFFFFF00.png)<br />
_**Figure 1 - Sample Meter from Google Charts**_

The last bit of code creates the kml file just like the BasicTutorial:
```
    folder = Kml().create_folder({'name':'Ann Arbor Parking Structures',
                                  'placemark':placemark})
    document = Kml().create_document({'folder':folder,
                                      'style':style})
    kml = Kml().create_kml({'document':document})
    toFile = open('rss_tutorial.kml','w')
    toFile.write(Utilities().SerializePretty(kml))
    toFile.close()
```

A sample output looks like:

<img src='http://pylibkml.googlecode.com/hg/src/docs/parking.jpg' width='650' height='450' /><br />
_**Figure 2 – Sample Output**_