"""This pattern allow us to create a placeholder object that can be used to represent
 the functionality of another object. The proxy object acts as an intermediary between
  the client and the real object, which can be located remotely, behind a firewall,
  or in a different address space."""


from abc import ABC, abstractmethod


class FileDownloader(ABC):
    @abstractmethod
    def download(self, url: str) -> bytes:
        pass


class RemoteFileDownloader(FileDownloader):
    def download(self, url: str) -> bytes:
        # Code to download file from remote server
        pass


class MEGAUPLOAD(FileDownloader):  # THIS IS THE FILE DOWNLOADER PROXY
    def __init__(self, file_downloader: FileDownloader):
        self.file_downloader = file_downloader

    def download(self, url: str) -> bytes:
        # Code to authenticate user
        # ...

        # Call the real downloader to download the file
        return self.file_downloader.download(url)


if __name__ == '__main__':
    real_downloader = RemoteFileDownloader()
    downloader_proxy = MEGAUPLOAD(real_downloader)

    file_url = 'https://wikileaks/who_killed_kennedy.zip'
    downloaded_file = downloader_proxy.download(file_url)
