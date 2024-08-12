import logging
import logging.config
import random
import string
import time
from datetime import datetime

from fastapi import Request

logger = logging.getLogger(__name__)


def setup_logging(config_dir: str, config_file: str, log_dir: str):
    """Load logging configuration"""
    config_path = "/".join([config_dir, config_file])
    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{log_dir}/{timestamp}.log"},
    )
    logging.getLogger("pymongo").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)


async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"rid={idem} completed_in={process_time}ms status_code={response.status_code}"
    )
    return response
