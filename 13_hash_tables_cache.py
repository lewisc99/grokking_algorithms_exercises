cache = {}


def get_data_from_server(url):
    # Simulates retrieving data from a server
    print(f"Fetching data from server for: {url}")
    return f"Data from {url}"


def get_page(url):
    if url in cache:
        print(f"Returning cached data for: {url}")
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


# Example usage
print(get_page("https://example.com"))
print(get_page("https://example.com"))  # This should use the cache
print(get_page("https://another.com"))
