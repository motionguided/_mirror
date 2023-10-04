from anvil import *
import anvil.server
import tables
from tables import app_tables


class SearchHintsDemo(SearchHintsDemoTemplate):
  """Shows how to use the SearchHints component in an app."""
  
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # The SearchHints instance has an event called x-get-search-keys that gets called to retrieve the search keys.
    self.search_hints_1.set_event_handler('x-get-search-keys', self.get_search_keys)

    # The SearchHints instance has an event called x-search-hints-result that gets called
    # when the result has been selected.
    self.search_hints_1.set_event_handler('x-search-hints-result', self.update_result_label)

  def update_result_label(self, result, **event_args):
    """Set the result label on this Form to the selected search result."""
    self.label_result.text = result

  def get_search_keys(self, **event_args):
    """Get the search keys from the Data Table."""
    return anvil.server.call('get_search_keys')
    