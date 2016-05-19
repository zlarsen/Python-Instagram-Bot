import sys, getopt

def main(argv):
   username = ''
   password = ''
   try:
      opts, args = getopt.getopt(argv,"hu:p:",["user=","pass="])
   except getopt.GetoptError:
      print 'test.py -u <username> -p <password>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -u <username> -p <password>'
         sys.exit()
      elif opt in ("-u", "--user"):
         username = arg
      elif opt in ("-p", "--pass"):
         password = arg
   print 'Username is', username
   print 'Password is', password

if __name__ == "__main__":
   main(sys.argv[1:])