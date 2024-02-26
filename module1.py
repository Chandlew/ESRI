# -*- coding: utf-8 -*-
""" INFO:
Created on: Jan 5, 2023
Last updated on: Jan 5, 2023
Author: Brian Russell
Email: brian.russell@lumen.com

Description: This file contains Classes and Variables that are used by multiple scripts for FMGIS. 
The classes are intended to be used as a way to organize frequently used variables.
Classes and Variables in this file can be added or modified as needed.
"""
""" README:
    Using this File requires the following:
    The code below allows the gis_config module to be imported from the parent directory.
    We need to find a way to make this work without having to add the above code to every script that uses this file.
    Enter these 5 lines of code at the beginning of any script that uses this file:

        import sys, os
        # Imports gis_config.py from the parent directory
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import gis_config


    As an alternative, you can try to add the parent directory to the PYTHONPATH environment variable, but this doesnt work for me.
    1. Add the directory that contains the gis_config.py file to the PYTHONPATH environment variable.
      You can set the PYTHONPATH environment variable in Windows to include directories that Python will add to the sys.path directory list. 
      Open the System Properties (Right click Computer in the start menu, or use the keyboard shortcut Win+Pause)
      Click Advanced system settings
      Click Environment Variables
      Click New in the System variables section
      Enter PYTHONPATH in the Variable name field
      Enter the path to the directory in the Variable value field. If you're adding multiple paths, separate them with a semicolon (;)
      Click OK, then Apply, then OK again
      Now, Python will look in the directories you added to PYTHONPATH when you try to import a module. 
      Note that you'll need to restart your command prompt or IDE for the changes to take effect.
    2. Restart your command prompt or IDE.
    3. Try importing the gis_config module again 
"""

## Paths to servers on the network
class Server:
    nngis3 = r'\\nadnp1b_cifs.corp.intranet\NNSGIS3\\' # J: drive

## SDE Connections to Portal Feature Classes
class Connections:
    prd2 =      Server.nngis3 + r'ArcMap\Connections\GISPRD2_NETWORK_DATA.sde\\'
    prd3_ro =   Server.nngis3 + r'ArcMap\Connections\NXPRD3_GISREAD.sde\\'
    telecom =   Server.nngis3 + r'ArcMap\Connections\NXPRD3_GISREAD.sde\NX_DATA.TelecomDatasetProjection\\'# Need to figure out self referencing classes to avoid having to use the full path
    ctl_data =  Server.nngis3 + r'ArcMap\Connections\NXPRD3_GISREAD.sde\NX_DATA.CTLDataset\\'
    tomtom =    Server.nngis3 + r'ArcMap\Connections\USDED000_TOMTOM_RO.sde\\'

## File Paths to directories
class Path:
    projects =      Server.nngis3 + r'ArcMap_Main\projects\\'
    production =    Server.nngis3 + r'ArcMap_Main\python\prod\\'
    backup =        Server.nngis3 + r'ArcMap_Main\data\backup\\'
    temp =          r'memory\Temp_Assignment'

## Portal Feature Classes
class PortalFC:
    clarify_queue =     Connections.prd2 +  'GIS_DATA.CLARIFY_QUEUE'
    ctl_national_cost = Connections.telecom + 'NX_DATA.CTL_National_Cost_Polygons'
    dispatch_area =     Connections.prd2 + 'NETWORK_DATA.DISPATCH_AREA'
    ecn =               Connections.prd2 + 'NETWORK_DATA.ECN'
    metro_markets =     Connections.telecom + 'NX_DATA.METRO_MARKETS'
    natl_division =     Connections.prd2 + 'GIS_DATA.Natl_Division'
    non_cpe_shipping =  Connections.prd2 + 'NETWORK_DATA.NON_CPE_SHIPPING'
    np_i_planning =     Connections.prd2 + 'GIS_DATA.NP_I_Planning'
    oncall =            Connections.prd2 + 'GIS_DATA.ONCALL'
    ospe =              Connections.prd2 + 'GIS_DATA.OSPE'
    pricing_area =      Connections.prd2 + 'NETWORK_DATA.PRICING_AREA'
    serving_areas =     Connections.prd2 + 'NETWORK_DATA.SERVING_AREAS_COMBINED'               
    state_coverage =    Connections.prd2 + 'GIS_DATA.State_Coverage'
    
class NetworkFC:
    natroute =      Connections.telecom + 'NX_DATA.route'
    locUGroute =    Connections.ctl_data + 'NX_DATA.CTL_Local_Copper_UG_Route'
    locAEroute =    Connections.ctl_data + 'NX_DATA.CTL_Local_Copper_UG_Route'
    
class GeoRef:
    tsr =           Connections.tomtom + 'NX_DATA.TOWNSHIP_SECTION_RANGE_NEW'
    county =        Connections.tomtom + 'TOMTOM.US_COUNTY'
    city =          Connections.tomtom + 'TOMTOM.US_CITY'      
    state =         Connections.tomtom + 'TOMTOM.US_STATE' 
    majorstreets =  Connections.tomtom + 'TOMTOM.US_MN_02'
    hwy =           Connections.tomtom + 'TOMTOM.US_MN_01'
    interstate =    Connections.tomtom + 'TOMTOM.US_MN_00'
    rail =          Connections.tomtom + 'TOMTOM.US_MN_RR'

## Mail Lists for tools_fmgis.email_send
class Emails:
    
    brian =     ["brian.russell@lumen.com"]
    devs =      ["brian.russell@lumen.com", "john.firnschild@lumen.com"]
    dispatch =  ["john.firnschild@lumen.com", "brian.russell@lumen.com", "kia.vue@lumen.com", "carissa.h.mcgibbon@lumen.com", "Katie.Cone@lumen.com"]
    national_records =  "national.records@centurylink.com" # Generic email for sending from National Records
