import pycurl 
import certifi 
from io import BytesIO 


res_buffer = BytesIO()
res_head_buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://mdxunlimited.com/wp-json/wc/v3/products')
c.setopt(c.USERPWD, 'ck:cs')
c.setopt(c.WRITEDATA, res_buffer)
c.setopt(c.HEADERFUNCTION, res_head_buffer.write)
c.perform()

status = c.getinfo(pycurl.RESPONSE_CODE)
c.close()

print(f"HTTP {status}")
print(res_head_buffer.getvalue().decode())
print(res_buffer.getvalue().decode())
