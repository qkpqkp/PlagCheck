# encoding: utf-8
# module win32comext.shell.shell
# from C:\Users\Doly\Anaconda3\lib\site-packages\win32comext\shell\shell.pyd
# by generator 1.147
""" A module wrapping Windows Shell functions and interfaces """

# imports
from pywintypes import error


# Variables with simple values

HOTKEYF_ALT = 4
HOTKEYF_CONTROL = 2
HOTKEYF_EXT = 8
HOTKEYF_SHIFT = 1

SLGP_RAWPATH = 4
SLGP_SHORTPATH = 1
SLGP_UNCPRIORITY = 2

SLR_ANY_MATCH = 2

SLR_INVOKE_MSI = 128

SLR_NOLINKINFO = 64
SLR_NOSEARCH = 16
SLR_NOTRACK = 32
SLR_NOUPDATE = 8

SLR_NO_UI = 1

SLR_UPDATE = 4

# functions

def AddressAsPIDL(*args, **kwargs): # real signature unknown
    pass

def AssocCreate(*args, **kwargs): # real signature unknown
    pass

def AssocCreateForClasses(*args, **kwargs): # real signature unknown
    pass

def CIDAAsString(*args, **kwargs): # real signature unknown
    pass

def DragQueryFile(*args, **kwargs): # real signature unknown
    pass

def DragQueryFileW(*args, **kwargs): # real signature unknown
    pass

def DragQueryPoint(*args, **kwargs): # real signature unknown
    pass

def FILEGROUPDESCRIPTORAsString(*args, **kwargs): # real signature unknown
    pass

def GetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    pass

def IsUserAnAdmin(*args, **kwargs): # real signature unknown
    pass

def PIDLAsString(*args, **kwargs): # real signature unknown
    pass

def SetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    pass

def SHAddToRecentDocs(*args, **kwargs): # real signature unknown
    pass

def SHBrowseForFolder(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotify(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotifyDeregister(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotifyRegister(*args, **kwargs): # real signature unknown
    pass

def SHCreateDataObject(*args, **kwargs): # real signature unknown
    pass

def SHCreateDefaultContextMenu(*args, **kwargs): # real signature unknown
    pass

def SHCreateDefaultExtractIcon(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromParsingName(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromRelativeName(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemInKnownFolder(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemWithParent(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellFolderView(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItem(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArray(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromDataObject(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromIDLists(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromShellItem(*args, **kwargs): # real signature unknown
    pass

def SHCreateStreamOnFileEx(*args, **kwargs): # real signature unknown
    pass

def ShellExecuteEx(*args, **kwargs): # real signature unknown
    pass

def SHEmptyRecycleBin(*args, **kwargs): # real signature unknown
    pass

def SHFileOperation(*args, **kwargs): # real signature unknown
    pass

def SHGetDesktopFolder(*args, **kwargs): # real signature unknown
    pass

def SHGetFileInfo(*args, **kwargs): # real signature unknown
    pass

def SHGetFolderLocation(*args, **kwargs): # real signature unknown
    pass

def SHGetFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHGetIDListFromObject(*args, **kwargs): # real signature unknown
    pass

def SHGetInstanceExplorer(*args, **kwargs): # real signature unknown
    pass

def SHGetNameFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHGetPathFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHGetPathFromIDListW(*args, **kwargs): # real signature unknown
    pass

def SHGetSettings(*args, **kwargs): # real signature unknown
    pass

def SHGetSpecialFolderLocation(*args, **kwargs): # real signature unknown
    pass

def SHGetSpecialFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHGetViewStatePropertyBag(*args, **kwargs): # real signature unknown
    pass

def SHILCreateFromPath(*args, **kwargs): # real signature unknown
    pass

def SHOpenFolderAndSelectItems(*args, **kwargs): # real signature unknown
    pass

def SHParseDisplayName(*args, **kwargs): # real signature unknown
    pass

def SHQueryRecycleBin(*args, **kwargs): # real signature unknown
    pass

def SHSetFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHUpdateImage(*args, **kwargs): # real signature unknown
    pass

def StringAsCIDA(*args, **kwargs): # real signature unknown
    pass

def StringAsFILEGROUPDESCRIPTOR(*args, **kwargs): # real signature unknown
    pass

def StringAsPIDL(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

BHID_AssociationArray = None # (!) real value is "IID('{BEA9EF17-82F1-4F60-9284-4F8DB75C3BE9}')"

BHID_DataObject = None # (!) real value is "IID('{B8C0BD9F-ED24-455C-83E6-D5390C4FE8C4}')"

BHID_EnumItems = None # (!) real value is "IID('{94F60519-2850-4924-AA5A-D15E84868039}')"

BHID_Filter = None # (!) real value is "IID('{38D08778-F557-4690-9EBF-BA54706AD8F7}')"

BHID_LinkTargetItem = None # (!) real value is "IID('{3981E228-F559-11D3-8E3A-00C04F6837D5}')"

BHID_PropertyStore = None # (!) real value is "IID('{0384E1A4-1523-439C-A4C8-AB911052F586}')"

BHID_SFObject = None # (!) real value is "IID('{3981E224-F559-11D3-8E3A-00C04F6837D5}')"

BHID_SFUIObject = None # (!) real value is "IID('{3981E225-F559-11D3-8E3A-00C04F6837D5}')"

BHID_SFViewObject = None # (!) real value is "IID('{3981E226-F559-11D3-8E3A-00C04F6837D5}')"

BHID_Storage = None # (!) real value is "IID('{3981E227-F559-11D3-8E3A-00C04F6837D5}')"

BHID_StorageEnum = None # (!) real value is "IID('{4621A4E3-F0D6-4773-8A9C-46E77B174840}')"

BHID_Stream = None # (!) real value is "IID('{1CEBB3AB-7C10-499A-A417-92CA16C4CB83}')"

BHID_ThumbnailHandler = None # (!) real value is "IID('{7B2E650A-8E20-4F4A-B09E-6597AFC72FB0}')"

BHID_Transfer = None # (!) real value is "IID('{D5E346A1-F753-4932-B403-4574800E2498}')"

CGID_DefView = None # (!) real value is "IID('{4AF07F10-D231-11D0-B942-00A0C90312E1}')"

CGID_Explorer = None # (!) real value is "IID('{000214D0-0000-0000-C000-000000000046}')"

CGID_ExplorerBarDoc = None # (!) real value is "IID('{000214D3-0000-0000-C000-000000000046}')"

CGID_ShellDocView = None # (!) real value is "IID('{000214D1-0000-0000-C000-000000000046}')"

CGID_ShellServiceObject = None # (!) real value is "IID('{000214D2-0000-0000-C000-000000000046}')"

CLSID_ActiveDesktop = None # (!) real value is "IID('{75048700-EF1F-11D0-9888-006097DEACF9}')"

CLSID_ApplicationDestinations = None # (!) real value is "IID('{86C14003-4D6B-4EF3-A7B4-0506663B2E68}')"

CLSID_ApplicationDocumentLists = None # (!) real value is "IID('{86BEC222-30F2-47E0-9F25-60D11CD75C28}')"

CLSID_ControlPanel = None # (!) real value is "IID('{21EC2020-3AEA-1069-A2DD-08002B30309D}')"

CLSID_DestinationList = None # (!) real value is "IID('{77F10CF0-3DB5-4966-B520-B7C54FD35ED6}')"

CLSID_DragDropHelper = None # (!) real value is "IID('{4657278A-411B-11D2-839A-00C04FD918D0}')"

CLSID_EnumerableObjectCollection = None # (!) real value is "IID('{2D3468C1-36A7-43B6-AC24-D3F02FD9607A}')"

CLSID_FileOperation = None # (!) real value is "IID('{3AD05575-8857-4850-9277-11B85BDB8E09}')"

CLSID_Internet = None # (!) real value is "IID('{871C5380-42A0-1069-A2EA-08002B30309D}')"

CLSID_InternetShortcut = None # (!) real value is "IID('{FBF23B40-E3F0-101B-8488-00AA003E56F8}')"

CLSID_KnownFolderManager = None # (!) real value is "IID('{4DF0C730-DF9D-4AE3-9153-AA6B82E9795A}')"

CLSID_MyComputer = None # (!) real value is "IID('{20D04FE0-3AEA-1069-A2D8-08002B30309D}')"

CLSID_MyDocuments = None # (!) real value is "IID('{450D8FBA-AD25-11D0-98A8-0800361B1103}')"

CLSID_NetworkDomain = None # (!) real value is "IID('{46E06680-4BF0-11D1-83EE-00A0C90DC849}')"

CLSID_NetworkPlaces = None # (!) real value is "IID('{208D2C60-3AEA-1069-A2D7-08002B30309D}')"

CLSID_NetworkServer = None # (!) real value is "IID('{C0542A90-4BF0-11D1-83EE-00A0C90DC849}')"

CLSID_NetworkShare = None # (!) real value is "IID('{54A754C0-4BF0-11D1-83EE-00A0C90DC849}')"

CLSID_Printers = None # (!) real value is "IID('{2227A280-3AEA-1069-A2DE-08002B30309D}')"

CLSID_RecycleBin = None # (!) real value is "IID('{645FF040-5081-101B-9F08-00AA002F954E}')"

CLSID_ShellDesktop = None # (!) real value is "IID('{00021400-0000-0000-C000-000000000046}')"

CLSID_ShellFSFolder = None # (!) real value is "IID('{F3364BA0-65B9-11CE-A9BA-00AA004AE837}')"

CLSID_ShellItem = None # (!) real value is "IID('{9AC9FBE1-E0A2-4AD6-B4EE-E212013EA917}')"

CLSID_ShellLibrary = None # (!) real value is "IID('{D9B3211D-E57F-4426-AAEF-30A806ADD397}')"

CLSID_ShellLink = None # (!) real value is "IID('{00021401-0000-0000-C000-000000000046}')"

CLSID_TaskbarList = None # (!) real value is "IID('{56FDF344-FD6D-11D0-958A-006097C9A090}')"

EP_AdvQueryPane = None # (!) real value is "IID('{B4E9DB8B-34BA-4C39-B5CC-16A1BD2C411C}')"

EP_Commands = None # (!) real value is "IID('{D9745868-CA5F-4A76-91CD-F5A129FBB076}')"

EP_Commands_Organize = None # (!) real value is "IID('{72E81700-E3EC-4660-BF24-3C3B7B648806}')"

EP_Commands_View = None # (!) real value is "IID('{21F7C32D-EEAA-439B-BB51-37B96FD6A943}')"

EP_DetailsPane = None # (!) real value is "IID('{43ABF98B-89B8-472D-B9CE-E69B8229F019}')"

EP_NavPane = None # (!) real value is "IID('{CB316B22-25F7-42B8-8A09-540D23A43C2F}')"

EP_PreviewPane = None # (!) real value is "IID('{893C63D1-45C8-4D17-BE19-223BE71BE365}')"

EP_QueryPane = None # (!) real value is "IID('{65BCDE4F-4F07-4F27-83A7-1AFCA4DF7DDD}')"

FMTID_AudioSummaryInformation = None # (!) real value is "IID('{64440490-4C8B-11D1-8B70-080036B11A03}')"

FMTID_Briefcase = None # (!) real value is "IID('{328D8B21-7729-4BFC-954C-902B329D56B0}')"

FMTID_Displaced = None # (!) real value is "IID('{9B174B33-40FF-11D2-A27E-00C04FC30871}')"

FMTID_ImageProperties = None # (!) real value is "IID('{14B81DA1-0135-4D31-96D9-6CBFC9671A99}')"

FMTID_ImageSummaryInformation = None # (!) real value is "IID('{6444048F-4C8B-11D1-8B70-080036B11A03}')"

FMTID_InternetSite = None # (!) real value is "IID('{000214A1-0000-0000-C000-000000000046}')"

FMTID_Intshcut = None # (!) real value is "IID('{000214A0-0000-0000-C000-000000000046}')"

FMTID_MediaFileSummaryInformation = None # (!) real value is "IID('{64440492-4C8B-11D1-8B70-080036B11A03}')"

FMTID_Misc = None # (!) real value is "IID('{9B174B34-40FF-11D2-A27E-00C04FC30871}')"

FMTID_Query = None # (!) real value is "IID('{49691C90-7E17-101A-A91C-08002B2ECDA9}')"

FMTID_ShellDetails = None # (!) real value is "IID('{28636AA6-953D-11D2-B5D6-00C04FD918D0}')"

FMTID_Storage = None # (!) real value is "IID('{B725F130-47EF-101A-A5F1-02608C9EEBAC}')"

FMTID_SummaryInformation = None # (!) real value is "IID('{F29F85E0-4FF9-1068-AB91-08002B27B3D9}')"

FMTID_Volume = None # (!) real value is "IID('{9B174B35-40FF-11D2-A27E-00C04FC30871}')"

FMTID_WebView = None # (!) real value is "IID('{F2275480-F782-4291-BD94-F13693513AEC}')"

FOLDERID_AddNewPrograms = None # (!) real value is "IID('{DE61D971-5EBC-4F02-A3A9-6C82895E5C04}')"

FOLDERID_AdminTools = None # (!) real value is "IID('{724EF170-A42D-4FEF-9F26-B60E846FBA4F}')"

FOLDERID_AppUpdates = None # (!) real value is "IID('{A305CE99-F527-492B-8B1A-7E76FA98D6E4}')"

FOLDERID_CDBurning = None # (!) real value is "IID('{9E52AB10-F80D-49DF-ACB8-4330F5687855}')"

FOLDERID_ChangeRemovePrograms = None # (!) real value is "IID('{DF7266AC-9274-4867-8D55-3BD661DE872D}')"

FOLDERID_CommonAdminTools = None # (!) real value is "IID('{D0384E7D-BAC3-4797-8F14-CBA229B392B5}')"

FOLDERID_CommonOEMLinks = None # (!) real value is "IID('{C1BAE2D0-10DF-4334-BEDD-7AA20B227A9D}')"

FOLDERID_CommonPrograms = None # (!) real value is "IID('{0139D44E-6AFE-49F2-8690-3DAFCAE6FFB8}')"

FOLDERID_CommonStartMenu = None # (!) real value is "IID('{A4115719-D62E-491D-AA7C-E74B8BE3B067}')"

FOLDERID_CommonStartup = None # (!) real value is "IID('{82A5EA35-D9CD-47C5-9629-E15D2F714E6E}')"

FOLDERID_CommonTemplates = None # (!) real value is "IID('{B94237E7-57AC-4347-9151-B08C6C32D1F7}')"

FOLDERID_ComputerFolder = None # (!) real value is "IID('{0AC0837C-BBF8-452A-850D-79D08E667CA7}')"

FOLDERID_ConflictFolder = None # (!) real value is "IID('{4BFEFB45-347D-4006-A5BE-AC0CB0567192}')"

FOLDERID_ConnectionsFolder = None # (!) real value is "IID('{6F0CD92B-2E97-45D1-88FF-B0D186B8DEDD}')"

FOLDERID_Contacts = None # (!) real value is "IID('{56784854-C6CB-462B-8169-88E350ACB882}')"

FOLDERID_ControlPanelFolder = None # (!) real value is "IID('{82A74AEB-AEB4-465C-A014-D097EE346D63}')"

FOLDERID_Cookies = None # (!) real value is "IID('{2B0F765D-C0E9-4171-908E-08A611B84FF6}')"

FOLDERID_Desktop = None # (!) real value is "IID('{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}')"

FOLDERID_DeviceMetadataStore = None # (!) real value is "IID('{5CE4A5E9-E4EB-479D-B89F-130C02886155}')"

FOLDERID_Documents = None # (!) real value is "IID('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}')"

FOLDERID_DocumentsLibrary = None # (!) real value is "IID('{7B0DB17D-9CD2-4A93-9733-46CC89022E7C}')"

FOLDERID_Downloads = None # (!) real value is "IID('{374DE290-123F-4565-9164-39C4925E467B}')"

FOLDERID_Favorites = None # (!) real value is "IID('{1777F761-68AD-4D8A-87BD-30B759FA33DD}')"

FOLDERID_Fonts = None # (!) real value is "IID('{FD228CB7-AE11-4AE3-864C-16F3910AB8FE}')"

FOLDERID_Games = None # (!) real value is "IID('{CAC52C1A-B53D-4EDC-92D7-6B2E8AC19434}')"

FOLDERID_GameTasks = None # (!) real value is "IID('{054FAE61-4DD8-4787-80B6-090220C4B700}')"

FOLDERID_History = None # (!) real value is "IID('{D9DC8A3B-B784-432E-A781-5A1130A75963}')"

FOLDERID_HomeGroup = None # (!) real value is "IID('{52528A6B-B9E3-4ADD-B60D-588C2DBA842D}')"

FOLDERID_ImplicitAppShortcuts = None # (!) real value is "IID('{BCB5256F-79F6-4CEE-B725-DC34E402FD46}')"

FOLDERID_InternetCache = None # (!) real value is "IID('{352481E8-33BE-4251-BA85-6007CAEDCF9D}')"

FOLDERID_InternetFolder = None # (!) real value is "IID('{4D9F7874-4E0C-4904-967B-40B0D20C3E4B}')"

FOLDERID_Libraries = None # (!) real value is "IID('{1B3EA5DC-B587-4786-B4EF-BD1DC332AEAE}')"

FOLDERID_Links = None # (!) real value is "IID('{BFB9D5E0-C6A9-404C-B2B2-AE6DB6AF4968}')"

FOLDERID_LocalAppData = None # (!) real value is "IID('{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}')"

FOLDERID_LocalAppDataLow = None # (!) real value is "IID('{A520A1A4-1780-4FF6-BD18-167343C5AF16}')"

FOLDERID_LocalizedResourcesDir = None # (!) real value is "IID('{2A00375E-224C-49DE-B8D1-440DF7EF3DDC}')"

FOLDERID_Music = None # (!) real value is "IID('{4BD8D571-6D19-48D3-BE97-422220080E43}')"

FOLDERID_MusicLibrary = None # (!) real value is "IID('{2112AB0A-C86A-4FFE-A368-0DE96E47012E}')"

FOLDERID_NetHood = None # (!) real value is "IID('{C5ABBF53-E17F-4121-8900-86626FC2C973}')"

FOLDERID_NetworkFolder = None # (!) real value is "IID('{D20BEEC4-5CA8-4905-AE3B-BF251EA09B53}')"

FOLDERID_OriginalImages = None # (!) real value is "IID('{2C36C0AA-5812-4B87-BFD0-4CD0DFB19B39}')"

FOLDERID_PhotoAlbums = None # (!) real value is "IID('{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}')"

FOLDERID_Pictures = None # (!) real value is "IID('{33E28130-4E1E-4676-835A-98395C3BC3BB}')"

FOLDERID_PicturesLibrary = None # (!) real value is "IID('{A990AE9F-A03B-4E80-94BC-9912D7504104}')"

FOLDERID_Playlists = None # (!) real value is "IID('{DE92C1C7-837F-4F69-A3BB-86E631204A23}')"

FOLDERID_PrintersFolder = None # (!) real value is "IID('{76FC4E2D-D6AD-4519-A663-37BD56068185}')"

FOLDERID_PrintHood = None # (!) real value is "IID('{9274BD8D-CFD1-41C3-B35E-B13F55A758F4}')"

FOLDERID_Profile = None # (!) real value is "IID('{5E6C858F-0E22-4760-9AFE-EA3317B67173}')"

FOLDERID_ProgramData = None # (!) real value is "IID('{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}')"

FOLDERID_ProgramFiles = None # (!) real value is "IID('{905E63B6-C1BF-494E-B29C-65B732D3D21A}')"

FOLDERID_ProgramFilesCommon = None # (!) real value is "IID('{F7F1ED05-9F6D-47A2-AAAE-29D317C6F066}')"

FOLDERID_ProgramFilesCommonX64 = None # (!) real value is "IID('{6365D5A7-0F0D-45E5-87F6-0DA56B6A4F7D}')"

FOLDERID_ProgramFilesCommonX86 = None # (!) real value is "IID('{DE974D24-D9C6-4D3E-BF91-F4455120B917}')"

FOLDERID_ProgramFilesX64 = None # (!) real value is "IID('{6D809377-6AF0-444B-8957-A3773F02200E}')"

FOLDERID_ProgramFilesX86 = None # (!) real value is "IID('{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}')"

FOLDERID_Programs = None # (!) real value is "IID('{A77F5D77-2E2B-44C3-A6A2-ABA601054A51}')"

FOLDERID_Public = None # (!) real value is "IID('{DFDF76A2-C82A-4D63-906A-5644AC457385}')"

FOLDERID_PublicDesktop = None # (!) real value is "IID('{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}')"

FOLDERID_PublicDocuments = None # (!) real value is "IID('{ED4824AF-DCE4-45A8-81E2-FC7965083634}')"

FOLDERID_PublicDownloads = None # (!) real value is "IID('{3D644C9B-1FB8-4F30-9B45-F670235F79C0}')"

FOLDERID_PublicGameTasks = None # (!) real value is "IID('{DEBF2536-E1A8-4C59-B6A2-414586476AEA}')"

FOLDERID_PublicLibraries = None # (!) real value is "IID('{48DAF80B-E6CF-4F4E-B800-0E69D84EE384}')"

FOLDERID_PublicMusic = None # (!) real value is "IID('{3214FAB5-9757-4298-BB61-92A9DEAA44FF}')"

FOLDERID_PublicPictures = None # (!) real value is "IID('{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}')"

FOLDERID_PublicRingtones = None # (!) real value is "IID('{E555AB60-153B-4D17-9F04-A5FE99FC15EC}')"

FOLDERID_PublicVideos = None # (!) real value is "IID('{2400183A-6185-49FB-A2D8-4A392A602BA3}')"

FOLDERID_QuickLaunch = None # (!) real value is "IID('{52A4F021-7B75-48A9-9F6B-4B87A210BC8F}')"

FOLDERID_Recent = None # (!) real value is "IID('{AE50C081-EBD2-438A-8655-8A092E34987A}')"

FOLDERID_RecordedTVLibrary = None # (!) real value is "IID('{1A6FDBA2-F42D-4358-A798-B74D745926C5}')"

FOLDERID_RecycleBinFolder = None # (!) real value is "IID('{B7534046-3ECB-4C18-BE4E-64CD4CB7D6AC}')"

FOLDERID_ResourceDir = None # (!) real value is "IID('{8AD10C31-2ADB-4296-A8F7-E4701232C972}')"

FOLDERID_Ringtones = None # (!) real value is "IID('{C870044B-F49E-4126-A9C3-B52A1FF411E8}')"

FOLDERID_RoamingAppData = None # (!) real value is "IID('{3EB685DB-65F9-4CF6-A03A-E3EF65729F3D}')"

FOLDERID_SampleMusic = None # (!) real value is "IID('{B250C668-F57D-4EE1-A63C-290EE7D1AA1F}')"

FOLDERID_SamplePictures = None # (!) real value is "IID('{C4900540-2379-4C75-844B-64E6FAF8716B}')"

FOLDERID_SamplePlaylists = None # (!) real value is "IID('{15CA69B3-30EE-49C1-ACE1-6B5EC372AFB5}')"

FOLDERID_SampleVideos = None # (!) real value is "IID('{859EAD94-2E85-48AD-A71A-0969CB56A6CD}')"

FOLDERID_SavedGames = None # (!) real value is "IID('{4C5C32FF-BB9D-43B0-B5B4-2D72E54EAAA4}')"

FOLDERID_SavedSearches = None # (!) real value is "IID('{7D1D3A04-DEBB-4115-95CF-2F29DA2920DA}')"

FOLDERID_SearchHome = None # (!) real value is "IID('{190337D1-B8CA-4121-A639-6D472D16972A}')"

FOLDERID_SEARCH_CSC = None # (!) real value is "IID('{EE32E446-31CA-4ABA-814F-A5EBD2FD6D5E}')"

FOLDERID_SEARCH_MAPI = None # (!) real value is "IID('{98EC0E18-2098-4D44-8644-66979315A281}')"

FOLDERID_SendTo = None # (!) real value is "IID('{8983036C-27C0-404B-8F08-102D10DCFD74}')"

FOLDERID_SidebarDefaultParts = None # (!) real value is "IID('{7B396E54-9EC5-4300-BE0A-2482EBAE1A26}')"

FOLDERID_SidebarParts = None # (!) real value is "IID('{A75D362E-50FC-4FB7-AC2C-A8BEAA314493}')"

FOLDERID_StartMenu = None # (!) real value is "IID('{625B53C3-AB48-4EC1-BA1F-A1EF4146FC19}')"

FOLDERID_Startup = None # (!) real value is "IID('{B97D20BB-F46A-4C97-BA10-5E3608430854}')"

FOLDERID_SyncManagerFolder = None # (!) real value is "IID('{43668BF8-C14E-49B2-97C9-747784D784B7}')"

FOLDERID_SyncResultsFolder = None # (!) real value is "IID('{289A9A43-BE44-4057-A41B-587A76D7E7F9}')"

FOLDERID_SyncSetupFolder = None # (!) real value is "IID('{0F214138-B1D3-4A90-BBA9-27CBC0C5389A}')"

FOLDERID_System = None # (!) real value is "IID('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}')"

FOLDERID_SystemX86 = None # (!) real value is "IID('{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}')"

FOLDERID_Templates = None # (!) real value is "IID('{A63293E8-664E-48DB-A079-DF759E0509F7}')"

FOLDERID_UserPinned = None # (!) real value is "IID('{9E3995AB-1F9C-4F13-B827-48B24B6C7174}')"

FOLDERID_UserProfiles = None # (!) real value is "IID('{0762D272-C50A-4BB0-A382-697DCD729B80}')"

FOLDERID_UserProgramFiles = None # (!) real value is "IID('{5CD7AEE2-2219-4A67-B85D-6C9CE15660CB}')"

FOLDERID_UserProgramFilesCommon = None # (!) real value is "IID('{BCBD3057-CA5C-4622-B42D-BC56DB0AE516}')"

FOLDERID_UsersFiles = None # (!) real value is "IID('{F3CE0F7C-4901-4ACC-8648-D5D44B04EF8F}')"

FOLDERID_UsersLibraries = None # (!) real value is "IID('{A302545D-DEFF-464B-ABE8-61C8648D939B}')"

FOLDERID_Videos = None # (!) real value is "IID('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}')"

FOLDERID_VideosLibrary = None # (!) real value is "IID('{491E922F-5643-4AF4-A7EB-4E7A138D8174}')"

FOLDERID_Windows = None # (!) real value is "IID('{F38BF404-1D43-42F2-9305-67DE0B28FC23}')"

FOLDERTYPEID_Communications = None # (!) real value is "IID('{91475FE5-586B-4EBA-8D75-D17434B8CDF6}')"

FOLDERTYPEID_CompressedFolder = None # (!) real value is "IID('{80213E82-BCFD-4C4F-8817-BB27601267A9}')"

FOLDERTYPEID_Contacts = None # (!) real value is "IID('{DE2B70EC-9BF7-4A93-BD3D-243F7881D492}')"

FOLDERTYPEID_ControlPanelCategory = None # (!) real value is "IID('{DE4F0660-FA10-4B8F-A494-068B20B22307}')"

FOLDERTYPEID_ControlPanelClassic = None # (!) real value is "IID('{0C3794F3-B545-43AA-A329-C37430C58D2A}')"

FOLDERTYPEID_Documents = None # (!) real value is "IID('{7D49D726-3C21-4F05-99AA-FDC2C9474656}')"

FOLDERTYPEID_Games = None # (!) real value is "IID('{B689B0D0-76D3-4CBB-87F7-585D0E0CE070}')"

FOLDERTYPEID_Generic = None # (!) real value is "IID('{5C4F28B5-F869-4E84-8E60-F11DB97C5CC7}')"

FOLDERTYPEID_GenericLibrary = None # (!) real value is "IID('{5F4EAB9A-6833-4F61-899D-31CF46979D49}')"

FOLDERTYPEID_GenericSearchResults = None # (!) real value is "IID('{7FDE1A1E-8B31-49A5-93B8-6BE14CFA4943}')"

FOLDERTYPEID_Invalid = None # (!) real value is "IID('{57807898-8C4F-4462-BB63-71042380B109}')"

FOLDERTYPEID_Music = None # (!) real value is "IID('{94D6DDCC-4A68-4175-A374-BD584A510B78}')"

FOLDERTYPEID_NetworkExplorer = None # (!) real value is "IID('{25CC242B-9A7C-4F51-80E0-7A2928FEBE42}')"

FOLDERTYPEID_OpenSearch = None # (!) real value is "IID('{8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}')"

FOLDERTYPEID_OtherUsers = None # (!) real value is "IID('{B337FD00-9DD5-4635-A6D4-DA33FD102B7A}')"

FOLDERTYPEID_Pictures = None # (!) real value is "IID('{B3690E58-E961-423B-B687-386EBFD83239}')"

FOLDERTYPEID_Printers = None # (!) real value is "IID('{2C7BBEC6-C844-4A0A-91FA-CEF6F59CFDA1}')"

FOLDERTYPEID_PublishedItems = None # (!) real value is "IID('{7F2F5B96-FF74-41DA-AFD8-1C78A5F3AEA2}')"

FOLDERTYPEID_RecordedTV = None # (!) real value is "IID('{5557A28F-5DA6-4F83-8809-C2C98A11A6FA}')"

FOLDERTYPEID_RecycleBin = None # (!) real value is "IID('{D6D9E004-CD87-442B-9D57-5E0AEB4F6F72}')"

FOLDERTYPEID_SavedGames = None # (!) real value is "IID('{D0363307-28CB-4106-9F23-2956E3E5E0E7}')"

FOLDERTYPEID_SearchConnector = None # (!) real value is "IID('{982725EE-6F47-479E-B447-812BFA7D2E8F}')"

FOLDERTYPEID_Searches = None # (!) real value is "IID('{0B0BA2E3-405F-415E-A6EE-CAD625207853}')"

FOLDERTYPEID_SearchHome = None # (!) real value is "IID('{834D8A44-0974-4ED6-866E-F203D80B3810}')"

FOLDERTYPEID_SoftwareExplorer = None # (!) real value is "IID('{D674391B-52D9-4E07-834E-67C98610F39D}')"

FOLDERTYPEID_StartMenu = None # (!) real value is "IID('{EF87B4CB-F2CE-4785-8658-4CA6C63E38C6}')"

FOLDERTYPEID_UserFiles = None # (!) real value is "IID('{CD0FC69B-71E2-46E5-9690-5BCD9F57AAB3}')"

FOLDERTYPEID_UsersLibraries = None # (!) real value is "IID('{C4D98F09-6124-4FE0-9942-826416082DA9}')"

FOLDERTYPEID_Videos = None # (!) real value is "IID('{5FA96407-7E77-483C-AC93-691D05850DE8}')"

IID_CDefView = None # (!) real value is "IID('{4434FF80-EF4C-11CE-AE65-08002B2E1262}')"

IID_IActiveDesktop = None # (!) real value is "IID('{F490EB00-1240-11D1-9888-006097DEACF9}')"

IID_IActiveDesktopP = None # (!) real value is "IID('{52502EE0-EC80-11D0-89AB-00C04FC2972D}')"

IID_IADesktopP2 = None # (!) real value is "IID('{B22754E2-4574-11D1-9888-006097DEACF9}')"

IID_IApplicationDestinations = None # (!) real value is "IID('{12337D35-94C6-48A0-BCE7-6A9C69D4D600}')"

IID_IApplicationDocumentLists = None # (!) real value is "IID('{3C594F9F-9F30-47A1-979A-C9E83D3D0A06}')"

IID_IAsyncOperation = None # (!) real value is "IID('{3D8B0590-F691-11D2-8EA9-006097DF5BD4}')"

IID_IBrowserFrameOptions = None # (!) real value is "IID('{10DF43C8-1DBE-11D3-8B34-006097DF5BD4}')"

IID_ICategorizer = None # (!) real value is "IID('{A3B14589-9174-49A8-89A3-06A1AE2B9BA7}')"

IID_ICategoryProvider = None # (!) real value is "IID('{9AF64809-5864-4C26-A720-C1F78C086EE3}')"

IID_IColumnProvider = None # (!) real value is "IID('{E8025004-1C42-11D2-BE2C-00A0C9A83DA1}')"

IID_IContextMenu = None # (!) real value is "IID('{000214E4-0000-0000-C000-000000000046}')"

IID_IContextMenu2 = None # (!) real value is "IID('{000214F4-0000-0000-C000-000000000046}')"

IID_IContextMenu3 = None # (!) real value is "IID('{BCFCE0A0-EC17-11D0-8D10-00A0C90F2719}')"

IID_ICopyHook = None # (!) real value is "IID('{000214EF-0000-0000-C000-000000000046}')"

IID_ICopyHookA = None # (!) real value is "IID('{000214EF-0000-0000-C000-000000000046}')"

IID_ICopyHookW = None # (!) real value is "IID('{000214FC-0000-0000-C000-000000000046}')"

IID_ICurrentItem = None # (!) real value is "IID('{240A7174-D653-4A1D-A6D3-D4943CFBFE3D}')"

IID_ICustomDestinationList = None # (!) real value is "IID('{6332DEBF-87B5-4670-90C0-5E57B408A49E}')"

IID_IDefaultExtractIconInit = None # (!) real value is "IID('{41DED17D-D6B3-4261-997D-88C60E4B1D58}')"

IID_IDeskBand = None # (!) real value is "IID('{EB0FE172-1A3A-11D0-89B3-00A0C90A90AC}')"

IID_IDisplayItem = None # (!) real value is "IID('{C6FD5997-9F6B-4888-8703-94E80E8CDE3F}')"

IID_IDockingWindow = None # (!) real value is "IID('{012DD920-7B26-11D0-8CA9-00A0C92DBFE8}')"

IID_IDropTargetHelper = None # (!) real value is "IID('{4657278B-411B-11D2-839A-00C04FD918D0}')"

IID_IEmptyVolumeCache = None # (!) real value is "IID('{8FCE5227-04DA-11D1-A004-00805F8ABE06}')"

IID_IEmptyVolumeCache2 = None # (!) real value is "IID('{02B7E3BA-4DB3-11D2-B2D9-00C04F8EEC8C}')"

IID_IEmptyVolumeCacheCallBack = None # (!) real value is "IID('{6E793361-73C6-11D0-8469-00AA00442901}')"

IID_IEnumExplorerCommand = None # (!) real value is "IID('{A88826F8-186F-4987-AADE-EA0CEF8FBFE8}')"

IID_IEnumIDList = None # (!) real value is "IID('{000214F2-0000-0000-C000-000000000046}')"

IID_IEnumObjects = None # (!) real value is "IID('{2C1C7E2E-2D0E-4059-831E-1E6F82335C2E}')"

IID_IEnumResources = None # (!) real value is "IID('{2DD81FE3-A83C-4DA9-A330-47249D345BA1}')"

IID_IEnumShellItems = None # (!) real value is "IID('{70629033-E363-4A28-A567-0DB78006E6D7}')"

IID_IExplorerBrowser = None # (!) real value is "IID('{DFD3B6B5-C10C-4BE9-85F6-A66969F402F6}')"

IID_IExplorerBrowserEvents = None # (!) real value is "IID('{361BBDC7-E6EE-4E13-BE58-58E2240C810F}')"

IID_IExplorerCommand = None # (!) real value is "IID('{A08CE4D0-FA25-44AB-B57C-C7B1C323E0B9}')"

IID_IExplorerCommandProvider = None # (!) real value is "IID('{64961751-0835-43C0-8FFE-D57686530E64}')"

IID_IExplorerPaneVisibility = None # (!) real value is "IID('{E07010EC-BC17-44C0-97B0-46C7C95B9EDC}')"

IID_IExtractIcon = None # (!) real value is "IID('{000214FA-0000-0000-C000-000000000046}')"

IID_IExtractIconW = None # (!) real value is "IID('{000214FA-0000-0000-C000-000000000046}')"

IID_IExtractImage = None # (!) real value is "IID('{BB2E617C-0920-11D1-9A0B-00C04FC2D6C1}')"

IID_IFileOperation = None # (!) real value is "IID('{947AAB5F-0A5C-4C13-B4D6-4BF7836FC9F8}')"

IID_IFileOperationProgressSink = None # (!) real value is "IID('{04B0F1A7-9490-44BC-96E1-4296A31252E2}')"

IID_IIdentityName = None # (!) real value is "IID('{7D903FCA-D6F9-4810-8332-946C0177E247}')"

IID_IKnownFolder = None # (!) real value is "IID('{3AA7AF7E-9B36-420C-A8E3-F77D4674A488}')"

IID_IKnownFolderManager = None # (!) real value is "IID('{8BE2D872-86AA-4D47-B776-32CCA40C7018}')"

IID_INameSpaceTreeControl = None # (!) real value is "IID('{028212A3-B627-47E9-8856-C14265554E4F}')"

IID_IObjectArray = None # (!) real value is "IID('{92CA9DCD-5622-4BBA-A805-5E9F541BD8C9}')"

IID_IObjectCollection = None # (!) real value is "IID('{5632B1A4-E38A-400A-928A-D4CD63230295}')"

IID_IPersistFolder = None # (!) real value is "IID('{000214EA-0000-0000-C000-000000000046}')"

IID_IPersistFolder2 = None # (!) real value is "IID('{1AC3D9F0-175C-11D1-95BE-00609797EA4F}')"

IID_IQueryAssociations = None # (!) real value is "IID('{C46CA590-3C3F-11D2-BEE6-0000F805CA57}')"

IID_IRelatedItem = None # (!) real value is "IID('{A73CE67A-8AB1-44F1-8D43-D2FCBF6B1CD0}')"

IID_IShellBrowser = None # (!) real value is "IID('{000214E2-0000-0000-C000-000000000046}')"

IID_IShellCopyHook = None # (!) real value is "IID('{000214FC-0000-0000-C000-000000000046}')"

IID_IShellCopyHookA = None # (!) real value is "IID('{000214EF-0000-0000-C000-000000000046}')"

IID_IShellCopyHookW = None # (!) real value is "IID('{000214FC-0000-0000-C000-000000000046}')"

IID_IShellExtInit = None # (!) real value is "IID('{000214E8-0000-0000-C000-000000000046}')"

IID_IShellFolder = None # (!) real value is "IID('{000214E6-0000-0000-C000-000000000046}')"

IID_IShellFolder2 = None # (!) real value is "IID('{93F2F68C-1D1B-11D3-A30E-00C04F79ABD1}')"

IID_IShellIcon = None # (!) real value is "IID('{000214E5-0000-0000-C000-000000000046}')"

IID_IShellIconOverlay = None # (!) real value is "IID('{7D688A70-C613-11D0-999B-00C04FD655E1}')"

IID_IShellIconOverlayIdentifier = None # (!) real value is "IID('{0C6C4200-C589-11D0-999A-00C04FD655E1}')"

IID_IShellIconOverlayManager = None # (!) real value is "IID('{F10B5E34-DD3B-42A7-AA7D-2F4EC54BB09B}')"

IID_IShellItem = None # (!) real value is "IID('{43826D1E-E718-42EE-BC55-A1E261C37BFE}')"

IID_IShellItem2 = None # (!) real value is "IID('{7E9FB0D3-919F-4307-AB2E-9B1860310C93}')"

IID_IShellItemArray = None # (!) real value is "IID('{B63EA76D-1F85-456F-A19C-48159EFA858B}')"

IID_IShellItemResources = None # (!) real value is "IID('{FF5693BE-2CE0-4D48-B5C5-40817D1ACDB9}')"

IID_IShellLibrary = None # (!) real value is "IID('{11A66EFA-382E-451A-9234-1E0E12EF3085}')"

IID_IShellLink = None # (!) real value is "IID('{000214F9-0000-0000-C000-000000000046}')"

IID_IShellLinkA = None # (!) real value is "IID('{000214EE-0000-0000-C000-000000000046}')"

IID_IShellLinkDataList = None # (!) real value is "IID('{45E2B4AE-B1C3-11D0-B92F-00A0C90312E1}')"

IID_IShellLinkW = None # (!) real value is "IID('{000214F9-0000-0000-C000-000000000046}')"

IID_IShellView = None # (!) real value is "IID('{000214E3-0000-0000-C000-000000000046}')"

IID_ITaskbarList = None # (!) real value is "IID('{56FDF342-FD6D-11D0-958A-006097C9A090}')"

IID_ITransferAdviseSink = None # (!) real value is "IID('{D594D0D8-8DA7-457B-B3B4-CE5DBAAC0B88}')"

IID_ITransferDestination = None # (!) real value is "IID('{48ADDD32-3CA5-4124-ABE3-B5A72531B207}')"

IID_ITransferMediumItem = None # (!) real value is "IID('{77F295D5-2D6F-4E19-B8AE-322F3E721AB5}')"

IID_ITransferSource = None # (!) real value is "IID('{00ADB003-BDE9-45C6-8E29-D09F9353E108}')"

IID_IUniformResourceLocator = None # (!) real value is "IID('{CABB0DA0-DA57-11CF-9974-0020AFD79762}')"

ResourceTypeStream = None # (!) real value is "IID('{4F74D1CF-680C-4EA3-8020-4BDA6792DA3C}')"

SID_CtxQueryAssociations = None # (!) real value is "IID('{FAADFC40-B777-4B69-AA81-77035EF0E6E8}')"

SID_DefView = None # (!) real value is "IID('{6D12FE80-7911-11CF-9534-0000C05BAE0B}')"

SID_LinkSite = None # (!) real value is "IID('{000214F9-0000-0000-C000-000000000046}')"

SID_MenuShellFolder = None # (!) real value is "IID('{A6C17EB4-2D65-11D2-838F-00C04FD918D0}')"

SID_SCommDlgBrowser = None # (!) real value is "IID('{80F30233-B7DF-11D2-A33B-006097DF5BD4}')"

SID_SGetViewFromViewDual = None # (!) real value is "IID('{889A935D-971E-4B12-B90C-24DFC9E1E5E8}')"

SID_ShellFolderViewCB = None # (!) real value is "IID('{2047E320-F2A9-11CE-AE65-08002B2E1262}')"

SID_SInternetExplorer = None # (!) real value is "IID('{0002DF05-0000-0000-C000-000000000046}')"

SID_SMenuBandBKContextMenu = None # (!) real value is "IID('{164BBD86-1D0D-4DE0-9A3B-D9729647C2B8}')"

SID_SMenuBandBottom = None # (!) real value is "IID('{743CA664-0DEB-11D1-9825-00C04FD91972}')"

SID_SMenuBandBottomSelected = None # (!) real value is "IID('{165EBAF4-6D51-11D2-83AD-00C04FD918D0}')"

SID_SMenuBandChild = None # (!) real value is "IID('{ED9CC020-08B9-11D1-9823-00C04FD91972}')"

SID_SMenuBandContextMenuModifier = None # (!) real value is "IID('{39545874-7162-465E-B783-2AA1874FEF81}')"

SID_SMenuBandParent = None # (!) real value is "IID('{8C278EEC-3EAB-11D1-8CB0-00C04FD918D0}')"

SID_SMenuBandTop = None # (!) real value is "IID('{9493A810-EC38-11D0-BC46-00AA006CE2F5}')"

SID_SMenuPopup = None # (!) real value is "IID('{D1E7AFEB-6A2E-11D0-8C78-00C04FD918B4}')"

SID_SProgressUI = None # (!) real value is "IID('{F8383852-FCD3-11D1-A6B9-006097DF5BD4}')"

SID_SShellBrowser = None # (!) real value is "IID('{000214E2-0000-0000-C000-000000000046}')"

SID_SShellDesktop = None # (!) real value is "IID('{00021400-0000-0000-C000-000000000046}')"

SID_STopLevelBrowser = None # (!) real value is "IID('{4C96BE40-915C-11CF-99D3-00AA004AE837}')"

SID_STopWindow = None # (!) real value is "IID('{49E1B500-4636-11D3-97F7-00C04F45D0B3}')"

SID_SUrlHistory = None # (!) real value is "IID('{3C374A40-BAE4-11CF-BF7D-00AA006946EE}')"

SID_SWebBrowserApp = None # (!) real value is "IID('{0002DF05-0000-0000-C000-000000000046}')"

VID_Details = None # (!) real value is "IID('{137E7700-3573-11CF-AE69-08002B2E1262}')"

VID_LargeIcons = None # (!) real value is "IID('{0057D0E0-3573-11CF-AE69-08002B2E1262}')"

VID_List = None # (!) real value is "IID('{0E1FA5E0-3573-11CF-AE69-08002B2E1262}')"

VID_SmallIcons = None # (!) real value is "IID('{089000C0-3573-11CF-AE69-08002B2E1262}')"

VID_Thumbnails = None # (!) real value is "IID('{8BEBB290-52D0-11D0-B7F4-00C04FD706EC}')"

VID_ThumbStrip = None # (!) real value is "IID('{8EEFA624-D1E9-445B-94B7-74FBCE2EA11A}')"

VID_Tile = None # (!) real value is "IID('{65F125E5-7BE1-4810-BA9D-D271C8432CE3}')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016C86AA91D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='win32comext.shell.shell', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016C86AA91D0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\win32comext\\\\shell\\\\shell.pyd')"

