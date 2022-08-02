import datetime as dt
import logging
import sys


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    formatter.converter = lambda x: dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).timetuple()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    msg = 'something message'
    logger.debug('message: %s', msg)

    sys.exit()


if __name__ == "__main__":
    main()
