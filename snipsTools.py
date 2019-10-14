import io
import configparser 

CONFIGURATION_ENCODING_FORMAT = "utf-8"


class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {
            section: {
                optname: option for optname, option in self.items(section)
            } for section in self.sections()
        }

    def optionxform(self, option):
        """
        This method is overriden to make config keys and values case-sensitive
        """
        return option

    @staticmethod
    def read_configuration_file(configuration_file):
        try:
            with io.open(
                    configuration_file,
                    encoding=CONFIGURATION_ENCODING_FORMAT) as f:
                # intents can contain ":", so restrict delimiters here
                conf_parser = SnipsConfigParser(delimiters=("=",))
                conf_parser.readfp(f)
                return conf_parser.to_dict()

        except (IOError, configparser.Error) as e:
            print(e)
            return dict()

    @staticmethod
    def write_configuration_file(configuration_file, data):
        conf_parser = SnipsConfigParser()
        for key in data.keys():
            conf_parser.add_section(key)
            for inner_key in data[key].keys():
                conf_parser.set(key, inner_key, data[key][inner_key])

        try:
            with open(configuration_file, 'w') as f:
                conf_parser.write(f)
                return True

        except (IOError, configparser.Error) as e:
            print(e)
            return False
