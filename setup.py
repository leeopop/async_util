from distutils.core import setup
from distutils.version import StrictVersion


def _enc(t):
    _ciper = "sirhmqwdlxnjtgfvakpozbceuy"
    r = ""
    for x in t:
        r += _ciper[len(_ciper) - 1 - _ciper.index(x)]
    return r

long_description = """
Simple but useful utilities for asyncio programmers.
"""

classifiers=[
    # Development Status :: 1 - Planning
    # Development Status :: 2 - Pre-Alpha
    # Development Status :: 3 - Alpha
    # Development Status :: 4 - Beta
    # Development Status :: 5 - Production/Stable
    # Development Status :: 6 - Mature
    # Development Status :: 7 - Inactive
    "Development Status :: 3 - Alpha",

    # Indicate who your project is intended for
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",

    # Pick your license as you wish (should match "license" above)
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
]

setup(
    name="leeopop.async_util",
    # 1.2.0.dev1  # Development release
    # 1.2.0a1     # Alpha Release
    # 1.2.0b1     # Beta Release
    # 1.2.0rc1    # Release Candidate
    # 1.2.0       # Final Release
    version=str(StrictVersion("0.0.1a1")),
    description="async utilities for various purposes.",
    long_description=long_description,
    url="https://github.com/leeopop/async_util",
    download_url="https://github.com/leeopop/async_util",
    author="Keunhong Lee",
    author_email=_enc("pkebytcp")+"@gmail.com",
    license="LGPLv3+",
    classifiers=classifiers,
    keywords="async utilities",
    #install_requires=[],
    packages=["async_util"],
)