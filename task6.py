def closure_outer(name):

    def closure_inner():
        return f"Hello, {name}!"
    return closure_inner

clousure = closure_outer("Hassan")
print(clousure())