# encoding: utf-8

#---------------------------IMPORT---------------------------
try:
    import time
except ImportError:
    print("Error importing time")
    exit()
    
try:
    from google import google
except ImportError:
    print("Error importing google module, try: pip install Google-Search-API")
    exit()
    
try:
    from random import randint
except ImportError:
    print("Error importing randit")
    exit()
#---------------------------CLASS DORK---------------------------
class dork:

    def __init__(self, URL, dorks, verbose, ban): # constructor
          self.__url=URL #url to attack
          self.__dork=dorks #selected dorks                  
          self.__verbose=verbose #verbose
          self.__category="" #category (deprecated systems, Info etc)
          self.__response ="No results" #used in line 61 to check results
          self.__noban=ban
          self.__bucle=0

#---------------------------MAIN FUNC---------------------------

    def mainfunc(self):  
         
        file_to = "dorks/" + str(self.__category) # the file to open will be "category.txt", for example Deprecated.txt
        file_to_open = file_to + ".txt"
        if self.__verbose: #if verbose...
            print("[*] opening Dorks File\n")
        try: #except error
            filex=open(file_to_open, "r")  #open
        except FileNotFoundError:
            print("[¡] File " + file_to_open + " does not exist")          
            exit()
        except IOError:
            print("[¡] 'IOError'Error opening FILE")
            exit()
            
        lines = len(open(file_to_open).readlines()) # count lines (will be used in line 44)
        dork = filex.readlines() #asign openned lines to dork list
        
#---------------------------ASIGN FILE DORKS, INFO ETC TO VARIABLES---------------------------

        for i in range(0, lines, 4): #file structure is "dork, impact, description and blank line, so its asign line 1 to dork etc"           
            search_qry = dork[i]
            search_qry = search_qry.replace('\n', ' ').replace('\r', '') #avoid \n
            i+=1
            Impact = dork[i]           
            i+=1
            Description = dork[i]           

#---------------------------google configure and search---------------------------

            query = search_qry + " inurl:" + str(self.__url) #what dorkme will search in google, target selected + inurl (only results of that url) and finally dork
  
 
            if self.__bucle != 0: 
                timet = randint(50,65)
                print("Sleeping {} seconds".format(timet))
                time.sleep(timet) 
                self.__bucle+=1    
                if self.__bucle > 100:
                    timet = randint(180,240)
                    time.sleep(timet)
                    print("Sleeping {} seconds (100 request reached)".format(timet))
                    
                if self.__verbose:
                    print("\n[*] Searching using {}".format(search_qry))           
                self.__response = google.search(query)
                
            else: 
                self.__bucle+=1                
                if self.__verbose:
                    print("\n[*] Searching using {}".format(search_qry))           
                self.__response = google.search(query)
                       
#---------------------------check response and write to file---------------------------

            name_file = self.__category + "_report.txt" #open file where report of X dictionary will be written

#---------------------------SHOW AND SAVE RESULTS---------------------------
            if self.__response: #only execute this loop if google have response                
                print("\n")
                name_file = "results/" + name_file
                for j in self.__response: # for each link in response....
                    Impacts = "" # asign colors
                    if 'high' in Impact.lower():
                        Impacts = "\033[0;31;47mHIGH\033[0m" 
                    if 'medium' in Impact.lower():
                        Impacts = "\033[1;33;40mMedium\033[0m"
                    if 'low' in Impact.lower():
                        Impacts = "\033[1;32;40mlow\033[0m"
                            
                    resultone = "[#] Found: " + str(j.link.encode('UTF-8'))  + "\nImpact: " + Impact + "Description: " + Description + "\n"# without color, (log)   
                    resultones = "[#] Found: " + str(j.link.encode('UTF-8'))  + "\nImpact: " + Impacts  + "\n" + "Description: " + Description #with color, (terminal), the diference between resultone and resultones is Impact variable, with color and colorblind
 
                    print(resultones) #print results
                    with open(name_file, 'a') as report_file:
                        report_file.write(resultone) #then write to file

                report_file.close() #close report file
            else:
                print("[*] no results\n")
                
        filex.close() #close dork dictionary

#---------------------------CHECK DORKS TYPES SELECTED BY USER---------------------------

    def searchs(self):
        for j in self.__dork:
            self.__dork = j.lower()

        print("Remember that DorkMe is Beta!\n Read README¡¡¡ \n please send any proposal, bug etc to telegram: blueudp\n")
        Deprecated=0 # all is false
        Login=0
        Info=0
        Vulns=0
        mydorks=0

        if "all" in self.__dork: # if user selected all (dorks), everything is True
            Login=1
            Vulns=1
            Info=1
            Deprecated=1
        if "login" in self.__dork: #if user selected login, its True etc
            Login=1
        if "vulns" in self.__dork:
            Vulns=1
        if "info" in self.__dork:
            Info=1
        if "deprecated" in self.__dork:
            Deprecated=1
        if "mydorks" in self.__dork:
            mydorks=1

        if Deprecated: #if deprecated is True, (use have selected it), it execute mainfunc with deprecated category, same with info, vulns etc
            print("\033[1;33;40m[*] Using 'Deprecated' Dorks \033[0m " + "\n")
            self.__category = "Deprecated"
            self.mainfunc()
        if Info:
            print("\033[1;33;40m[*] Using 'Info' Dorks \033[0m ")
            self.__category = "Info" #same
            self.mainfunc()
            
        if Vulns:
            print("\033[1;33;40m[*] Using 'Vuln' Dorks \033[0m ")
            self.__category = "Vulns"
            self.mainfunc()
            
        if Login:
            print("\033[1;33;40m[*] Using 'Login' Dorks \033[0m ")
            self.__category = "Login"
            self.mainfunc()
        if mydorks:
            print("\033[1;33;40m[*] Using your dorks \033[0m ")
            self.__category = "mydorks"
            self.mainfunc()  
              
if __name__ == "__main__":  #have no sense execute this directly, so...
     print("[¡] This is a module¡, use DorkMe.py instead")
     exit()
