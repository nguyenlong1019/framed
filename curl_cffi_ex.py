from curl_cffi import requests

# r = requests.get(
#     'https://mdxunlimited.com/wp-json/wc/v3/products',
#     auth=('ck', 'cs'),
# )
#
# print(r.status_code)
# print(r.text)

r = requests.get(
    'https://soufeel.com',
    impersonate='chrome131'
)
print(r.status_code)
print(r.text)