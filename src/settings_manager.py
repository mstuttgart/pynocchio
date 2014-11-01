# -*- coding: utf-8 -*-


class SettingsManager(object):

    def __init__(self):
        super(SettingsManager, self).__init__()

    @staticmethod
    def load_settings(file_name):

        import ConfigParser

        config = ConfigParser.ConfigParser()

        try:
            config.read(file_name)
        except IOError, err:
            print err

        content = {}

        for sec in config.sections():
            content[sec] = {}

            for key in config.items(sec):
                option = key[0]
                value = key[1]
                content[sec][option] = value

        return content

    @staticmethod
    def save_settings(content, file_name):

        import ConfigParser

        config = ConfigParser.ConfigParser()
        file_settings = open(file_name, "w")

        for section, keys in content.items():
            config.add_section(section)

            for option, value in keys.items():
                config.set(section, option, value)

        config.write(file_settings)
        file_settings.close()

