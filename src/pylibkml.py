# -*- coding: utf-8 -*-
################################################################################
#  pylibkml
#  Copyright (C) 2009  Tyler Erickson <tylerickson@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the accompanying LICENSE.txt file.
#
#  Thanks to anyone who does anything for this project.
################################################################################
"""
pylibkml - Python helper class for libkml

The wrapper can assist in generating KML objects in Python. 

Dependencies:
    libkml - Google's library for parsing, generating, and operating on KML
    http://code.google.com/p/libkml/

Example Usage:
    import kmldom
    import pylibkml
    folder = pylibkml.Kml().create_folder({'name' : 'Sample Folder',})
    kmldom.SerializeRaw(folder)
    
    See tests.py for unit test and other examples
"""
__version__ = 0.1

from types import *
import string
from string import *
import zipfile

try:
    import kmldom
    import kmlbase
except ImportError:
    logging.error('Unable to import libkml modules')

factory = kmldom.KmlFactory_GetFactory()

class Kml():
    """
    Abstract class for all KML object operations
    """
    def __init__(self):
        self = factory.CreateKml()

    """ --------------------------------------------------------------
    <AbstractView> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#abstractview
    """
    def process_abstractview_attributes(self,abstractview,params={}):
    
        abstractview = self.process_object_attributes(abstractview,params)
        
        for key in params:
            if key == 'gxtimestamp' or key == 'gxtimespan':
                abstractview.set_gx_timeprimitive(params[key])
        return abstractview

    """ --------------------------------------------------------------
    <Alias> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#alias
    """
    def create_alias(self,params={}):
    
        alias = factory.CreateAlias()
        alias = self.process_geometry_attributes(alias,params)
        
        for key in params:
            if key == 'sourcehref':
                alias.set_sourcehref(params[key])
            elif key == 'targethref':
                alias.set_targethref(params[key])
        return alias
        
    """ --------------------------------------------------------------
    <atom:Author> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#atomauthor
    """
    def create_atomauthor(self,params={}):
        atomauthor = factory.CreateAtomAuthor()
        atomauthor = self.process_object_attributes(atomauthor,params)
        
        for key in params:
            if key == 'uri':
                atomauthor.set_uri(params[key])
            elif key == 'email':
                atomauthor.set_email(params[key])
            elif key == 'name':
                atomauthor.set_name(params[key])
        return atomauthor  
    
    """ --------------------------------------------------------------
    <atom:Link> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#atomlink
    """
    def create_atomlink(self,params={}):
        atomlink = factory.CreateAtomLink()
        
        for key in params:
            if key == 'href':
                atomlink.set_href(params[key])
            elif key == 'hreflang':
                atomlink.set_hreflang(params[key])
            elif key == 'length':
                atomlink.set_length(params[key])
            elif key == 'rel':
                atomlink.set_rel(params[key])
            elif key == 'title':
                atomlink.set_title(params[key])
            elif key == 'type':
                atomlink.set_type(params[key])
        return atomlink   
        
    """ --------------------------------------------------------------
    <BalloonStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#balloonstyle
    """
    def create_balloonstyle(self, params = {}):
        
        balloonstyle = factory.CreateBalloonStyle()
        balloonstyle = self.process_colorstyle_attributes(balloonstyle,params)
        
        for key in params:
            if key == 'bgcolor':
                balloonstyle.set_bgcolor(kmlbase.Color32(params[key]))
            elif key == 'textcolor':
                balloonstyle.set_textcolor(kmlbase.Color32(params[key]))
            elif key == 'text':
                balloonstyle.set_text(params[key])
            elif key == 'displaymode':
                if params[key] == 'default':
                    balloonstyle.set_displaymode(kmldom.DISPLAYMODE_DEFAULT)
                elif params[key] == 'hide':
                    balloonstyle.set_displaymode(kmldom.DISPLAYMODE_HIDE)
        return balloonstyle

    """ --------------------------------------------------------------
    <Camera> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#camera
    """
    def create_camera(self,params = {}):
        camera = factory.CreateCamera()
        camera = self.process_abstractview_attributes(camera,params)
        
        for key in params:
            if key == 'longitude':
                camera.set_longitude(params[key])
            elif key == 'latitude':
                camera.set_latitude(params[key])
            elif key == 'altitude':
                camera.set_altitude(params[key])
            elif key == 'heading':
                camera.set_heading(params[key])
            elif key == 'tilt':
                camera.set_tilt(params[key])
            elif key == 'roll':
                camera.set_roll(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    camera.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    camera.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    camera.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    camera.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    camera.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
        return camera

    """ --------------------------------------------------------------
    <Change> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#change
    """
    def create_change(self,params={}):
        change = factory.CreateChange()
        
        for key in params:
                change.add_object(params[key])
        return change

    """ --------------------------------------------------------------
    <ColorStyle> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#colorstyle
    """        
    def process_colorstyle_attributes(self, colorstyle, params):
    
        colorstyle = self.process_object_attributes(colorstyle, params)

        for key in params:
            if key == 'color':
                colorstyle.set_color(kmlbase.Color32(params[key]))
            elif key == 'colormode':
                if params[key] == 'normal':
                    colorstyle.set_colormode(kmldom.COLORMODE_NORMAL)
                elif params[key] == 'random':
                    colorstyle.set_colormode(kmldom.COLORMODE_RANDOM)
                else:
                    colorstyle.set_colormode(params[key])
                
        return colorstyle

    """ --------------------------------------------------------------
    <Container> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#container
    """
    def process_container_attributes(self, container, params, docflag=0):

        container = self.process_feature_attributes(container, params, docflag)

        for key in params:
            if key == 'folder' or key == 'document' or key == 'photooverlay' or key == 'screenoverlay' or key == 'groundoverlay' or key == 'placemark' or key == 'networklink' or key == 'gxtour':
                if isinstance(params[key],list):
                    for feature in params[key]:
                        container.add_feature(feature)
                else:
                    container.add_feature(params[key])

        return container

    """ --------------------------------------------------------------
    <coordinates> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#coordinates
    """
    def create_coordinates(self, longitude=None, latitude=None, altitude = None, many = []):
    
        coordinates = factory.CreateCoordinates()
        
        if isinstance(longitude,list):
            for key in longitude:
                coordinates.add_latlngalt(key[1],key[0],key[2])
        elif len(many) > 0:
            for key in many:
                coordinates.add_latlngalt(key[1],key[0],key[2])
        elif altitude == None:
            coordinates.add_latlng(latitude, longitude)
        else:
            coordinates.add_latlngalt(latitude, longitude, altitude) 
    
        return coordinates

    """ --------------------------------------------------------------
    <Create> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#create
    """
    def create_create(self,params={}):
        create = factory.CreateCreate()
        
        for key in params:
            if key == 'folder' or key == 'document':
                if isinstance(params[key],list):
                    for x in params[key]:
                        create.add_container(x)
                else:
                    create.add_container(params[key])
        return create

    """ --------------------------------------------------------------
    <Data> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#document
    """
    def create_data(self,params={}):
        data = factory.CreateData()
        for key in params:
            if key == 'name':
                data.set_name(params[key])
            elif key == 'displayname':
                data.set_displayname(params[key])
            elif key == 'value':
                data.set_value(str(params[key]))
        return data
        
    """ --------------------------------------------------------------
    <Delete> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#delete
    """
    def create_delete(self,params={}):
        delete = factory.CreateDelete()
        
        for key in params:
            if key == 'folder' or key == 'document' or key == 'photooverlay' or key == 'screenoverlay' or key == 'groundoverlay' or key == 'placemark' or key == 'networklink' or key == 'gxtour':
                if isinstance(params[key],list):
                    for x in params[key]:
                        delete.add_feature(x)
                else:
                    delete.add_feature(params[key])
        return delete

    """ --------------------------------------------------------------
    <Document> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#document
    """
    def create_document(self, params={}):
    
        document = factory.CreateDocument()

        for key in params:
            if key == 'folder' or key == 'document' or key == 'photooverlay' or key == 'screenoverlay' or key == 'groundoverlay' or key == 'placemark' or key == 'networklink' or key == 'gxtour':
                if isinstance(params[key],list):
                    for x in params[key]:
                        document.add_feature(x)
                else:
                    document.add_feature(params[key])
            elif key == 'schema':
                if isinstance(params[key],list):
                    for x in params[key]:
                        document.add_schema(x)
                else:
                    document.add_schema(params[key])
                    
        document = self.process_container_attributes(document,params,1)
        return document
    """ --------------------------------------------------------------
    <ExtendedData> element 
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#extendeddata
    """
    def create_extendeddata(self,params={}):
        extendeddata = factory.CreateExtendedData()
        
        for key in params:
            if key == 'data':
                if isinstance(params[key],list):
                    for x in params[key]:
                        extendeddata.add_data(x)
                else:
                    extendeddata.add_data(params[key]) 
            elif key == 'schemadata':
                if isinstance(params[key],list):
                    for x in params[key]:
                        extendeddata.add_schemadata(x)
                else:
                    extendeddata.add_schemadata(params[key])
                    
        return extendeddata

    """ --------------------------------------------------------------
    <Feature> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#feature
    """
    def process_feature_attributes(self, feature, params, docflag=0):
        """
        Processes the attributes that are part of the abstract feature element
        """
        feature = self.process_object_attributes(feature, params)  
        for key in params:
            if key == 'name':
                feature.set_name(params[key])
            elif key == 'visibility':
                feature.set_visibility(params[key])
            elif key == 'open':
                feature.set_open(params[key])
            elif key == 'address':
                feature.set_address(params[key])
            elif key == 'phonenumber':
                feature.set_phonenumber(params[key])
            elif key == 'snippet':
                feature.set_snippet(params[key])
            elif key == 'description':
                feature.set_description(params[key].encode())
            elif key == 'lookat' or key == 'camera':
                feature.set_abstractview(params[key])
            elif (key == 'timespan'):
                if type(params[key]) == DictType:
                    timespan = Kml().create_timespan(params[key])
                    feature.set_timeprimitive(timespan)
                else:
                    feature.set_timeprimitive(params[key])
            elif key == 'timestamp':
                if type(params[key]) == DictType:
                    timestamp = Kml().create_timestamp(params[key])
                    feature.set_timeprimitive(timestamp)
                else:
                    feature.set_timeprimitive(params[key])
            elif key == 'styleurl':
                feature.set_styleurl(params[key])
            elif key == 'style' or key == 'stylemap':
                if docflag == 1:
                    if isinstance(params[key],list):
                        for x in params[key]:
                            feature.add_styleselector(x)
                    else:
                        feature.add_styleselector(params[key])
                else:
                    feature.set_styleselector(params[key])
            elif key == 'region':
                feature.set_region(params[key])
            elif key == 'extendeddata':
                feature.set_extendeddata(params[key])
            elif key == 'gxballoonvisibility':
                feature.set_gx_balloonvisibility(params[key])
            elif key == 'atomauthor':
                feature.set_atomauthor(params[key])
            elif key == 'atomlink':
                feature.set_atomlink(params[key])
        return feature

    """ --------------------------------------------------------------
    <Folder> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#folder
    """
    def create_folder(self, params = {} ):
    
        folder = factory.CreateFolder()
        folder = self.process_container_attributes(folder, params)

        for key in params:
            if key == 'folder' or key == 'document' or key == 'photooverlay' or key == 'screenoverlay' or key == 'groundoverlay' or key == 'placemark' or key == 'networklink' or key == 'gxtour':
                if isinstance(params[key],list):
                    for x in params[key]:
                        folder.add_feature(x)
                else:
                    folder.add_feature(params[key])
        return folder
    
    """ --------------------------------------------------------------
    <Geometry> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#geometry
    """
    
    def process_geometry_attributes(self, geometry, params):

        geometry = self.process_object_attributes(geometry, params)
        return geometry

    """ --------------------------------------------------------------
    <GroundOverlay> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#groundoverlay
    """
    def create_groundoverlay(self,params={}):
        groundoverlay = factory.CreateGroundOverlay()
        groundoverlay = self.process_overlay_attributes(groundoverlay,params)
        
        for key in params:
            if key == 'altitude':
                groundoverlay.set_altitude(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    groundoverlay.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    groundoverlay.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    groundoverlay.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    groundoverlay.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    groundoverlay.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'latlonbox':
                groundoverlay.set_latlonbox(params[key])
        return groundoverlay
                
    """ --------------------------------------------------------------
    <gx:AnimatedUpdate> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxanimatedupdate
    """
    def create_gxanimatedupdate(self,params={}):
        gxanimatedupdate = factory.CreateGxAnimatedUpdate()
        gxanimatedupdate = self.process_gxtourprimitive_attributes(gxanimatedupdate,params)
        
        for key in params:
            if key == 'gxduration':
                gxanimatedupdate.set_gx_duration(params[key])
            elif key == 'update':
                gxanimatedupdate.set_update(params[key])
        return gxanimatedupdate

    """--------------------------------------------------------------
    <gx:FlyTo> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxflyto
    """
    def create_gxflyto(self,params={}):
        gxflyto = factory.CreateGxFlyTo()
        gxflyto = self.process_gxtourprimitive_attributes(gxflyto,params)
        
        for key in params:
            if key == 'gxduration' or key == 'duration':
                gxflyto.set_gx_duration(params[key])
            elif key == 'gxflytomode':
                if params[key] == 'bounce':
                    gxflyto.set_gx_flytomode(kmldom.GX_FLYTOMODE_BOUNCE)
                elif params[key] == 'smooth':
                    gxflyto.set_gx_flytomode(kmldom.GX_FLYTOMODE_SMOOTH)
            elif key == 'camera' or key == 'lookat':
                gxflyto.set_abstractview(params[key])
        return gxflyto

    """ --------------------------------------------------------------
    <gx:LatLonQuad> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxlatlonquad
    """
    def create_gxlatlonquad(self,params={}):
        
        gxlatlonquad = factory.CreateGxLatLonQuad()
        gxlatlonquad = self.process_object_attributes(gxlatlonquad,params)
        
        for key in params:
            if key == 'coordinates':
                gxlatlonquad.set_coordinates(params[key])
        return gxlatlonquad

    """ --------------------------------------------------------------
    <gx:PlayList> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxplaylist
    """
    def create_gxplaylist(self, params = {}):
       
        gxplaylist = factory.CreateGxPlaylist()
        gxplaylist = self.process_gxtourprimitive_attributes(gxplaylist,params)

        for key in params:
            if key == 'gxanimatedupdate' or key == 'gxflyto' or key == 'gxtourcontrol' or key == 'gxsoundcue' or key == 'gxwait':
                if isinstance(params[key],list):
                    for x in params[key]:
                        gxplaylist.add_gx_tourprimitive(x)
                else:
                    gxplaylist.add_gx_tourprimitive(params[key])
        return gxplaylist

    """ --------------------------------------------------------------
    <gx:SoundCue> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxsoundcue
    """
    def create_gxsoundcue(self,params={}):
        gxsoundcue = factory.CreateGxSoundCue()
        gxsoundcue = self.process_gxtourprimitive_attributes(gxsoundcue,params={})
        
        for key in params:
            if key == 'href':
                gxsoundcue.set_href(params[key])
        return gxsoundcue
      
    """ --------------------------------------------------------------
    <gx:TimeSpan> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxtimespan
    """
    def create_gxtimespan(self,params={}):
        gxtimespan = factory.CreateGxTimeSpan()
        gxtimespan = self.process_timeprimitive_attributes(gxtimespan,params={})
        
        for key in params:
            if key == 'begin':
                gxtimespan.set_begin(params[key])
            elif key == 'end':
                gxtimespan.set_end(params[key])
        return gxtimespan      
        
    
    """ --------------------------------------------------------------
    <gx:TimeStamp> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxtimestamp
    """  
    def create_gxtimestamp(self, params={}):
        gxtimestamp = factory.CreateGxTimeStamp()
        gxtimestamp = self.process_timeprimitive_attributes(gxtimestamp, params)

        for key in params:
            if key == 'when':
                gxtimestamp.set_when(params[key])
        return gxtimestamp
            
    """ --------------------------------------------------------------
    <gx:Tour> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxtour
    """
    def create_gxtour(self, params = {}):
       
        gxtour = factory.CreateGxTour()
        gxtour = self.process_feature_attributes(gxtour,params)
        
        for key in params:
            if key == 'gxplaylist':
                gxtour.set_gx_playlist(params[key])
        return gxtour

    """ --------------------------------------------------------------
    <gx:TourControl> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxtourcontrol
    """
    def create_gxtourcontrol(self,params={}):
        gxtourcontrol = factory.CreateGxTourControl()
        gxtourcontrol = self.process_gxtourprimitive_attributes(gxtourcontrol,params={})
        
        for key in params:
            if key == 'gxplaymode':
                if params[key] == 'pause':
                    gxtourcontrol.set_gx_playmode(kmldom.GX_PLAYMODE_PAUSE)
        return gxtourcontrol

    """ --------------------------------------------------------------
    <gx:TourPrimitive> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxtourprimitive
    """
    
    def process_gxtourprimitive_attributes(self, gxtourprimitive, params):

        gxtourprimitive = self.process_object_attributes(gxtourprimitive, params)
        return gxtourprimitive
    """ --------------------------------------------------------------
    <gx:Wait> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#gxwait
    """
    def create_gxwait(self,params={}):
        gxwait = factory.CreateGxWait()
        gxwait = self.process_object_attributes(gxwait,params={})
        
        for key in params:
            if key == 'gxduration':
                gxwait.set_gx_duration(params[key])
        return gxwait

    """ --------------------------------------------------------------
    <hotSpot> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#hotspot
    """
    def create_hotspot(self, x, y, xunits, yunits):
    
        hotspot = factory.CreateHotSpot()

        hotspot.set_x(x)
        hotspot.set_y(y)

        if type(xunits) == IntType:
            hotspot.set_xunits(xunits)
        else:
            if xunits == 'fraction':
                hotspot.set_xunits(kmldom.UNITS_FRACTION)
            elif xunits == 'pixels':
                hotspot.set_xunits(kmldom.UNITS_PIXELS)
            elif xunits == 'insetpixels':
                hotspot.set_xunits(kmldom.UNITS_INSETPIXELS)
                
        if type(yunits) == IntType:
            hotspot.set_yunits(yunits)
        else:
            if yunits == 'fraction':
                hotspot.set_yunits(kmldom.UNITS_FRACTION)
            elif yunits == 'pixels':
                hotspot.set_yunits(kmldom.UNITS_PIXELS)
            elif yunits == 'insetpixels':
                hotspot.set_yunits(kmldom.UNITS_INSETPIXELS)    
        return hotspot

    """ --------------------------------------------------------------
    <Icon> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#icon
    """
    def create_icon(self, params = {} ):
    
        icon = factory.CreateIcon()  
        icon = self.process_object_attributes(icon, params)

        for key in params:           
            if key == 'href':
                icon.set_href(params[key])
            elif key == 'refreshmode':
                if params[key] == 'onchange':
                    icon.set_refreshmode(kmldom.REFRESHMODE_ONCHANGE)
                elif params[key] == 'onexpire':
                    icon.set_refreshmode(kmldom.REFRESHMODE_ONEXPIRE)
                elif params[key] == 'oninterval':
                    icon.set_refreshmode(kmldom.REFRESHMODE_ONINTERVAL)
            elif key == 'refreshinterval':
                icon.set_refreshinterval(params[key])
            elif key == 'viewrefreshmode':
                if params[key] == 'never':
                    icon.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_NEVER)
                elif params[key] == 'onregion':
                    icon.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONREGION)
                elif params[key] == 'onrequest':
                    icon.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONREQUEST)
                elif params[key] == 'onstop':
                    icon.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONSTOP)
            elif key == 'viewrefreshtime':
                icon.set_viewrefreshtime(params[key])
            elif key == 'viewboundscale':
                icon.set_viewboundscale(params[key])
            elif key == 'viewformat':
                icon.set_viewformat(params[key])    
            elif key == 'httpquery':
                icon.set_httpquery(params[key])                  
        
        return icon

    """ --------------------------------------------------------------
    <IconStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#iconstyle
    """
    def create_iconstyle(self, params = {} ):
    
        iconstyle = factory.CreateIconStyle()
        iconstyle = self.process_colorstyle_attributes(iconstyle, params)

        for key in params:           
            if key == 'scale':
                iconstyle.set_scale(params[key])
            elif key == 'heading':
                iconstyle.set_heading(params[key])
            elif key == 'icon':
                iconstyle.set_icon(params[key])
            elif key == 'hotspot':
                iconstyle.set_hotspot(params[key])
                
        return iconstyle


    """ --------------------------------------------------------------
    <IconStyleIcon> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#iconstyle
    """
    def create_iconstyleicon(self, params = {} ):
    
        iconstyleicon = factory.CreateIconStyleIcon()
        iconstyleicon = self.process_object_attributes(iconstyleicon, params)

        for key in params:           
            if key == 'href':
                iconstyleicon.set_href(params[key])
                
        return iconstyleicon

    """ --------------------------------------------------------------
    <ImagePyramid> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#imagepyramid
    """
    def create_imagepyramid(self,params={}):
        imagepyramid = factory.CreateImagePyramid()
        imagepyramid = self.process_object_attributes(imagepyramid,params)
        
        for key in params:
            if key == 'tilesize':
                imagepyramid.set_tilesize(params[key])
            elif key == 'maxwidth':
                imagepyramid.set_maxwidth(params[key])
            elif key == 'maxheight':
                imagepyramid.set_maxheight(params[key])
            elif key == 'gridorigin':
                if params[key] == 'lowerleft':
                    imagepyramid.set_gridorigin(kmldom.GRIDORIGIN_LOWERLEFT)
                elif params[key] == 'upperleft':
                    imagepyramid.set_gridorigin(kmldom.GRIDORIGIN_UPPERLEFT)
        return imagepyramid
        
    """ --------------------------------------------------------------
    <InnerBoundaryIs> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#innerBoundaryIs
    """
    def create_innerboundaryis(self,params={}):
    
        innerBound = factory.CreateInnerBoundaryIs()
        for key in params:
            if key == 'linearring':
                innerBound.set_linearring(params[key]);
        return innerBound
  
    """ --------------------------------------------------------------
    <ItemIcon> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#itemicon
    """
    def create_itemicon(self,params={}):
        itemicon = factory.CreateItemIcon()
        itemicon = self.process_object_attributes(itemicon,params)
        
        for key in params:
            if key == 'href':
                itemicon.set_href(params[key])
            elif key == 'state':
                if params[key] == 'open':
                    itemicon.set_state(kmldom.STATE_OPEN)
                elif params[key] == 'closed':
                    itemicon.set_state(kmldom.STATE_CLOSED)
                elif params[key] == 'error':
                    itemicon.set_state(kmldom.STATE_ERROR)
                elif params[key] == 'fetching0':
                    itemicon.set_state(kmldom.STATE_FETCHING0)
                elif params[key] == 'fetching1':
                    itemicon.set_state(kmldom.STATE_FETCHING1)
                elif params[key] == 'fetching2':
                    itemicon.set_state(kmldom.STATE_FETCHING2)
                else:
                    itemicon.set_state(params[key])
        return itemicon

    """ --------------------------------------------------------------
    <Kml> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#kml
    """
    def create_kml(self,params={}):
        kml = factory.CreateKml()
        
        for key in params:
            if key == 'networklinkcontrol':
                kml.set_networklinkcontrol(params[key])
            elif key == 'hint':
                kml.set_hint(params[key])
            elif key == 'folder' or key == 'document' or key == 'photooverlay' or key == 'screenoverlay' or key == 'groundoverlay' or key == 'placemark' or key == 'networklink' or key == 'gxtour':
                kml.set_feature(params[key])
        return kml

    """ --------------------------------------------------------------
    <LabelStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#labelstyle
    """
    def create_labelstyle(self,params={}):
        labelstyle = factory.CreateLabelStyle()
        labelstyle = self.process_colorstyle_attributes(labelstyle,params)
        
        for key in params:
            if key == 'scale':
                labelstyle.set_scale(params[key])
        return labelstyle
 
    """ --------------------------------------------------------------
    <LatLonAltBox> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#latlonaltbox
    """
    def create_latlonaltbox(self,params={}):
        latlonaltbox = factory.CreateLatLonAltBox()
        latlonaltbox = self.process_object_attributes(latlonaltbox,params)
        
        for key in params:
            if key == 'north':
                latlonaltbox.set_north(params[key])
            elif key == 'south':
                latlonaltbox.set_south(params[key])
            elif key == 'east':
                latlonaltbox.set_east(params[key])
            elif key == 'west':
                latlonaltbox.set_west(params[key])
            elif key == 'minaltitude':
                latlonaltbox.set_minaltitude(params[key])
            elif key == 'maxaltitude':
                latlonaltbox.set_maxaltitude(params[key])
        return latlonaltbox

    """ --------------------------------------------------------------
    <LatLonBox> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#latlonbox
    """
    def create_latlonbox(self,params={}):
        latlonbox = factory.CreateLatLonBox()
        latlonbox = self.process_object_attributes(latlonbox,params)
        
        for key in params:
        
            if key == 'north':
                latlonbox.set_north(params[key])
            elif key == 'south':
                latlonbox.set_south(params[key])
            elif key == 'east':
                latlonbox.set_east(params[key])
            elif key == 'west':
                latlonbox.set_west(params[key])
            elif key == 'rotation':
                latlonbox.set_rotation(params[key])
        return latlonbox

    """ --------------------------------------------------------------
    <LinearRing> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#linearring
    """
    def create_linearring(self,params = {}):

        linearring = factory.CreateLinearRing()
        linearring = self.process_geometry_attributes(linearring, params) 

        for key in params:           
            if key == 'extrude':
                linearring.set_extrude(params[key])
            elif key == 'tessellate':
                linearring.set_tessellate(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    linearring.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    linearring.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    linearring.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    linearring.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    linearring.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'coordinates': 
                linearring.set_coordinates(params[key])
        return linearring
                
    """ --------------------------------------------------------------
    <LineString> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#linestring
    """
    def create_linestring(self,params = {}):

        linestring = factory.CreateLineString()
        linestring = self.process_geometry_attributes(linestring, params) 
        

        for key in params:           
            if key == 'extrude':
                linestring.set_extrude(params[key])
            elif key == 'tessellate':
                linestring.set_tessellate(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    linestring.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    linestring.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    linestring.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    linestring.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    linestring.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'coordinates':
                linestring.set_coordinates(params[key])
        return linestring

    """ --------------------------------------------------------------
    <LineStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#linestyle
    """
    def create_linestyle(self,params = {}):

        linestyle = factory.CreateLineStyle() 
        linestyle = self.process_colorstyle_attributes(linestyle, params)
        
        for key in params:
            if key == 'width':
                linestyle.set_width(params[key])
        return linestyle 

    """ --------------------------------------------------------------
    <Link> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#link
    """
    def create_link(self,params={}):
        link = factory.CreateLink()
        link = self.process_object_attributes(link,params)
        
        for key in params:
            if key == 'href':
                link.set_href(str(params[key]))
            elif key == 'refreshmode':
                if params[key] == 'onchange':
                    link.set_refreshmode(kmldom.REFRESHMODE_ONCHANGE)
                elif params[key] == 'onexpire':
                    link.set_refreshmode(kmldom.REFRESHMODE_ONEXPIRE)
                elif params[key] == 'oninterval':
                    link.set_refreshmode(kmldom.REFRESHMODE_ONINTERVAL)
            elif key == 'refreshinterval':
                link.set_refreshinterval(params[key])
            elif key == 'viewrefreshmode':
                if params[key] == 'never':
                    link.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_NEVER)
                elif params[key] == 'onregion':
                    link.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONREGION)
                elif params[key] == 'onrequest':
                    link.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONREQUEST)
                elif params[key] == 'onstop':
                    link.set_viewrefreshmode(kmldom.VIEWREFRESHMODE_ONSTOP)
            elif key == 'viewrefreshtime':
                link.set_viewrefreshtime(params[key])
            elif key == 'viewboundscale':
                link.set_viewboundscale(params[key])
            elif key == 'viewformat':
                link.set_viewformat(params[key])
            elif key == 'httpquery':
                link.set_httpquery(params[key])
                
        return link

    """ --------------------------------------------------------------
    <LinkSnippet> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#linksnippet
    """
    def create_linksnippet(self,params={}):
        linksnippet = factory.CreateLinkSnippet()

        for key in params:
            if key == 'maxlines':
                linksnippet.set_maxlines(params[key])
            elif key == 'text':
                linksnippet.set_text(params[key])
        return linksnippet

    """ --------------------------------------------------------------
    <ListStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#liststyle
    """
    def create_liststyle(self,params={}):
        liststyle = factory.CreateListStyle()
        liststyle = self.process_object_attributes(liststyle,params)
        
        for key in params:
            if key == 'listitemtype':
                if params[key] == 'check':
                    liststyle.set_listitemtype(kmldom.LISTITEMTYPE_CHECK)
                elif params[key] == 'checkhidechildren':
                    liststyle.set_listitemtype(kmldom.LISTITEMTYPE_CHECKHIDECHILDREN)
                elif params[key] == 'checkoffonly':
                    liststyle.set_listitemtype(kmldom.LISTITEMTYPE_CHECKOFFONLY)
                elif params[key] == 'radiofolder':
                    liststyle.set_listitemtype(kmldom.LISTITEMTYPE_RADIOFOLDER)
            elif key == 'bgcolor':
                liststyle.set_bgcolor(kmlbase.Color32(params[key]))
            elif key == 'itemicon':
                liststyle.add_itemicon(params[key])
        return liststyle

    """ --------------------------------------------------------------
    <Location> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#location
    """
    def create_location(self,params={}):
        location = factory.CreateLocation()
        location = self.process_object_attributes(location,params)
        
        for key in params:
            if key == 'latitude':
                location.set_latitude(params[key])
            elif key == 'longitude':
                location.set_longitude(params[key])
            elif key == 'altitude':
                location.set_altitude(params[key])
        return location

    """ --------------------------------------------------------------
    <Lod> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#lod
    """
    def create_lod(self,params={}):
        lod = factory.CreateLod()
        lod = self.process_object_attributes(lod,params)
        
        for key in params:
            if key == 'minlodpixels':
                lod.set_minlodpixels(params[key])
            elif key == 'maxlodpixels':
                lod.set_maxlodpixels(params[key])
            elif key == 'minfadeextent':
                lod.set_minfadeextent(params[key])
            elif key == 'maxfadeextent':
                lod.set_maxfadeextent(params[key])
        return lod

    """ --------------------------------------------------------------
    <LookAt> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#lookat
    """
    def create_lookat(self,params = {}):
    
        lookat = factory.CreateLookAt()
        lookat = self.process_abstractview_attributes(lookat,params)
        
        for key in params:
            if key == 'longitude':
                lookat.set_longitude(params[key])
            elif key == 'latitude':
                lookat.set_latitude(params[key])
            elif key == 'altitude':
                lookat.set_altitude(params[key])
            elif key == 'heading':
                lookat.set_heading(params[key])
            elif key == 'tilt':
                lookat.set_tilt(params[key])
            elif key == 'range':
                lookat.set_range(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    lookat.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    lookat.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    lookat.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    lookat.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    lookat.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
        return lookat

    """ --------------------------------------------------------------
    <Model> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#model
    """
    def create_model(self,params={}):
        model = factory.CreateModel()
        model = self.process_geometry_attributes(model,params)
        
        for key in params:
            if key == 'altitudemode':
                if params[key] == 'clamptoground':
                    model.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    model.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    model.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    model.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    model.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'location':
                model.set_location(params[key])
            elif key == 'orientation':
                model.set_orientation(params[key])
            elif key == 'scale':
                model.set_scale(params[key])
            elif key == 'link':
                model.set_link(params[key])
            elif key == 'resourcemap':
                model.set_resourcemap(params[key])
        return model

    """ --------------------------------------------------------------
    <MultiGeometry> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#multigeometry
    """
    def create_multigeometry(self,geoms= {}):
    
        multigeometry = factory.CreateMultiGeometry()
        multigeometry = self.process_geometry_attributes(multigeometry,geoms)
        
        for key in geoms:
            if ((key == 'point')
                    | (key == 'linestring')
                    | (key == 'linearring')
                    | (key == 'polygon')
                    | (key == 'multigeometry')
                    | (key == 'model')):
                if isinstance(geoms[key],list):
                    for x in geoms[key]:
                        multigeometry.add_geometry(x)
                else:
                    multigeometry.add_geometry(geoms[key])
        return multigeometry

    """ --------------------------------------------------------------
    <NetworkLink> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#networklink
    """
    def create_networklink(self,params={}):
    
        networklink = factory.CreateNetworkLink()
        networklink = self.process_feature_attributes(networklink,params)
        
        for key in params:
            if key == 'refreshvisibility':
                networklink.set_refreshvisibility(params[key])
            elif key == 'flytoview':
                networklink.set_flytoview(params[key])
            elif key == 'link':
                networklink.set_link(params[key])
        return networklink
        
    """ --------------------------------------------------------------
    <NetworkLinkControl> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#networklinkcontrol
    """
    def create_networklinkcontrol(self,params={}):
    
        networklinkcontrol = factory.CreateNetworkLinkControl()
        
        for key in params:
            if key == 'minrefreshperiod':
                networklinkcontrol.set_minrefreshperiod(params[key])
            elif key == 'maxsessionlength':
                networklinkcontrol.set_maxsessionlength(params[key])
            elif key == 'cookie':
                networklinkcontrol.set_cookie(params[key])
            elif key == 'message':
                networklinkcontrol.set_message(params[key])
            elif key == 'linkname':
                networklinkcontrol.set_linkname(params[key])
            elif key == 'linkdescription':
                networklinkcontrol.set_linkdescription(params[key])
            elif key == 'linksnippet':
                networklinkcontrol.set_linksnippet(params[key])
            elif key == 'expires':
                networklinkcontrol.set_expires(params[key])
            elif key == 'update':
                networklinkcontrol.set_update(params[key])
            elif key == 'camera' or key == 'lookat':
                networklinkcontrol.set_abstractview(params[key])
        return networklinkcontrol

    """ --------------------------------------------------------------
    <Object> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#object
    """
    def process_object_attributes(self, obj, params):

        for key in params:           
            if key == 'id':
                obj.set_id(params[key])
            elif key == 'targetid':
                obj.set_targetid(params[key])
                     
        return obj
  
    """ --------------------------------------------------------------
    <Orientation> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#orientation
    """
    def create_orientation(self,params={}):
    
        orientation = factory.CreateOrientation()
        orientation = self.process_object_attributes(orientation,params)
        
        for key in params:
            if key == 'heading':
                orientation.set_heading(params[key])
            elif key == 'roll':
                orientation.set_roll(params[key])
            elif key == 'tilt':
                orientation.set_tilt(params[key])
        return orientation
    
    """ --------------------------------------------------------------
    <outerBoundaryIs> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#outerBoundaryIs
    """
    def create_outerboundaryis(self,params={}):
    
        outerBound = factory.CreateOuterBoundaryIs()

        for key in params:
            if key == 'linearring':
                outerBound.set_linearring(params[key]);
        
        return outerBound

    """ --------------------------------------------------------------
    <Overlay> element (abstract)
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#pair
    """
    def process_overlay_attributes(self,overlay,params={}):
        overlay = self.process_feature_attributes(overlay,params)
        
        for key in params:
            if key == 'color':
                overlay.set_color(kmlbase.Color32(params[key]))
            elif key == 'draworder':
                overlay.set_draworder(params[key])
            elif key == 'icon':
                overlay.set_icon(params[key])
        return overlay

    """ --------------------------------------------------------------
    <OverlayXY> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#overlayxy
    """
    def create_overlayxy(self,params={}):
        overlayxy = factory.CreateOverlayXY()
        
        for key in params:
            if key == 'x':
                overlayxy.set_x(params[key])
            elif key == 'xunits':
                if params[key] == 'fraction':
                    overlayxy.set_xunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    overlayxy.set_xunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    overlayxy.set_xunits(kmldom.UNITS_PIXELS)
            elif key == 'y':
                overlayxy.set_y(params[key])
            elif key == 'yunits':
                if params[key] == 'fraction':
                    overlayxy.set_yunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    overlayxy.set_yunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    overlayxy.set_yunits(kmldom.UNITS_PIXELS)
        return overlayxy
      
    """ --------------------------------------------------------------
    <Pair> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#pair
    """
    def create_pair(self,params={}):
    
        pair = factory.CreatePair()
        pair = self.process_styleselector_attributes(pair, params)
        
        for key in params:
            if key == 'key':
                if params[key] == 'normal':
                    pair.set_key(0)
                elif params[key] == 'highlight':
                    pair.set_key(1)
                else:
                    pair.set_key(params[key])
            elif key == 'styleUrl':
                pair.set_styleurl(params[key])
            elif key == 'style':
                pair.set_styleselector(params[key])
        return pair

    """ --------------------------------------------------------------
    <PhotoOverlay> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#photooverlay
    """
    def create_photooverlay(self,params={}):
        photooverlay = factory.CreatePhotoOverlay()
        photooverlay = self.process_overlay_attributes(photooverlay,params)
        
        for key in params:
            if key == 'rotation':
                photooverlay.set_rotation(params[key])
            elif key == 'viewvolume':
                photooverlay.set_viewvolume(params[key])
            elif key == 'imagepyramid':
                photooverlay.set_imagepyramid(params[key])
            elif key == 'point':
                photooverlay.set_point(params[key])
            elif key == 'shape':
                if params[key] == 'cylinder':
                    photooverlay.set_shape(kmldom.SHAPE_CYLINDER)
                elif params[key] == 'sphere':
                    photooverlay.set_shape(kmldom.SHAPE_SPHERE)
                elif params[key] == 'rectangle':
                    photooverlay.set_shape(kmldom.SHAPE_RECTANGLE)
        return photooverlay
  
    """ --------------------------------------------------------------
    <Placemark> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#placemark
    """
    def create_placemark(self, params = {} ):
    
        placemark = factory.CreatePlacemark()
        placemark = self.process_feature_attributes(placemark, params) 
        
        for key in params:           
            if ((key == 'point')
                    | (key == 'linestring')
                    | (key == 'linearring')
                    | (key == 'polygon')
                    | (key == 'multigeometry')
                    | (key == 'model')):
                
                placemark.set_geometry(params[key])
        return placemark

    """ --------------------------------------------------------------
    <Point> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#point
    """
    def create_point(self, params = {} ):
    
        point = factory.CreatePoint()
        point = self.process_geometry_attributes(point, params) 
        
        for key in params:
            if key == 'extrude':
                point.set_extrude(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    point.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    point.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    point.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    point.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    point.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'coordinates':
                point.set_coordinates(params[key])
        return point

    """ --------------------------------------------------------------
    <Polygon> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#polygon
    """
    def create_polygon(self,params = {}):
        
        polygon = factory.CreatePolygon()
        polygon = self.process_geometry_attributes(polygon, params)

        for key in params:           
            if key == 'extrude':
                polygon.set_extrude(params[key])
            elif key == 'tessellate':
                polygon.set_tessellate(params[key])
            elif key == 'altitudemode':
                if params[key] == 'clamptoground':
                    polygon.set_altitudemode(kmldom.ALTITUDEMODE_CLAMPTOGROUND)
                elif params[key] == 'relativetoground':
                    polygon.set_altitudemode(kmldom.ALTITUDEMODE_RELATIVETOGROUND)
                elif params[key] == 'absolute':
                    polygon.set_altitudemode(kmldom.ALTITUDEMODE_ABSOLUTE)
            elif key == 'gxaltitudemode':
                if params[key] == 'clamptoseafloor':
                    polygon.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_CLAMPTOSEAFLOOR)
                elif params[key] == 'relativetoseafloor':
                    polygon.set_gx_altitudemode(kmldom.GX_ALTITUDEMODE_RELATIVETOSEAFLOOR)
            elif key == 'coordinates':
                polygon.set_coordinates(params[key])
            elif key == 'outerboundaryis':
                polygon.set_outerboundaryis(params[key])
            elif key == 'innerboundaryis':                
                if isinstance(params[key],list):
                    for x in params[key]:
                        polygon.add_innerboundaryis(x)
                else:
                    polygon.add_innerboundaryis(params[key])  
        return polygon

    """ --------------------------------------------------------------
    <PolyStyle> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#polystyle
    """
    def create_polystyle(self, params = {}):
        
        polystyle = factory.CreatePolyStyle()
        polystyle = self.process_colorstyle_attributes(polystyle,params)
        
        for key in params:
            if key == 'fill':
                polystyle.set_fill(params[key])
            elif key == 'outline':
                polystyle.set_outline(params[key])        
        return polystyle
        
    """ --------------------------------------------------------------
    <Region> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#region
    """
    def create_region(self,params={}):
        region = factory.CreateRegion()
        region = self.process_object_attributes(region,params)
        
        for key in params:
            if key == 'latlonaltbox':
                region.set_latlonaltbox(params[key])
            elif key == 'lod':
                region.set_lod(params[key])
        return region

    """ --------------------------------------------------------------
    <ResourceMap> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#resourcemap
    """ 
    def create_resourcemap(self,params={}):
        resourcemap = factory.CreateResourceMap()
        resourcemap = self.process_object_attributes(resourcemap,params)
        
        for key in params:
            if key == 'alias':
                if isinstance(params[key],list):
                    for x in params[key]:
                        resourcemap.add_alias(x)
                else:
                    resourcemap.add_alias(params[key])
        return resourcemap

    """ --------------------------------------------------------------
    <RotationXY> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#rotationxy
    """
    def create_rotationxy(self,params={}):
        rotationxy = factory.CreateRotationXY()
        
        for key in params:
            if key == 'x':
                rotationxy.set_x(params[key])
            elif key == 'xunits':
                if params[key] == 'fraction':
                    rotationxy.set_xunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    rotationxy.set_xunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    rotationxy.set_xunits(kmldom.UNITS_PIXELS)
            elif key == 'y':
                rotationxy.set_y(params[key])
            elif key == 'yunits':
                if params[key] == 'fraction':
                    rotationxy.set_yunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    rotationxy.set_yunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    rotationxy.set_yunits(kmldom.UNITS_PIXELS)
        return rotationxy
       
    """ --------------------------------------------------------------
    <Scale> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#scale
    """ 
    def create_scale(self,params = {}):
    
        scale = factory.CreateScale()
        scale = self.process_object_attributes(scale, params)
        
        for key in params:
            if key == 'x':
                scale.set_x(params[key])
            elif key == 'y':
                scale.set_y(params[key])
            elif key == 'z':
                scale.set_z(params[key])
        return scale

    """ --------------------------------------------------------------
    <Schema> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#schema
    """
    def create_schema(self,params={}):
    
        schema = factory.CreateSchema()
        schema = self.process_object_attributes(schema,params)
        
        for key in params:
            if key == 'name':
                schema.set_name(params[key])
            elif key == 'simplefield':
                if isinstance(params[key],list):
                    for x in params[key]:
                        schema.add_simplefield(x)
                else:
                    schema.add_simplefield(params[key])
        return schema
        
    """ --------------------------------------------------------------
    <SchemaData> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#schemadata
    """
    def create_schemadata(self,params={}):
        schemadata = factory.CreateSchemaData()
       
        for key in params:
            if key == 'simpledata':
                if isinstance(params[key],list):
                    for x in params[key]:
                        schemadata.add_simpledata(x)
                else:
                    schemadata.add_simpledata(params[key])
        return schemadata

    """ --------------------------------------------------------------
    <ScreenOverlay> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#screenoverlay
    """
    def create_screenoverlay(self,params={}):
    
        screenoverlay = factory.CreateScreenOverlay()
        screenoverlay = self.process_overlay_attributes(screenoverlay,params)
        
        for key in params:
            if key == 'overlayxy':
                screenoverlay.set_overlayxy(params[key])
            elif key == 'screenxy':
                screenoverlay.set_screenxy(params[key])
            elif key == 'rotationxy':
                screenoverlay.set_rotationxy(params[key])
            elif key == 'size':
                screenoverlay.set_size(params[key])
            elif key == 'rotation':
                screenoverlay.set_rotation(params[key])
        return screenoverlay

    """ --------------------------------------------------------------
    <ScreenXY> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#screenxy
    """
    def create_screenxy(self,params={}):
        screenxy = factory.CreateScreenXY()
        
        for key in params:
            if key == 'x':
                screenxy.set_x(params[key])
            elif key == 'xunits':
                if params[key] == 'fraction':
                    screenxy.set_xunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    screenxy.set_xunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    screenxy.set_xunits(kmldom.UNITS_PIXELS)
            elif key == 'y':
                screenxy.set_y(params[key])
            elif key == 'yunits':
                if params[key] == 'fraction':
                    screenxy.set_yunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    screenxy.set_yunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    screenxy.set_yunits(kmldom.UNITS_PIXELS)
        return screenxy

    """ --------------------------------------------------------------
    <SimpleField> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#simplefield
    """
    def create_simplefield(self,params={}):
        simplefield = factory.CreateSimpleField()
        
        for key in params:
            if key == 'type':
                simplefield.set_type(params[key])
            elif key == 'displayname':
                simplefield.set_displayname(params[key])
            elif key == 'name':
                simplefield.set_name(params[key])
        return simplefield

    """ --------------------------------------------------------------
    <SimpleData> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#simpledata
    """
    def create_simpledata(self,params={}):
        simpledata = factory.CreateSimpleData()
        
        for key in params:
            if key == 'name':
                simpledata.set_name(params[key])
            elif key == 'text':
                simpledata.set_text(params[key])
        return simpledata

    """ --------------------------------------------------------------
    <Size> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#size
    """
    def create_size(self,params={}):
        size = factory.CreateSize()
        
        for key in params:
            if key == 'x':
                size.set_x(params[key])
            elif key == 'xunits':
                if params[key] == 'fraction':
                    size.set_xunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    size.set_xunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    size.set_xunits(kmldom.UNITS_PIXELS)
            elif key == 'y':
                size.set_y(params[key])
            elif key == 'yunits':
                if params[key] == 'fraction':
                    size.set_yunits(kmldom.UNITS_FRACTION)
                elif params[key] == 'insetpixels':
                    size.set_yunits(kmldom.UNITS_INSETPIXELS)
                elif params[key] == 'pixels':
                    size.set_yunits(kmldom.UNITS_PIXELS)
        return size

    """ --------------------------------------------------------------
    <Snippet> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#snippet
    """        
    def create_snippet(self, params = {} ):
    
        snippet = factory.CreateSnippet()
        for key in params:
            if key == 'maxlines':
                snippet.set_maxlines(params[key])
            elif key == 'text':
                snippet.set_text(params[key])
        return snippet

    """ --------------------------------------------------------------
    <Style> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#style
    """        
    def create_style(self, params = {} ):
    
        style = factory.CreateStyle()
        style = self.process_styleselector_attributes(style, params)
        
        for key in params:            
            if key == 'iconstyle':
                style.set_iconstyle(params[key])
            elif key == 'labelstyle':
                style.set_labelstyle(params[key])
            elif key == 'linestyle':
                style.set_linestyle(params[key])
            elif key == 'polystyle':
                style.set_polystyle(params[key])
            elif key == 'balloonstyle':
                style.set_balloonstyle(params[key])
            elif key == 'liststyle':
                style.set_liststyle(params[key])
        return style


    """ --------------------------------------------------------------
    <StyleMap> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#stylemap
    """   
    def create_stylemap(self,params={}):
        
        stylemap = factory.CreateStyleMap()
        stylemap = self.process_styleselector_attributes(stylemap, params)
        
        for key in params:
            if key == 'pair':
                if isinstance(params[key],list):
                    for x in params[key]:
                        stylemap.add_pair(x)
                else:
                    stylemap.add_pair(params[key])
        return stylemap
    
          
    """ --------------------------------------------------------------
    <StyleSelector> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#styleselector
    """        
    def process_styleselector_attributes(self, styleselector, params):
        
        styleselector = self.process_object_attributes(styleselector, params)
        return styleselector

    """ --------------------------------------------------------------
    <SubStyle> element abstract class
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#substyle
    """ 
    def process_substyle_attributes(self,substyle, params):
        
        substyle = self.process_object_attributes(substyle, params)        
        return substyle

    """ --------------------------------------------------------------
    <TimeSpan> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#timespan
    """
    def create_timespan(self, params={}):
    
        import datetime
            
        timespan = factory.CreateTimeSpan()
        timespan = self.process_timeprimitive_attributes(timespan, params)

        for key in params:
            if key == 'begin':
                if type(params[key]) == StringType:
                    timespan.set_begin(params[key])
                elif type(params[key]) == datetime.datetime:
                    timespan.set_begin(params[key].isoformat())
                else:
                    print "ERROR: unrecognized 'begin' parameter."
            elif key == 'end':
                if type(params[key]) == StringType:
                    timespan.set_end(params[key])
                elif type(params[key]) == datetime.datetime:
                    timespan.set_end(params[key].isoformat())
                else:
                    print "ERROR: unrecognized 'end' parameter."
        return timespan

    """ --------------------------------------------------------------
    <TimeStamp> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#timestamp
    """
    def create_timestamp(self, params={}):
    
        import datetime
        
        timestamp = factory.CreateTimeStamp()
        timestamp = self.process_timeprimitive_attributes(timestamp, params)

        for key in params:
            if key == 'when':
                if type(params[key]) == StringType:
                    timestamp.set_when(params[key])
                elif type(params[key]) == datetime.datetime:
                    timestamp.set_when(params[key].isoformat())
                else:
                    print "ERROR: unrecognized 'when' parameter."
                
        return timestamp

    """ --------------------------------------------------------------
    <TimePrimitive> element abstract class
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#timeprimitive
    """ 
    def process_timeprimitive_attributes(self,timeprimitive, params):
    
        timeprimitive = self.process_object_attributes(timeprimitive, params)
        return timeprimitive

    """ --------------------------------------------------------------
    <Update> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#update
    """
    def create_update(self, params={}):
        update = factory.CreateUpdate()
        
        for key in params:
            if key == 'targethref':
                update.set_targethref(params[key])
            elif key == 'create' or key == 'change' or key == 'delete':
                if isinstance(params[key],list):
                    for x in params[key]:
                        update.add_updateoperation(x)
                else:
                    update.add_updateoperation(params[key])
        return update

    """ --------------------------------------------------------------
    <ViewVolume> element
    
    Ref:
    http://code.google.com/apis/kml/documentation/kmlreference.html#viewvolume
    """    
    def create_viewvolume(self,params={}):
        viewvolume = factory.CreateViewVolume()
        viewvolume = self.process_object_attributes(viewvolume,params)
        
        for key in params:
            if key == 'leftFov':
                viewvolume.set_leftfov(params[key])
            elif key == 'rightFov':
                viewvolume.set_rightfov(params[key])
            elif key == 'bottomFov':
                viewvolume.set_bottomfov(params[key])
            elif key == 'topFov':
                viewvolume.set_topfov(params[key])
            elif key == 'near':
                viewvolume.set_near(params[key])
        return viewvolume

class Utilities():

    def SerializeRaw(self,object):
        return kmldom.SerializeRaw(object)
    
    def SerializePretty(self,object):
        return kmldom.SerializePretty(object)
    
    def AddAltitudeToShape(self,shape,alt,altMode):

        newShape = None

        if shape.Type() == kmldom.Type_MultiGeometry:

            newMg = factory.CreateMultiGeometry()         
            for idx in range(0,shape.get_geometry_array_size()):
                geo = shape.get_geometry_array_at(idx)
                newGeo = self.AddAltitudeToShape(geo,alt, altMode)
                newMg.add_geometry(newGeo)
            newShape = newMg
        
        elif shape.Type() == kmldom.Type_Point:
            oldPoint = kmldom.AsPoint(shape)            
            newPoint = factory.CreatePoint()
            pointCoords = oldPoint.get_coordinates()
            newCoords = factory.CreateCoordinates()
            for idx in range(0, pointCoords.get_coordinates_array_size()):
                coord = pointCoords.get_coordinates_array_at(idx)
                lat = coord.get_latitude()
                lon = coord.get_longitude()
                newCoords.add_latlngalt(lat,lon,alt)
            newPoint.set_coordinates(newCoords)
            newPoint.set_altitudemode(altMode)
            newShape = newPoint
        
        elif shape.Type() == kmldom.Type_LinearRing:
            oldLR = kmldom.AsLinearRing(shape)
            newLR = factory.CreateLinearRing()
            lrCoords = oldLR.get_coordinates()
            newCoords = factory.CreateCoordinates()
            for idx in range(0, lrCoords.get_coordinates_array_size()):
                coord = lrCoords.get_coordinates_array_at(idx)
                lat = coord.get_latitude()
                lon = coord.get_longitude()
                newCoords.add_latlngalt(lat,lon,alt)
            newLR.set_coordinates(newCoords)
            newShape = newLR

        elif shape.Type() == kmldom.Type_Polygon:
            oldPoly = kmldom.AsPolygon(shape)            
            newPoly = factory.CreatePolygon()

            if oldPoly.has_outerboundaryis():
                obi = oldPoly.get_outerboundaryis()          
                newObi = factory.CreateOuterBoundaryIs()
                lro = obi.get_linearring()
                newLRO = self.AddAltitudeToShape(lro, alt, altMode)
                newObi.set_linearring(newLRO)
                newPoly.set_outerboundaryis(newObi)

            for idx in range(0,oldPoly.get_innerboundaryis_array_size()):
                ibi = oldPoly.get_innerboundaryis_array_at(idx)  
                newIbi = factory.CreateInnerBoundaryIs()
                lri = ibi.get_linearring()
                newLRI = self.AddAltitudeToShape(lri, alt, altMode)
                newIbi.set_linearring(newLRI)
                newPoly.add_innerboundaryis(newIbi)

            newShape = newPoly

        else:
            pass
        
        return newShape

    def IdentifyElement(self,element):

        #This dictionary matches the type constant for libkml datatypes with a conversion function
        TypeDict = {kmldom.Type_AbstractLatLonBox:kmldom.AsAbstractLatLonBox(element),
                        kmldom.Type_AbstractView:kmldom.AsAbstractView(element),kmldom.Type_Alias:kmldom.AsAlias(element),
                        kmldom.Type_AtomAuthor:kmldom.AsAtomAuthor(element),
                        kmldom.Type_AtomLink:kmldom.AsAtomLink(element),kmldom.Type_BalloonStyle:kmldom.AsBalloonStyle(element),
                        kmldom.Type_Camera:kmldom.AsCamera(element),
                        kmldom.Type_Change:kmldom.AsChange(element),kmldom.Type_ColorStyle:kmldom.AsColorStyle(element),
                        kmldom.Type_Container:kmldom.AsContainer(element),kmldom.Type_Create:kmldom.AsCreate(element),
                        kmldom.Type_Data:kmldom.AsData(element),
                        kmldom.Type_Delete:kmldom.AsDelete(element),
                        kmldom.Type_Document:kmldom.AsDocument(element),kmldom.Type_ExtendedData:kmldom.AsExtendedData(element),
                        kmldom.Type_Feature:kmldom.AsFeature(element),kmldom.Type_Folder:kmldom.AsFolder(element),
                        kmldom.Type_Geometry:kmldom.AsGeometry(element),
                        kmldom.Type_GroundOverlay:kmldom.AsGroundOverlay(element),kmldom.Type_GxAnimatedUpdate:kmldom.AsGxAnimatedUpdate(element),
                        kmldom.Type_GxFlyTo:kmldom.AsGxFlyTo(element),
                        kmldom.Type_GxLatLonQuad:kmldom.AsGxLatLonQuad(element),kmldom.Type_GxPlaylist:kmldom.AsGxPlaylist(element),
                        kmldom.Type_GxSoundCue:kmldom.AsGxSoundCue(element),kmldom.Type_GxTimeSpan:kmldom.AsGxTimeSpan(element),
                        kmldom.Type_GxTimeStamp:kmldom.AsGxTimeStamp(element),
                        kmldom.Type_GxTour:kmldom.AsGxTour(element),kmldom.Type_GxTourControl:kmldom.AsGxTourControl(element),
                        kmldom.Type_GxTourPrimitive:kmldom.AsGxTourPrimitive(element),
                        kmldom.Type_GxWait:kmldom.AsGxWait(element),kmldom.Type_Icon:kmldom.AsIcon(element),
                        kmldom.Type_IconStyle:kmldom.AsIconStyle(element),kmldom.Type_IconStyleIcon:kmldom.AsIconStyleIcon(element),
                        kmldom.Type_ImagePyramid:kmldom.AsImagePyramid(element),
                        kmldom.Type_ItemIcon:kmldom.AsItemIcon(element),kmldom.Type_LabelStyle:kmldom.AsLabelStyle(element),
                        kmldom.Type_LatLonAltBox:kmldom.AsLatLonAltBox(element),kmldom.Type_LatLonBox:kmldom.AsLatLonBox(element),
                        kmldom.Type_LineString:kmldom.AsLineString(element),
                        kmldom.Type_LineStyle:kmldom.AsLineStyle(element),kmldom.Type_LinearRing:kmldom.AsLinearRing(element),
                        kmldom.Type_Link:kmldom.AsLink(element),kmldom.Type_ListStyle:kmldom.AsListStyle(element),
                        kmldom.Type_Location:kmldom.AsLocation(element),
                        kmldom.Type_Lod:kmldom.AsLod(element),kmldom.Type_LookAt:kmldom.AsLookAt(element),
                        kmldom.Type_Model:kmldom.AsModel(element),
                        kmldom.Type_MultiGeometry:kmldom.AsMultiGeometry(element),kmldom.Type_NetworkLink:kmldom.AsNetworkLink(element),
                        kmldom.Type_NetworkLinkControl:kmldom.AsNetworkLinkControl(element),kmldom.Type_Object:kmldom.AsObject(element),
                        kmldom.Type_Orientation:kmldom.AsOrientation(element),
                        kmldom.Type_Overlay:kmldom.AsOverlay(element),kmldom.Type_Pair:kmldom.AsPair(element),
                        kmldom.Type_PhotoOverlay:kmldom.AsPhotoOverlay(element),
                        kmldom.Type_Placemark:kmldom.AsPlacemark(element),kmldom.Type_Point:kmldom.AsPoint(element),
                        kmldom.Type_PolyStyle:kmldom.AsPolyStyle(element),
                        kmldom.Type_Polygon:kmldom.AsPolygon(element),kmldom.Type_Region:kmldom.AsRegion(element),
                        kmldom.Type_ResourceMap:kmldom.AsResourceMap(element),
                        kmldom.Type_Scale:kmldom.AsScale(element),kmldom.Type_Schema:kmldom.AsSchema(element),
                        kmldom.Type_SchemaData:kmldom.AsSchemaData(element),kmldom.Type_ScreenOverlay:kmldom.AsScreenOverlay(element),
                        kmldom.Type_SimpleData:kmldom.AsSimpleData(element),
                        kmldom.Type_SimpleField:kmldom.AsSimpleField(element),kmldom.Type_Snippet:kmldom.AsSnippet(element),
                        kmldom.Type_Style:kmldom.AsStyle(element),
                        kmldom.Type_StyleMap:kmldom.AsStyleMap(element),kmldom.Type_StyleSelector:kmldom.AsStyleSelector(element),
                        kmldom.Type_SubStyle:kmldom.AsSubStyle(element),
                        kmldom.Type_TimePrimitive:kmldom.AsTimePrimitive(element),kmldom.Type_TimeSpan:kmldom.AsTimeSpan(element),
                        kmldom.Type_TimeStamp:kmldom.AsTimeStamp(element),
                        kmldom.Type_Update:kmldom.AsUpdate(element),kmldom.Type_ViewVolume:kmldom.AsViewVolume(element),
                        }

        #Try to match in the type dictionary. If no match, return the element that was passed
        try:
            return TypeDict[kmldom.Element.Type(element)]
        except KeyError:
            return element
    
    def RawKMLToLibKMLObject(self, kmlstring):
        
        strlist = []
        if isinstance(kmlstring,list):
            strlist = kmlstring
        else:
            strlist.append(kmlstring)

        kmlobj = []
        for val in strlist:
            element = kmldom.ParseKml(val)
            kmlobj.append(self.IdentifyElement(element))
        if len(kmlobj) > 1:
            return kmlobj
        else:
            return kmlobj[0]


    def GetShapeTypeDescription(self,shape):
        
        ShapeTypeDict = {kmldom.Type_Polygon:'polygon',kmldom.Type_Point:'point',kmldom.Type_LinearRing:'linearring',kmldom.Type_MultiGeometry:'multigeometry'}

        try:
            return ShapeTypeDict[shape.Type()]
        except KeyError:
            return ''
 
    '''----------------------------------------------------------------------
        NAME: create_kmz()
        DESCRIPTION: CREATE A KMZ FILE
        INPUT: KMLFileName - (string) name of .kml file to be zipped (including directory)
                outputFileName - (string) name of the .kmz file that you want to be created
                filesToBeZipped - (list of strings) names of the files (and their directories) that you want zipped into the .kmz
    '''    
    def create_kmz(self, KMLFileName, outputFileName = 'out.kmz' ,filesToBeZipped = []):
    
        zip = zipfile.ZipFile(outputFileName,'w')
        zip.write(KMLFileName)
        for x in filesToBeZipped:
            zip.write(x)
       
        zip.close()
        
    def process_html(self,inputFile):
        
        cData = '<![CDATA['
        
        temp = open(inputFile,'r')
        for line in temp:
            i=0
            for i in range(0,len(line)):
                if line[i] != ' ':
                    break
            cData = cData + line[i:len(line)]

        cData = cData + ']]>' 
        return cData

if __name__=='__main__':
    from tests import test
    test()
