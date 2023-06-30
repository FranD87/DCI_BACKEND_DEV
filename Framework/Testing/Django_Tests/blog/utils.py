import logging

logger = logging.getLogger()

def add_items(item_1, item_2):
    result = None
    logger.debug(f"Items {item_1}, {item_2}")
    try:
        logger.info(f"About Adding item {item_1} and {item_2}")
        result = item_1 + item_2
        logger.warning("Check the types of items")
    except Exception as error:
        logger.error(f"An error occurred {error}")
        logger.critical("This error would have stopped me")
    logger.info(f"My result is {result}")
    return result