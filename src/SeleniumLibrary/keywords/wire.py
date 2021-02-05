from selenium.common.exceptions import NoSuchWindowException

from SeleniumLibrary.base import keyword, LibraryComponent


class WireKeywords(LibraryComponent):
  @keyword
  def assert_request(self, pattern: str) -> str:
    """Verifies that a request was made with a URL matching ``pattern``.

    """
    for request in self.driver.requests:
      if pattern in request.url:
        self.info(f"Found request matching '{pattern}'")
        return request.url

    raise AssertionError(f"Didn't find any request matching '{pattern}'")
