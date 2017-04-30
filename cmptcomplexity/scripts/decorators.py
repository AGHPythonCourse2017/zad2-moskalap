from functools import wraps
import signal
import cmptcomplexity.scripts.exceptions as exceptions
import logging

def log_it(func):
    def wrap(*args, **kwargs):
        logging.info('started function %s', func.__name__)
        result = func(*args, **kwargs)
        logging.info('function %s returned %s', func.__name__, str(result))
        return result

    return wrap

def timeout():
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise exceptions.TimeoutCCExcetion('ops')

        def wrapper(*args, **kwargs):
            ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)
            signal.setitimer(signal.ITIMER_REAL, ltou)
            signal.signal(signal.SIGALRM, _handle_timeout)

            try:
                result = func(*args, **kwargs)
            except exceptions.TimeoutCCExcetion:
                return 0, 'except'

            finally:
                ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)
                signal.setitimer(signal.ITIMER_REAL, ltou)

            return result, ltou

        return wraps(func)(wrapper)

    return decorator
