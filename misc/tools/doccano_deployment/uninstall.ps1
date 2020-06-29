Set-ExecutionPolicy Bypass -Scope Process -Force
"y"|choco uninstall git.install -n --skip-autouninstaller
choco uninstall python -y -n --skip-autouninstal
"y"|choco uninstall nodejs --version=13.11.0 -n --skip-autouninstaller
"y"|choco uninstall yarn -n --skip-autouninstaller
"y"|choco uninstall nssm -n --skip-autouninstaller
