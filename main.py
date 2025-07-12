import myModules as mM

while True:
    try:
        mM.main()
    except Exception as e:
        print(f"something went wrong {e}")

