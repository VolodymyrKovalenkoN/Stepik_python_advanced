password = input()
is_strong = lambda passwa: "YES" if any(ch.isdigit() for ch in passwa) and \
                           any(ch.isupper() for ch in passwa) and \
                           any(ch.islower() for ch in passwa) and \
                           len(password) >= 7 else "NO"
print(is_strong(password))
