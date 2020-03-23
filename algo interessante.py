#
# music searcher
#
import webbrowser

WEB = "https://www.youtube.com/results?search_query="
query = input("what music are you looking for?\n >>> ")
webbrowser.open_new_tab(WEB + query)
