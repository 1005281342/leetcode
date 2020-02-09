def q():s='def q():s=%s;return s%%repr(s)';return s%repr(s)


ans = q()
print(ans)