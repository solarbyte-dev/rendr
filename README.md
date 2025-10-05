# rendr
 rendr is a simple script i created which serves two simple purposes. Firstly, it enable you to see 'rendered' markdown and secondly, it generates an html file for the same.
 
## installation
 run the following command:
 
 ```bash
 git clone https://github.com/solarbyte-dev/rendr.git && cd rendr && pip install markdown webbrowser --break-system-packages
 ```
 this will install the project and all its dependencies. 
 (the --break-system-packages part is only necessary for distro following pep 668 + mardown and webbrowser are unlikely to break anything)

## usage
 
 ```bash
    python rendr.py {path-to-file}.md
 ```
 this will generate a .html file, which is located alongside the original file and will automatically show this in your default browser.
 
## features
 - minimal dependencies.
 - support for all the basic stuff + tables, code highlighting, footnotes, fenced code blocks, TOC, metadata etc
 - really nothing more.