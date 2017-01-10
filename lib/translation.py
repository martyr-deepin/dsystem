import os
import configparser

class CharTranslation:

    def getCharTrans(self, char):
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/lib/translate.ini')
        if os.getenv('LANG') == 'zh_CN.UTF-8':
            return config['zh_CN'][char]
        else:
            return config['en_US'][char]

charTrans = CharTranslation()
