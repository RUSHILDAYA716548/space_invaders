import bs4

#function used to extract bed, bath, garage information from a section of
# soup tree. not a stand alone function
def extractFeatures(featSoup):

	#the feature tree should contain 3 or less sub spans
	spansChildren = featSoup.findChildren()

	for span in spansChildren:
		if span.has_attr('class')==False: # ignores the spans which are for divider objects
			print("awe")
