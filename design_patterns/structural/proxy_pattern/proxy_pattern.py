"""This pattern allow us to create a placeholder object that can be used to represent
 the functionality of another object. The proxy object acts as an intermediary between
  the client and the real object, which can be located remotely, behind a firewall,
  or in a different address space."""


from abc import ABC, abstractmethod


class FileDownloader(ABC):
    """Interface shared by the real downloader and its proxy."""
    @abstractmethod
    def download(self, url: str) -> bytes:
        """Download the file at url and return its bytes."""


class RemoteFileDownloader(FileDownloader):
    """Real subject: the object that actually downloads the file."""
    def download(self, url: str) -> bytes:
        print(f"  [remote] downloading {url} ...")
        # simulated download
        return b"file content of " + url.encode()


class MEGAUPLOAD(FileDownloader):  # THIS IS THE FILE DOWNLOADER PROXY
    """Proxy: checks access and caches results before reaching the real downloader."""
    def __init__(self, file_downloader: FileDownloader, allowed: bool = True):
        self.file_downloader = file_downloader
        self.allowed = allowed
        self._cache: dict[str, bytes] = {}

    def download(self, url: str) -> bytes:
        if not self.allowed:
            raise PermissionError("user is not allowed to download files")

        # return the cached copy if we already downloaded this url
        if url in self._cache:
            print(f"  [proxy] cache hit for {url}")
            return self._cache[url]

        # Call the real downloader to download the file
        content = self.file_downloader.download(url)
        self._cache[url] = content
        return content


if __name__ == '__main__':
    real_downloader = RemoteFileDownloader()
    downloader_proxy = MEGAUPLOAD(real_downloader)

    downloaded_file = downloader_proxy.download('https://example.com/file.zip')
    print(downloaded_file)

    # second call is served from the proxy cache
    downloaded_file = downloader_proxy.download('https://example.com/file.zip')
    print(downloaded_file)

    blocked_proxy = MEGAUPLOAD(real_downloader, allowed=False)
    try:
        blocked_proxy.download('https://example.com/file.zip')
    except PermissionError as error:
        print(error)
