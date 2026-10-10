Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("Wscript.Shell")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
repoDir = fso.GetParentFolderName(scriptDir)

shell.CurrentDirectory = repoDir

strCommand = "python """ & scriptDir & "\start.py"" """ & repoDir & """"

For Each Arg In WScript.Arguments
    strCommand = strCommand & " """ & replace(Arg, """", """""""") & """"
Next

shell.Run strCommand, 0, false
