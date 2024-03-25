import os

askURL = input("Enter the URL:")

#'https' == s[0:5]


if (askURL[0:5] == "https"):

    os.system("curl qrenco.de/" + askURL)

else:

    print()
    print("Give a Valid URL! , Try Again")