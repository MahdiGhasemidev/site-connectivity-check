import requests
from concurrent.futures import ThreadPoolExecutor

import streamlit as st 

# Format the entered URL by stripping http(s) and www, then prepending a consistent prefix
def format_url(url: str) -> str:
    """format input url to correct format

    :param url: input url
    :type url: str
    :return: formatted url
    :rtype: str
    """
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
    
    if url.startswith('www.'):
        url = url[len('www.'):]
        
    formatted_url = 'https://www.' + url
    return formatted_url

# Check whether a given URL is reachable (returns HTTP 200)
def check_connecticity(url: str) -> bool:
    """check connecivity of url

    :param url: url
    :type url: str
    :return: True or False
    :rtype: bool
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Main Streamlit app
def main():
    st.title(":signal_strength: WebSite Availability Checker")

    # Initialize session state for URLs if it doesn't exist
    if 'urls' not in st.session_state:
        st.session_state.urls = []

    # Text input for entering a new URL
    new_url = st.text_input('Enter a URL to add to the list: ', "")

    col1, col2 = st.columns([1, 1])
    
    # Button to add a new URL to the list
    with col1:
        if st.button('Add URL'):
            formatted_url = format_url(new_url)
            if formatted_url not in st.session_state.urls and new_url != "":
                st.session_state.urls.append(formatted_url)
                st.success(f'Added {formatted_url} to the list')
            else:
                st.warning('URL Already exists or is invalid')

    # Buttons for clearing list and checking all URLs
    with col2:
        if st.button('Clear List'):
            st.session_state.urls.clear()

        # Check all URLs concurrently using ThreadPoolExecutor
        if st.button('Check All'):
            with ThreadPoolExecutor(max_workers=10) as executor:
                results = list(executor.map(check_connecticity, st.session_state.urls))
            for indx, result in enumerate(results):
                st.session_state[f'status_{indx}'] = result

    # Display each URL and its status (✅ / ❌)
    for indx, url in enumerate(st.session_state.urls):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.write(url)
        with col2:
            if f'status_{indx}' in st.session_state:
                st.write("✅" if st.session_state[f'status_{indx}'] else "❌")
            else:
                st.write("")  # Empty if not checked yet


if __name__ == '__main__':
    main()
