# Import the required packages
import pandas as pd
import numpy as np

#import data
df = pd.read_csv('friendship_google_maps.csv')
lat=df['lat'].values
long=df['long'].values
commute=df['friend_recommend'].values

#creating the bars
block_start='<Placemark><name>Friend_Recommend</name><styleUrl>#transGreenPoly</styleUrl><Polygon><extrude>1</extrude><altitudeMode>relativeToGround</altitudeMode><outerBoundaryIs><LinearRing><coordinates>'
block_end = '</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>'
block =''

for i in range(0,len(lat)):
    block_start2 = block_start
    value = commute[i]*10000
    block = block + block_start2 + " " + str(long[i]) + "," + str(lat[i]) +"," + str(value) + " "
    block = block + " " + str(long[i]) + "," + str(lat[i]-1) +"," + str(value) + " "
    block = block + " " + str(long[i]+1) + "," + str(lat[i]-1) +"," + str(value) + " "
    block = block + " " + str(long[i]+1) + "," + str(lat[i]) +"," + str(value)
    block = block + block_end

#write to text file. Save it as a kmz file and open it with Google Earth Pro
start = '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document><name>Friend_Recommend</name><Style id="transGreenPoly"><LineStyle><width>1.5</width></LineStyle><PolyStyle><color>7d00ff00</color></PolyStyle></Style><Folder><name>Fix</name>'
end = '</Folder></Document></kml>'
final = start+block+end
f = open("googlemaps_friend.txt", "w");

f.write(final)
f.close()