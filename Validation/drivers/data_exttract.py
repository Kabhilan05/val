from Validation.drivers.data_loader import TestDataLoader

loader = TestDataLoader()

# test_case_key = "SSVAL-T1"
# specific_tets_case = loader.get_test_cases_by_key(test_case_key)
# print(f"Test Case '{test_case_key}': {specific_tets_case}")

# all_test_cases =loader.get_all_test_cases()
# print(all_test_cases)

# folder_name = 'CPU'
# specific_folder = loader.get_test_cases_by_folder(folder_name)
# print(specific_folder)

# priority = 'Normal'
# specific_priority = loader.get_test_cases_by_priority(priority)
# print(specific_priority)

label = 'CPU'
specific_label = loader.get_test_cases_by_labels(label)
print(specific_label)

# from utils.yaml_load import load_config
# data = load_config('config.yaml')
# print(data['json']['folder'])
