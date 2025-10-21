import MetaTrader5 as mt5

# --- FUNCTION: INITIALIZE ---
def initialize(login, server, password, path):
    if not mt5.initialize(path):
        print("initialize() failed, error code {}", mt5.last_error())
        quit()
    #else:
    #    if not mt5.login(login,password,server):
    #        print("login failed, error code: {}".format(mt5.last_error()))
