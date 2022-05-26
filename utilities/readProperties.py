import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL(self):
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword(self):
        password = config.get('common info', 'password')
        return password
