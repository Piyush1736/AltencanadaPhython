import os

if os.system("which java"):
    # java is not installed

    print("Java Is Not Installed")

    os.system("pip install urllib3")

    cookie = 'Cookie'
    license = 'oraclelicense=accept-securebackup-cookie'
    url = 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-windows-x64.exe'
    filename = 'jdk-8u131-windows-x64.exe'
    opener = urllib2.build_opener()
    opener.addheaders.append((cookie, license))
    f = opener.open(url)
    with open(filename, 'wb+') as save:
        save.write(f.read())

else:
    # java is  installed
    print("Java is  installed on path :")
    print(os.system("which java"))
    print("Version of Java :")
    print(os.system("java -version"))
