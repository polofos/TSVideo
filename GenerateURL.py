import sys

def generateURLS(URL,TS_max):

    #Working with URLs
    max_digits = len(TS_max)
    termination_start = URL.find('.ts')
    #print(termination_start)
    url_base = URL[:termination_start-max_digits]
    termination = URL[termination_start:]
    #print(url_base,termination)
    #print(str("{:03d}".format(1)))
    
    with open("TS_URLS.txt", "w") as f:
        # First URL
        f.write(URL+'\n')

        #Rest of URLs
        for i in range (1, int(TS_max) + 1):
            new_url = url_base + str("{:03d}".format(i)) + termination
            #print(new_url)
            f.write(new_url+'\n')

if __name__ == '__main__':
    generateURLS(sys.argv[1], sys.argv[2])
