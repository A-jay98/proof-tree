class Settings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.settings = {}

    def __getattr__(self, name):
        if name == 'settings':
            return object.__getattribute__(self, name)
        return object.__getattribute__(self, 'settings').get(name, None)

    def __setattr__(self, name, value):
        if name == 'settings':
            super(Settings, self).__setattr__(name, value)
        else:
            self.settings[name] = value

    def __str__(self):
        return str(self.settings)

    def load_settings(self, **kwargs):
        if self.settings:
            raise Exception("Settings have already been loaded, complete overrides are not acceptable.")
        self.settings.update(kwargs)


settings = Settings()
