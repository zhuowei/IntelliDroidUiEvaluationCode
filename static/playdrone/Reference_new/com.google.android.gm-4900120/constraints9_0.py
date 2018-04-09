# Entrypoint: com.android.mail.ui.cr.<init>()V
# Target: PC@33

IAAv0 = Real('IAAv0')    # <ChainedInput2>
IAAv1 = Int('IAAv1')    # <ChainedInput2>.moveToFirst()
IAAv4 = Int('IAAv4')    # <ChainedInput2>.getCount()
IAAv3 = Int('IAAv3')    # Pointer<-1262134233>
IAAv2 = Int('IAAv2')    # <ChainedInput2>.moveToNext()
IAAv5 = Int('IAAv5')    # Pointer<972162467>

s.add(And(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv2 == 0)), Or(And((IAAv3 != 0), (IAAv0 == 0)), And(And((IAAv3 != 0), (IAAv0 != 0)), (IAAv4 == 0)))), (IAAv5 == 0)))

