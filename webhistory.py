import browserhistory as bh
dict_obj = bh.get_browserhistory()
dict_obj.keys()
dict_keys(["safari", "firefox", "chrome"])
dict_obj['safari'][0]


bh.write_browserhistory_csv()