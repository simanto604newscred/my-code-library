from aiohttp import ClientSession
import logging
import asyncio
logger = logging.getLogger(__name__)
from typing import List, Dict
import time

async def fetch_decryption_keys_batch_async(all_brand_ids, brand_keys):
    new_brand_count = 0
    async with ClientSession() as ks:
        for brand_id in all_brand_ids:
            # check if brand_id already acquired
            if brand_id not in brand_keys:
                try:
                    keys_obj = await ks.get("http://httpbin.org/delay/"+str(brand_id))
                    brand_keys[brand_id] = keys_obj.status
                    new_brand_count += 1
                except Exception as e:
                    logger.exception(e)
                    brand_keys[brand_id] = None
                    logging.debug(f"No key for brand '{brand_id}'")
    logger.info(f"Collected {new_brand_count} keysets for {len(all_brand_ids)} brands")
    return brand_keys




def fetch_decryption_keys_batch(
    brand_ids: List[str], brand_keys: Dict[str, dict] = {}
) -> Dict[str, dict]:
    """
    Driver function for fetching decryption keys async
    """
    st = time.time()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    event_loop = asyncio.get_event_loop()
    keys = event_loop.run_until_complete(
        fetch_decryption_keys_batch_async(brand_ids, brand_keys)

    )
    loop.close()
    logger.info(f"Took {time.time() - st:.2f}s to collect the decryption keys")
    print(f"Took {time.time() - st:.2f}s to collect the decryption keys")



keys = fetch_decryption_keys_batch([1,2,3,4], {})
print(keys)

