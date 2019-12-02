import importlib, importlib.util

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# need to give name & file path
locator = module_from_file("locator","./locators/quote_locators.py")

# 
print(locator.QuoteLocators.AUTHOR)
