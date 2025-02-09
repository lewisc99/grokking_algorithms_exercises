cache = {}
def get_page(url):
  if url in cache:
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data
    return data
