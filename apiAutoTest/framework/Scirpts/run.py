import sys

envPath = '..\Env.txt'
stageUrl = 'http://stageapi.vipabc.com'
productUrl = 'http://api.vipabc.com'

def decideEnv(inputText):
    print inputText
    output = open(envPath, 'w')
    if inputText.lower() == 'stage':
        output.write(stageUrl)
        print 'Server Url: '+stageUrl
    elif inputText.lower() == 'product':
        output.write(productUrl)
        print 'Server Url: '+productUrl
    else:
        print  'ERROR : ' + inputText + ' is not corrent value, it should be "stage" or "product"'
        output.close()

if __name__ == "__main__":
    text = sys.argv[1]
    decideEnv(text)
