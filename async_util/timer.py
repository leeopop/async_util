import asyncio


class Timer:
    def __init__(self, loop):
        self._loop = loop

    def trigger(self, func, delta, canceled=lambda: None):
        async def _trigger():
            try:
                await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                func()
            except asyncio.CancelledError:
                canceled()

        return asyncio.ensure_future(_trigger(), loop=self._loop)

    def async_trigger(self, coro_func, delta, canceled=lambda: None):
        async def _trigger():
            try:
                await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                await coro_func()
            except asyncio.CancelledError:
                canceled()

        return asyncio.ensure_future(_trigger(), loop=self._loop)

    def period(self, func, delta, repeat=None, canceled=lambda: None):
        if repeat is None:
            async def _period():
                try:
                    while True:
                        func()
                        await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                except asyncio.CancelledError:
                    canceled()

            return asyncio.ensure_future(_period(), loop=self._loop)
        else:
            async def _period():
                try:
                    counter = 0
                    while counter < repeat:
                        func()
                        await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                        counter += 1
                except asyncio.CancelledError:
                    canceled()

            return asyncio.ensure_future(_period(), loop=self._loop)

    def async_period(self, coro_func, delta, repeat=None, canceled=lambda: None):
        if repeat is None:
            async def _period():
                try:
                    while True:
                        await coro_func()
                        await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                except asyncio.CancelledError:
                    canceled()

            return asyncio.ensure_future(_period(), loop=self._loop)
        else:
            async def _period():
                try:
                    counter = 0
                    while counter < repeat:
                        await coro_func()
                        await asyncio.sleep(delta.total_seconds(), loop=self._loop)
                        counter += 1
                except asyncio.CancelledError:
                    canceled()

            return asyncio.ensure_future(_period(), loop=self._loop)