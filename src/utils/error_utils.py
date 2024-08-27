import logging
import traceback

def log_error(e: Exception) -> None:
    logger = logging.getLogger(__name__)
    logger.error(f"An error occurred: {str(e)}")

def log_warning(message: str) -> None:
    logger = logging.getLogger('app_logger')
    logger.warning(message)

def log_info(message: str) -> None:
    logger = logging.getLogger('app_logger')
    logger.info(message)

def log_debug(message: str) -> None:
    logger = logging.getLogger('app_logger')
    logger.debug(message)

def handle_exception(e: Exception) -> None:
    log_error(e)

def format_exception(e: Exception) -> str:
    return f"{str(e)}\n{traceback.format_exc()}"