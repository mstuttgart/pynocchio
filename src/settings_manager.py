# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>..


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
        file_name = str(file_name)

        import ConfigParser

        config = ConfigParser.ConfigParser()
        file_settings = open(file_name, "w")

        for section, keys in content.items():
            config.add_section(str(section))

            for option, value in keys.items():
                config.set(str(section), option, value)

        config.write(file_settings)
        file_settings.close()

