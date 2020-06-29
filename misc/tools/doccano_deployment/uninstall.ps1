Set-ExecutionPolicy Bypass -Scope Process -Force
"y"|choco uninstall git.install -n --skipautouninstaller 
choco uninstall python -y -n --skipautouninstaller
"y"|choco uninstall nodejs --version=13.11.0 -n --skipautouninstaller
"y"|choco uninstall yarn -n --skipautouninstaller
"y"|choco uninstall nssm -n --skipautouninstaller
