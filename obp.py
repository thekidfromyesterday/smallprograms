import sys
h = input("Insert how many hits he had? ")
bb = input("Insert how many walks he had? ")
hbp = input("Insert how many times he got hit by a pitch? ")
ab = input("Insert how many at bats did he have? ")
sf = input("Insert how many sacrifice flies did he have? ")
batter = raw_input("Enter the name of the batter ")

ob1 = h + bb + hbp
ob2 = ab + bb + hbp + sf
obp = ob1 / float(ob2)
print "%s's on-base percentage is %f" % (batter, obp)

results = input("Press 1 to save your results ")
if results == 1:
	results = open('/users/akaash/desktop/obp.txt', 'a')
	results.write('%f %s \n' % (obp, batter))
	results.close()
else:
	sys.exit()
