# - ComputeClimatology.py - #
# ------------------------- #
# - Start as main script (not as module)
if __name__ == '__main__':

   import sys, os, MySQLdb, utils
   import numpy as np
   from glob import glob
   # - Wetterturnier specific methods
   from pywetterturnier import utils
   from pywetterturnier import database
   from pywetterturnier import mitteltip

   # - Evaluating input arguments
   inputs = utils.inputcheck('ComputeClimatology')
   # - Read configuration file
   config = utils.readconfig('config.conf',inputs)


   # - Initializing class and open database connection
   db        = database.database(config)

   # - Loading tdate (day since 1970-01-01) for the tournament.
   #   Normaly Friday-Tornament (tdate is then Friday) while
   #   the bet-dates are for Saturday and Sunday if there was
   #   no input tournament date -t/--tdate.
   if config['input_tdate'] == None:
      tdate      = db.current_tournament()
   else:
      tdate      = config['input_tdate']

   print '  * Current tournament is %s' % utils.tdate2string( tdate )
   # - Loading all different cities (active cities)
   cities     = db.get_cities()
   # - If input city set, then drop all other cities.
   if not config['input_city'] == None:
      tmp = []
      for elem in cities:
         if elem['name'] == config['input_city']: tmp.append( elem )
      cities = tmp

   # - Reading parameter list
   params = db.get_parameter_names(False)


   # ----------------------------------------------------------------
   # - Prepare the Climatology
   # ----------------------------------------------------------------
   #username = 'Climatology'
   #db.create_user( username )
   #userID = db.get_user_id( username )

   # ----------------------------------------------------------------

   # ----------------------------------------------------------------
   # - Loopig over all tournament dates
   # ----------------------------------------------------------------
   from datetime import datetime as dt
   
   for tdate in tdates:
      # - Using obervations of the tournament day for our Persistenz player
      tdate_str = dt.fromtimestamp( tdate * 86400 ).strftime('%a, %Y-%m-%d')
      print "    Searching for Observations:     %s (%d)" % (tdate_str,tdate)

   def get_obs_data(self,cityID,paramID,tdate,bdate,wmo=None):
	 # val = dv.get_obs_data(city['10382'], paramID['1'], tdate_str['11292']	, bdate['11293'], wmo=None)
      print 'bla'
