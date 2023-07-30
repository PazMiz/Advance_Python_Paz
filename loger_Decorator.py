import random
import logging
import time

# Set up the logger
class CustomFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.logged_messages = set()

    def format(self, record):
        message = record.getMessage()
        if message not in self.logged_messages:
            self.logged_messages.add(message)
            return super().format(record)
        else:
            return ''

    def formatTime(self, record, datefmt=None):
        return time.strftime('%Y-%m-%d %H:%M:%S')

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', )
logger = logging.getLogger()
handler = logging.FileHandler('app.log')
handler.setFormatter(CustomFormatter())
logger.addHandler(handler)

class MaxAttemptsExceededError(Exception):
    pass

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_warning(message):
    logger.warning(message)

def log_debug(message):
    logger.debug(message)

def log_critical(message):
    logger.critical(message)

def log_function_execution(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        log_info(f"Function '{function_name}' started. Args: {args}, Kwargs: {kwargs}")
        start_time = time.time()

        try:
            # Validate arguments here if needed
            # For example, check if max_attempts and max_wait_time are integers
            for arg in args:
                if not isinstance(arg, int):
                    raise ValueError("Invalid argument type. Expected integer.")

            for value in kwargs.values():
                if not isinstance(value, int):
                    raise ValueError("Invalid argument type. Expected integer.")

            expected_result = "Operation successful!"
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time

            if result == expected_result:
                log_info(f"Function '{function_name}' completed successfully. Execution time: {execution_time:.2f} seconds. Expected: {expected_result}, Got: {result}")
            else:
                log_warning(f"Function '{function_name}' returned an unexpected result. Execution time: {execution_time:.2f} seconds. Expected: {expected_result}, Got: {result}")

            return result
        except (ValueError, TypeError) as e:
            log_critical(f"Invalid argument(s) passed to function '{function_name}': {e}")
            raise
        except Exception as e:
            log_critical(f"Function '{function_name}' failed with error: {e}")
            raise

    return wrapper

@log_function_execution   
# Decorator
def do_something_unstable(max_attempts=3, max_wait_time=3):
    for attempt in range(1, max_attempts + 1):
        try:
            if random.random() < 0.5:
                raise ValueError("Something went wrong!")
            return "Operation successful!"
        except ValueError as e:
            log_error(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                wait_time = random.randint(1, max_wait_time)
                log_warning(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                log_error("Max attempts reached. Operation failed.")
                raise MaxAttemptsExceededError("Max attempts reached.")
    return None

if __name__ == "__main__":
    try:
        result = do_something_unstable(max_attempts=3, max_wait_time=3)
        log_info(result)
    except MaxAttemptsExceededError:
        log_critical("Max attempts exceeded. Exiting...")
    except Exception as e:
        log_critical(f"Unexpected error: {e}")
        raise
    finally:
        logging.shutdown()
