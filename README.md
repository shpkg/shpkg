## what is shpkg?
it is a cross-distro package manager that uses shell scripts to install packages. you see, packages are complicated, and most people don't make package their software anyways. then we said,
> what if we made packaging fun and easy so it's more accessible and developer-friendly?

and that started shpkg/shpm's journey.

24.11.2024 (us 11.24.2024) - shpkg/shpm was created

## how does it work?
shpkg first searches for the desired package name ending with .sh in the `https://github.com/shpkg/repo` git repository. if it finds a match, it curl-bashes (to be exact, requests.get()) the script. else, it fails.
## how do i install it?
```bash
pip install shpkg
```
## how do i uninstall it?
```bash
pip uninstall shpkg
```
## how do i use it?
### install a package
```bash
shpkg i <package-name>
```
### uninstall a package
```bash
shpkg x <package-name>
```
### update a package
```bash
shpkg u <package-name>
```
### list installed packages
```bash
shpkg l
```
### update shpkg
```bash
pip install shpkg --upgrade
```
### update all packages
```bash
shpkg ua
```
### help
```bash
shpkg --help
```
### version
```bash
shpkg --version
```
## how do i make a package?
see https://github.com/shpkg/repo/blob/main/README.md
