from logging.config import dictConfig

def setup_logger():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': 'app.log',
                'encoding': 'utf8'
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            },
            'app_logger': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': False
            },
        }
    }
    dictConfig(logging_config)