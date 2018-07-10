# pipe-scan

pipe-scan is an open source script that automates the process of identifying accessible named pipes.

**The pipe-scan project is sponsored by [CGI](https://www.cgi.com/en).**

Installation
----

You can download pipe-scan by cloning the [Git](https://github.com/p33kab00/pipe-scan) repository:

    git clone https://github.com/p33kab00/pipe-scan.git

pipe-scan works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.

Usage
----

Identify open pipes:

    # python pipe-scan.py 192.168.5.131 139
    [*] pipe-scan 0.1
    [*] by p33kab00 (mudnorb@gmail.com)
    [*] # of checks: 42

    [+] Found open pipe
        netlogon

    [+] Found open pipe
        samr

    [+] Found open pipe
        lsarpc

    [+] Found open pipe
        browser

    [*] Found 4 open pipes in 364 ms.
