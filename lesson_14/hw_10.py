import asyncio
import logging

import aiohttp

logging.basicConfig(level=logging.INFO)

urls_to_scrape = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]


async def scrape_and_save(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_text = await response.text()
                with open(
                    f'{url.replace("https://", "").replace("/", "_")}' ".html",
                    "w",
                ) as f:
                    f.write(response_text)
                logging.info(f"Successfully scraped and saved {url}")
    except Exception as e:
        logging.error(f"Error while scraping {url}: {e}")


async def worker(queue):
    while True:
        url = await queue.get()
        if url is None:
            break
        await scrape_and_save(url)
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker(queue)) for _ in range(len(urls_to_scrape))
    ]

    for url in urls_to_scrape:
        await queue.put(url)

    await queue.join()

    for _ in range(len(urls_to_scrape)):
        await queue.put(None)

    await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())
