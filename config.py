import yaml


def read_config():
    with open('config.yml', 'r', encoding='utf-8')  as file:
        return yaml.safe_load(file)
class Config():
    ...

if __name__ == '__main__':
    config = read_config()

    print(config)