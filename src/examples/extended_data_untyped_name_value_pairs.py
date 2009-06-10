#import sys
import kmlbase
from pylibkml import *
import unittest

''' This class contains examples shown on the Adding Custom Data page of 
    the KML Developer's Guide
    http://code.google.com/apis/kml/documentation/extendeddata.html
'''

def main():
    ''' This test creates the KML shown under the
    "Adding Untyped Name/Value Pairs" section.
    '''
    
    placemark1 = Kml().create_placemark({
                'name' : 'Club house',
                    'extendeddata' : [
                            Kml().create_data({
                                    'name' : 'holeNumber',
                                    'value' : 1,
                                }),
                            Kml().create_data({
                                    'name' : 'holeYardage',
                                    'value' : 234,
                                }),
                            Kml().create_data({
                                    'name' : 'holePar',
                                    'value' : 4,
                                }),
                        ],
                'point' : Kml().create_point({
                    'coordinates' : Kml().create_coordinates(-111.956,33.5043),
                })
            })
    
    placemark2 = Kml().create_placemark({
                'name' : 'By the lake',
                    'extendeddata' : [
                            Kml().create_data({
                                    'name' : 'holeNumber',
                                    'value' : 5,
                                }),
                            Kml().create_data({
                                    'name' : 'holeYardage',
                                    'value' : 523,
                                }),
                            Kml().create_data({
                                    'name' : 'holePar',
                                    'value' : 5,
                                }),
                        ],
                'point' : Kml().create_point({
                    'coordinates' : Kml().create_coordinates(-111.95,33.5024),
                })
            })
    
    document = Kml().create_document({
            'name' : 'My Golf Course Example',
            'placemark' : [placemark1,placemark2],
        })
    
    print(kmldom.SerializeRaw(document))

if __name__ == '__main__':
    main()
