import time


current_time = time.time()
print(f"seconds since January 1, 1970: {current_time:,.4f} {current_time:.2e} in scientific notation  {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(f"{time.strftime('%B %d %Y', time.localtime(current_time))}")
