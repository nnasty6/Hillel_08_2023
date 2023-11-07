import asyncio

import aiohttp
import aiosqlite
from bs4 import BeautifulSoup


async def scrape_urls(semaphore, queue, name_db):
    """scrape_urls function retrives urls and
    their titles for database
    """
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            while not queue.empty():
                url = await queue.get()
                title = await get_title_from_url(session, url)

                await save_to_db(name_db, url, title)
                print(f"📥 Url {url} is scraped, title - {title}")

                queue.task_done()


async def scrape_url(session, url):
    """scrape_url function processes a single url
    with a time limit (timeout) and prevent an
    HTML page in a text format
    """
    async with session.get(url, timeout=2) as scrape:
        print(f"ℹ️  Status of URL {url} is {scrape.status}")
        # if scrape.status == 200:
        return await scrape.text()

        # else:
        #     return (
        #         f"Probably URL {url} incorrect. "
        #         f"Status code: {scrape.status}"
        #     )


async def get_title_from_url(session, url):
    """get_title_from_url function processes url information
    and extract a title of the current page
    """
    task = asyncio.create_task(scrape_url(session, url))
    page_html = await task
    soup = BeautifulSoup(page_html, "lxml")
    title_tag = soup.find("head").find("title")

    title = title_tag.text
    return title


async def save_to_db(name_db, url, title):
    """save_to_db function creates a new database or adds
    an information to database if it already exists
    """
    connection = await aiosqlite.connect(name_db)
    cursor = await connection.cursor()
    await cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS scrapped_urls (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL,
            title TEXT NOT NULL
        )
    """
    )

    await cursor.execute(
        "INSERT INTO scrapped_urls (url, title) VALUES (?,  ?)",
        (url, title),
    )
    await connection.commit()
    await connection.close()


async def main():
    URLS = [
        "http://loveread.ec/read_book.php?id=36105&p=1",
        "http://loveread.ec/read_book.php?id=36105&p=2",
        "http://loveread.ec/read_book.php?id=36105&p=3",
        "http://loveread.ec/read_book.php?id=2392&p=1",
        "http://loveread.ec/read_book.php?id=2392&p=2",
        "http://loveread.ec/read_book.php?id=2392&p=3",
        "http://loveread.ec/read_book.php?id=2392&p=4",
    ]

    name_db = "scrapped_urls.db"
    queue = asyncio.Queue(10)
    max_requests = 5
    semaphore = asyncio.Semaphore(max_requests)
    try:
        for url in URLS:
            await queue.put(url)

        tasks = [
            scrape_urls(semaphore, queue, name_db) for _ in range(max_requests)
        ]
        await asyncio.gather(*tasks)
    except aiohttp.ClientConnectorError as e:
        print(
            "❗️❗️❗️ Oops! Something went wrong with request! "
            f"ERROR is - {e}"
        )
    except asyncio.TimeoutError:
        print("🛑 Waiting is too long, task was canceled")
    await queue.join()
    print(f"📰 {len(URLS)} urls are scraped")


if __name__ == "__main__":
    asyncio.run(main())
    print("🎉 all data is successfully saved to db")
