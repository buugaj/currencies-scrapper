from __future__ import absolute_import, unicode_literals
import logging
from celery import task
from currencies.models import ExchangeRate
from currencies.scrapper import scrap_rss_urls, scrap_currency_rss

logger = logging.getLogger("celery")


@task
def scrap_currencies():
    logger.info("-"*25)
    logger.info("Scrapping rss urls")

    try:
        urls = scrap_rss_urls()
    except Exception as e:
        logger.error("Scrapping rss urls failed with error:")
        logger.error(e)
        return

    results = []
    for url in urls:
        logger.info("Scrapping url {}".format(url))
        try:
            results.extend(scrap_currency_rss(url))
        except Exception as e:
            logger.error("Scrapping url {} failed with error:".format(url))
            logger.error(e)
            return
    ExchangeRate.objects.bulk_insert_or_update_insert_new_related(results)
    logger.info("-"*25)
