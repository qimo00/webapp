import orm, asyncio, sys
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='woshidahao1.', db='awesome')
    u = User(name='Test', email='tes@example.com', passwd='1234567890', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(loop)]))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
