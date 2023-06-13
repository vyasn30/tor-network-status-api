import stem.descriptor.remote

try:
    for desc in stem.descriptor.remote.get_consensus():
        print(f"found relay {desc.nickname}: {desc.fingerprint}")

except Exception as e:
    print(e)
