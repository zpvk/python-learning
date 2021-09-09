def anncounce(f):
    def wapper():
        print("About to run th function")
        f()
        print("Done with the function")
    return wapper

@anncounce
def hello():
    print("Hello world")
    

hello()