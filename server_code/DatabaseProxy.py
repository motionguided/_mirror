import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import tables
from tables import app_tables
import anvil.server

@anvil.server.callable()
def get_search_keys():
  """Get the keys to populate the Search Hints."""
  return app_tables.toolbox.search()
