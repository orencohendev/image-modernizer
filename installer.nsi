; Name of the installer
Outfile "Image_Modernizer_Installer.exe"
InstallDir "$PROGRAMFILES\Image Modernizer"

; Default section
Section

  ; Where to install
  SetOutPath $INSTDIR
  File /oname=$INSTDIR\image_modernizer.exe "dist\image_modernizer.exe"
  CreateShortCut "$DESKTOP\Image Modernizer.lnk" "$INSTDIR\image_modernizer.exe"

  ; Create an uninstaller
  WriteUninstaller $INSTDIR\Uninstaller.exe

SectionEnd

; Optional section for the uninstaller
Section "Uninstall"

  ; Remove the installed file
  Delete $INSTDIR\image_modernizer.exe

  ; Remove the uninstaller
  Delete $INSTDIR\Uninstaller.exe

  ; Remove the install directory
  RMDir $INSTDIR

SectionEnd
