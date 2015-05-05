# Introduction #

This is a basic tutorial on how to take a sample raw data set and create a time stamped and stylish KML file that can be viewed in Google Earth. In order to do this, you will need to have a basic understanding of programming (this tutorial will use Python) If you have experience with programming and do not know python, then you should still pick this up relatively quickly.

# Getting Set Up #

In order to complete this task, we will need to acquire the Pylibkml suite at http://code.google.com/p/pylibkml/. Although this software is still in development, it is stable enough to produce high quality .kml files with raw data sets. As of the date this tutorial was published, this software is available only through a Mercurial repository. Put the pylibkml.py file in your python path, and then you should be set. In order for pylibkml, you may need to install other dependencies (libkml and any dependencies it may have.)

Pylibkml is a python wrapper to another open source software set called “libkml.” Libkml is primarily written in C, which can be fairly difficult to work with. Python, being a bit more user friendly and easier to learn, seems like a more suitable language to teach scientists and other non-programmers. Pylibkml allows for a script based program to easily create KML objects/files (to help manage all of the KML syntax.)

# Handling Raw Data in Python #

Although this process will depend on the type of data you have (format, style, ordering, etc.); after learning to do this once, it is easy to adapt your program to handle the dataset that you have. The dataset used for this tutorial is a .csv (comma separated values) formatted file that can be downloaded at http://earthquake.usgs.gov/eqcenter/catalogs/eqs7day-M1.txt. For future reference, if you have your own dataset in Microsoft Excel, you can “Save As” a .csv file so that you can easily process the data.

After you have the dataset, it is now time to write a program that can easily process the data. First, look at the .csv file and figure out what information you would like to have in your .kml file. In this case, I have chosen to use everything except for the columns labeled “Src” and “Version.” We will have our python program start off by pulling out all necessary data and storing them in something called a list (equivalent to an array.) Our initial script will look something like this:

```
from pylibkml import Kml,Utilities
from csv import reader
def main():
    inputfile = reader(file('eqs7day-M1.csv','r'), delimiter=',')
    inputfile.next() # Get rid of the header information
    Eqid = [];DateTime = [];Lat=[];Lon=[];Magnitude=[];
    Depth=[];NST=[];Location=[]
    for line in inputfile:
        Eqid.append(line[1])
        DateTime.append(line[3])
        Lat.append(line[4])
        Lon.append(line[5])
        Magnitude.append(line[6])
        Depth.append(line[7])
        NST.append(line[8])
        Location.append(line[9]) 
if __name__ == '__main__':
    main()
```

What is happening here is the reader() function grabs the .csv file and turns every line into a list of data separated by a delimiter (which in this case is a comma.) The next line of code skips the header in the .csv file allowing it to move on to the actual data that we want. The next python line initializes the lists (i.e. “Eqid = `[]`” symbolizes the earthquake ID) which is where all of the data will be placed. We then loop through the .csv file and grab all of the data to append (or place at the end) to these lists.

At this point, the data is stored properly in these lists and can be accessed throughout the duration of the program.

# Basic `<Placemark>` Creation #

Now that we have all of the data stored, we will begin building basic `<Placemark>` objects for our .kml file. A `<Placemark>` is the part of the .kml file that contains all of the data (style-id, geometry, location, etc.) To do this, add the following lines:

```
from pylibkml import Kml,Utilities
from csv import reader
from string import atof 
def main():
    inputfile = reader(file('eqs7day-M1.csv','r'), delimiter=',')
    inputfile.next() # Get rid of the header information
    Eqid = [];DateTime = [];Lat=[];Lon=[];Magnitude=[];
          Depth=[];NST=[];Location=[]
    for line in inputfile:
        Eqid.append(line[1])
        DateTime.append(line[3])
        Lat.append(line[4])
        Lon.append(line[5])
        Magnitude.append(line[6])
        Depth.append(line[7])
        NST.append(line[8])
        Location.append(line[9]) 
    placemark = []
    for i in range(0,len(Lat)):
        coordinate = Kml().create_coordinates(atof(Lon[i]),atof(Lat[i]))
        point = Kml().create_point({'coordinates':coordinate})
        placemark.append(Kml().create_placemark({‘name’: Eqid[i],
                                                 'point':point}))
if __name__ == '__main__':
    main()
```

This part loops through all of the coordinate values and creates a `<Placemark>` at the latitude and longitude values we extracted from our .csv file. To do this, we had to create a `<coordinate>` object and add this to the `<Point>` object. After this, we can add our `<Point>` to our `<Placemark>`. We will be adding several other things to our `<Placemark>` throughout the tutorial.

# Creating a `<TimeStamp>` for our `<Placemark>` #

The next step is to assign a time and date for all of our `<Placemark>` objects. The time and date entry we stored in the list named `"DateTime"` is currently in ISO format, and we need to parse it into a format appropriate for KML. Although there are several formats for these time primitive objects (see the full list at http://code.google.com/apis/kml/documentation/kmlreference.html#timeprimitive), we are going to use the “YYYY-MM-DDTHH:MM:SSZ” format. For example, one of the entries in the `"DateTime"` list reads:

“Thursday, August  6, 2009 18:52:36 UTC”

In KML, this translates into:

“2009-08-06T18:52:36Z”

To perform this conversion, I have written a small function in python to be included with the program. It is heavily commented (lines that start with '#' are comments) so that you can understand what is going on line by line:

```
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
```

In future programs, you will have to write similar functions, so it is important to understand what everything is doing. In order for this function to work, you will need to amend one of the import lines at the top of the program to read `from string import atof,replace` so that you can use the replace() function in the string class.

Now, we are ready to create the `<TimeStamp>` object. In the lines of code below, add the lines in green:
```
timestamp = Kml().create_timestamp({'when':process_datetime(DateTime[i])})
placemark.append(Kml().create_placemark({'name':Eqid[i],
                                         'point':point,
                                         'timestamp':timestamp}))
```

# Creating `<Style>` Objects #

Now we will make our data look more appealing in the Google Earth software. This is something that we can do with the `<Style>` tags and its associated sub-styles (`<BalloonStyle>`, `<ListStyle>`, `<LineStyle>`, `<PolyStyle>`, `<IconStyle>`, and `<LabelStyle>`.) In this tutorial, we will deal with the `<BalloonStyle>` and `<IconStyle>`. These sub-styles all go into a `<Style>` tag and link with the `<Placemark>` objects using its `<styleUrl>` attribute. This way, you can have multiple styles if desired (just assign other placemarks different `<styleUrl>` tags.)

The `<IconStyle>` gives the individual `<Placemark>` objects their color, size, and image attributes. In this tutorial, we are going to represent each earthquake as a little red dot. First of all, we create the `<Icon>` and assign it to the `<IconStyle>` as follows:
```
icon_href = 'http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
iconstyleicon = Kml().create_iconstyleicon({'href': icon_href})
iconstyle = Kml().create_iconstyle({'color':'ff0400ff',
                                    'scale' : 1.2,
                                    'colormode': 'normal',
                                    'icon':iconstyleicon})
```
The 'iconstyleicon' variable is the `<Icon>` that is passed to the `<IconStyle>` object. The 'href' attribute can be any link to an image online or in your local file directory. In the create\_iconstyle() function, we assign it a size (scale) and a color.

NOTE: The KML color scheme follows the “AABBGGRR” format [4](4.md) where each value is a hexadecimal color code. Each AA, BB, GG, and RR are within the range of (00-FF) where AA is the extent of opacity (transparency) and BB, GG, and RR are blue, green, and red (respectively.) Be aware that this is different than the HTML “RRGGBB” format. In the case of this `<IconStyle>`, ff0400ff has max opacity with the max red intensity value selected (and just a hint of blue.)

Now, the `<BalloonStyle>` can be a bit more complicated and requires a basic knowledge of HTML because the pop-up balloon is styled via HTML syntax (so you could create an entire webpage inside a `<BalloonStyle>`…with certain limitations) In this tutorial, we will make a simple table displaying all relevant data in a html <table> format. The sample <code>&lt;BalloonStyle&gt;</code> generated for the tutorial is shown below:<br>
<pre><code>balloon_txt = '&lt;![CDATA[&lt;BODY bgcolor="ff0004"&gt;\n&lt;h3&gt;USGS Earthquake Data'+\<br>
      '&lt;TABLE BORDER=1&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Earthquake ID&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[eqid]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Date/Time&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[datetime]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Latitude,Longitude&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[lat],$[lon]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Magnitude&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[magnitude]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Depth&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[depth]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;NST&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[nst]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;tr&gt;&lt;td&gt;&lt;b&gt;Location&lt;/b&gt;&lt;/td&gt;&lt;td&gt;$[location]&lt;/td&gt;&lt;/tr&gt;\n'+\<br>
      '&lt;/TABLE&gt;&lt;/BODY&gt;]]&gt;'<br>
balloonstyle = Kml().create_balloonstyle({'text':balloon_txt,<br>
					  'bgcolor':'ff0400ff'})<br>
</code></pre>
The variable “balloon_txt” contains the HTML code required to generate a small table of entries. As you can see, there is a row for each set of data we collected earlier in the tutorial. The part that requires a bit of explaining is that the values are written as <code>$[something].</code> These variables will pull from an element called <code>&lt;ExtendedData&gt;</code> which we will talk about in the next section. For now, just understand that this will automatically pull the appropriate piece of data and put it in the <code>&lt;BalloonStyle&gt;</code> for you.<br>
<br>
Now as we have finished creating the two sub-styles, we will add them to a <code>&lt;Style&gt;</code> tag. This is simply done by:<br>
<pre><code>style = Kml().create_style({'id':'primary-style',<br>
                            'balloonstyle':balloonstyle,<br>
                            'iconstyle':iconstyle})<br>
</code></pre>
And modifying the placemark attribute:<br>
<pre><code>placemark.append(Kml().create_placemark({'name':Eqid[i],<br>
                                         'point':point,<br>
                                         'timestamp':timestamp,<br>
                                         'styleurl':'#primary-style'}))<br>
</code></pre>
The <code>&lt;styleUrl&gt;</code> value in the <code>&lt;Placemark&gt;</code> and the <code>&lt;Style id=””&gt;</code> need to match. The only think different is that the <code>&lt;styleUrl&gt;</code> will have a ‘#’ at the beginning. Your <code>&lt;Placemark&gt;</code> objects are all now perfectly styled.<br>
<br>
<h1><code>&lt;Data&gt;</code> and <code>&lt;ExtendedData&gt;</code></h1>

Elements in the <code>&lt;Data&gt;</code> tag contain the name and value of a particular piece of data related to the <code>&lt;Placemark&gt;</code>. The <code>&lt;name&gt;</code> of the <code>&lt;Data&gt;</code> and the <code>$[whatever]</code> in the <code>&lt;BalloonStyle&gt;</code> need to match up in order for it to show up in Google Earth properly. All of the sets of <code>&lt;Data&gt;</code> (in the case of this tutorial, there are eight data sets per <code>&lt;Placemark&gt;</code>) wrap-up in an <code>&lt;ExtendedData&gt;</code> object. In the data set for the tutorial, we are able to build these tags by:<br>
<br>
<pre><code>data = []<br>
data.append(Kml().create_data({'name':'eqid','value':Eqid[i]}))<br>
data.append(Kml().create_data({'name':'datetime','value':DateTime[i]}))<br>
data.append(Kml().create_data({'name':'lat','value':Lat[i]}))<br>
data.append(Kml().create_data({'name':'lon','value':Lon[i]}))<br>
data.append(Kml().create_data({'name':'mag','value':Magnitude[i]}))<br>
data.append(Kml().create_data({'name':'depth','value':Depth[i]})) data.append(Kml().create_data({'name':'nst','value':NST[i]})) data.append(Kml().create_data({'name':'location','value':Location[i]})) extendeddata = Kml().create_extendeddata({'data':data})<br>
placemark.append(Kml().create_placemark({'name':Eqid[i],<br>
                        'point':point,<br>
                        'timestamp':timestamp,<br>
                        'extendeddata':extendeddata,<br>
                        'styleurl':'#primary-style'}))<br>
</code></pre>
Although this will make your KML file more interesting, it will also take up a lot more space (in terms of disk space.)<br>
<br>
<h1>Building the KML File and Viewing it in Google Earth</h1>

It is almost time to see what all of your hard work has accomplished. Just a few lines of code remain to develop the finished product. Add the following lines to the bottom of the main method to finish the product:<br>
<pre><code>folder = Kml().create_folder({'name':'USGS Earthquakes',<br>
                              'placemark':placemark})<br>
document = Kml().create_document({'folder':folder,<br>
                                  'style':style})<br>
kml = Kml().create_kml({'document':document})<br>
toFile = open('tutorial.kml','w')<br>
toFile.write(Utilities().SerializePretty(kml))<br>
toFile.close()<br>
</code></pre>
The first line of code puts all of your <code>&lt;Placemark&gt;</code> objects into a <code>&lt;Folder&gt;</code> named 'USGS Earthquakes.' This <code>&lt;Folder&gt;</code> and the <code>&lt;Style&gt;</code> that you created are placed into a <code>&lt;Document&gt;</code> object which is then put into a <code>&lt;Kml&gt;</code> object. The last step, which the last three lines do, is to write the <code>&lt;Kml&gt;</code> object to a file named 'tutorial.kml.' The <code>Utilities().SerializePretty()</code> function turns the entire <code>&lt;Kml&gt;</code> object into text so it can be written to the file. (See the attached file <a href='http://pylibkml.googlecode.com/hg/src/docs/test.py'>test.py</a> for the complete and documented program.) Now you can view your .kml file in Google Earth.<br>
<br>
<h1>Viewing in Google Earth</h1>

After you have run this program, in the same directory, there will be a file called ‘tutorial.kml’ that you should open up in Google Earth. When you first open the program, you will notice that nothing is on your globe. This is because the data is time-stamped. In the upper-left hand side of the globe is a timeline tool bar. As you adjust it, little red dots will start to appear all over the world.<br>
<br>
<img src='http://pylibkml.googlecode.com/hg/src/docs/alaska.jpg' width='650' height='450' /><br />
<i><b>Figure 1 – Every red dot is an earthquake detection.</b></i>

The number next to each particular dot is the <code>&lt;name&gt;</code> attribute assigned to each <code>&lt;Placemark&gt;</code>. In this case, it is the earthquake id number. You could modify it to be anything you like. Now, zoom in on a particular <code>&lt;Placemark&gt;</code> and click on the red dot. The <code>&lt;BalloonStyle&gt;</code> will spring to action and you will see all of the data for that particular earthquake.<br>
<br>
<img src='http://pylibkml.googlecode.com/hg/src/docs/balloon.png' width='650' height='450' /><br />
<i><b>Figure 2 – A <code>&lt;BalloonStyle&gt;</code> for a particular earthquake</b></i>

<h1>What Pylibkml Created – Understanding KML</h1>
To properly understand the KML syntax, I will give a brief explanation on how KML operates. For the most part, it works a lot like HTML (in the sense it has opening and closing tags that represent different objects.) The following is one of the earthquake <code>&lt;Placemark&gt;</code> objects in KML tagging format:<br>
<pre><code>    &lt;Placemark&gt;<br>
      &lt;name&gt;14496640&lt;/name&gt;<br>
      &lt;TimeStamp&gt;<br>
        &lt;when&gt;2009-08-06T18:04:46Z&lt;/when&gt;<br>
      &lt;/TimeStamp&gt;<br>
      &lt;styleUrl&gt;#primary-style&lt;/styleUrl&gt;<br>
      &lt;ExtendedData&gt;<br>
        &lt;Data name="eqid"&gt;<br>
          &lt;value&gt;14496640&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="datetime"&gt;<br>
          &lt;value&gt;Thursday, August  6, 2009 18:04:46 UTC&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="lat"&gt;<br>
          &lt;value&gt;33.3483&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="lon"&gt;<br>
          &lt;value&gt;-115.6995&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="mag"&gt;<br>
          &lt;value&gt;1.5&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="depth"&gt;<br>
          &lt;value&gt;9.90&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="nst"&gt;<br>
          &lt;value&gt;35&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
        &lt;Data name="location"&gt;<br>
          &lt;value&gt;Southern California&lt;/value&gt;<br>
        &lt;/Data&gt;<br>
      &lt;/ExtendedData&gt;<br>
      &lt;Point&gt;<br>
        &lt;coordinates&gt;<br>
          -115.6995,33.3483,0<br>
        &lt;/coordinates&gt;<br>
      &lt;/Point&gt;<br>
    &lt;/Placemark&gt;<br>
</code></pre>
As can be seen, the <code>&lt;Placemark&gt;</code> tag has attributes such as <code>&lt;name&gt;</code>, <code>&lt;TimeStamp&gt;</code>, etc. Some of these attributes have attributes of their own. This is apparent in the case of <code>&lt;TimeStamp&gt;</code> that has the <code>&lt;when&gt;</code> attribute which describes when that particular earthquake occurred. All of these placemarks, as seen in the software, are in a <code>&lt;Folder&gt;</code> object. To see all of the possible KML tags, geometries, styles, attributes, etc., then visit <a href='http://code.google.com/apis/kml/documentation/kmlreference.html'>http://code.google.com/apis/kml/documentation/kmlreference.html</a> for a comprehensive list. On this site, it gives examples of how each element is used and where exactly each element goes.<br>
<br>
<h1>Creating Software that Automatically Pulls Data From Online</h1>
It is extremely aggravating when you have to constantly go to the website, download the file, and reload the data into your directory to run it. You can add a few lines of code to get your code to automatically download the file and save it in your working directory while it is building your .kml file. First of all, you will need to add <code>import urllib2</code> to your list of libraries that you would like to use. Then, at the beginning of your main method, add and modify the following lines:<br>
<pre><code>url = 'http://earthquake.usgs.gov/eqcenter/catalogs/eqs7day-M1.txt'<br>
    webFile = urllib2.urlopen(url)<br>
    localFile = open(url.split('/')[-1], 'w')<br>
    localFile.write(webFile.read())<br>
    webFile.close()<br>
    localFile.close()<br>
    inputfile = reader(file(url.split('/')[-1]), delimiter=',')<br>
</code></pre>
This code will grab whatever is at that url, save the file, and load it as the working data set as before. This just saves you the time of going online and loading it yourself.<br>
<br>
<h1>Working with Geometries other than <code>&lt;Point&gt;</code></h1>
There are a few other types of Geometry objects such as <code>&lt;LineString&gt;</code>, <code>&lt;LinearRing&gt;</code>, <code>&lt;Polygon&gt;</code>, <code>&lt;MultiGeometry&gt;</code>, and <code>&lt;Model&gt;</code>. Here are a few examples on how a couple of these work.<br>
<br>
If we wanted to create a doughnut shaped <code>&lt;Polygon&gt;</code>, we would created two <code>&lt;LinearRing&gt;</code> objects and place one inside the other like so:<br>
<pre><code> #Demonstrating a Doughnut shaped Polygon<br>
    coord_out = [(-122.366278,37.818844,30),<br>
            (-122.365248,37.819267,30),<br>
            (-122.365640,37.819861,30),<br>
            (-122.366669,37.819429,30),<br>
            (-122.366278,37.818844,30)]<br>
    coord_out = Kml().create_coordinates(coord_out)<br>
    outer_ring = Kml().create_linearring({'coordinates':coord_out})<br>
    outerboundary = Kml().create_outerboundaryis({'linearring':outer_ring})<br>
    coord_in = [(-122.366212,37.818977,30),<br>
            (-122.365424,37.819294,30),<br>
            (-122.365704,37.819731,30),<br>
            (-122.366488,37.819402,30),<br>
            (-122.366212,37.818977,30)]<br>
    coord_in = Kml().create_coordinates(coord_in)<br>
    inner_ring = Kml().create_linearring({'coordinates':coord_in})<br>
    innerboundary = Kml().create_innerboundaryis({'linearring':inner_ring})<br>
    polygon = Kml().create_polygon({'extrude':1,<br>
                                    'altitudemode':'relativetoground',<br>
                                    'innerboundaryis':innerboundary,<br>
                                    'outerboundaryis':outerboundary})<br>
    placemark = Kml().create_placemark({'name':'Sample Doughnut Polygon',<br>
                                        'polygon':polygon,<br>
                                        'styleurl':'#poly-style'})<br>
    folder.append(Kml().create_folder({'name':'Sample Polygons',<br>
                                        'placemark':placemark}))<br>
    #&lt;Style&gt; for the &lt;Polygon&gt; demonstration<br>
    polystyle = Kml().create_polystyle({'color':'ffff0000',<br>
                                        'fill':1,<br>
                                        'outline':1})<br>
    style.append(Kml().create_style({'id':'poly-style',<br>
                                        'polystyle':polystyle}))<br>
</code></pre>
This obviously makes the assumption that the style and folder variables have been turned into list types in order to allow for multiple folders and styles. Adding the code results in the following <code>&lt;Polygon&gt;</code>:<br>
<br>
<img src='http://pylibkml.googlecode.com/hg/src/docs/blue_poly.jpg' width='650' height='450' /><br />
<i><b>Figure 3 - The doughnut type polygon demonstration</b></i>

If we wanted to make this one tall solid polygon, we would just remove the <code>&lt;InnerBoundary&gt;</code> object. Also, you can have multiple <code>&lt;InnerBoundary&gt;</code> objects within the <code>&lt;OuterBoundary&gt;</code>. One other important thing to mention is the extrusion of the <code>&lt;Polygon&gt;</code>. If you add altitude to the <code>&lt;coordinate&gt;</code> object and set <code>&lt;extrude&gt;</code> to 1 as done in this example, you can get any geometry to stick out.