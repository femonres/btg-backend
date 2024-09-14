import logging

def setup_logging():
    # Configura el logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Puedes ajustar el nivel de log

    # Crea un manejador para stdout
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Define el formato de los logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Añade el manejador al logger
    logger.addHandler(handler)

    return logger
