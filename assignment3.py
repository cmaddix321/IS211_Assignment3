import urllib.request
import argparse
import re

# other imports go here
# http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv

def pullfile(url):
    response = urllib.request.urlopen(url)
    file_content = response.read().decode('utf-8')
    data = file_content.split("\r\n")
    return data

def searchimg(lst):
    pattern = "\.PNG|\.png|\.jpg|\.gif|\.jpeg|\.GIF"
    countimg = 0
    for line in lst:
        if re.search(pattern,line):
            countimg +=1
    avg = countimg/(len(lst)-1)
    avg *= 100
    output = ("{0}% of searches were images.".format(avg))
    return output

def searchbr(lst):
    browser1 = "Firefox"
    browser2 = "Chrome"
    browser3 = "Internet Explorer"
    browser4 = "Safari"
    countFf = 0
    countC = 0
    countIE = 0
    countS = 0
    for line in lst:
        if re.search(browser1,line):
            countFf +=1
        if re.search(browser2,line):
            countC +=1
        if re.search(browser3,line):
            countIE +=1
        if re.search(browser4,line):
            countS +=1

    countlist = [countS,countIE,countFf,countC]

    x = countS
    if countFf == x:
        output = ("{0} is the most used browser.".format(browser1))

    elif countC == x:
        output = ("{0} is the most used browser.".format(browser2))

    elif countIE == x:
        output = ("{0} is the most used browser.".format(browser3))

    elif countS == x:
        output = ("{0} is the most used browser.".format(browser4))

    return output

def main(url):
    print(f"Running main with URL = {url}...")
    flist = pullfile(url)
    lavg = searchimg(flist)
    favbr = searchbr(flist)
    print(lavg)
    print(favbr)



if __name__ == "__main__":

    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
