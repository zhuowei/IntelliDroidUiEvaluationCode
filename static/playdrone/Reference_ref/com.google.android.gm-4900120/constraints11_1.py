# Entrypoint: com.android.mail.ui.u.onLoadFinished(Landroid/content/Loader;Ljava/lang/Object;)V
# Target: invokevirtual < Application, Lcom/android/mail/ui/co, startActivity(Landroid/content/Intent;)V >@306

IAAv4 = Int('IAAv4')    # Pointer<313732425>.a(<ChainedInput2>)
IAAv1 = Real('IAAv1')    # <ChainedInput2>
IAAv6 = Real('IAAv6')    # Pointer<313732425>.Aa
IAAv7 = Real('IAAv7')    # <ChainedInput2>.b()
IAAv5 = Int('IAAv5')    # <ChainedInput2>.moveToFirst()
IAAv3 = Int('IAAv3')    # Pointer<313732425>.Vq
IAAv9 = Real('IAAv9')    # Pointer<313732425>.Aa.Qw.Uz
IAAv2 = BitVec('IAAv2',32)    # <ChainedInput2>.getCount()
IAAv0 = Int('IAAv0')    # <ChainedInput1>.getId()
IAAv10 = Int('IAAv10')    # equals49<return>
IAAv8 = Real('IAAv8')    # Pointer<313732425>.nn().EMPTY

s.add(And(And(Or(And(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 != 0)), (IAAv3 == 0)), And(And(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 != 0)), (IAAv3 != 0)), (IAAv4 != 0))), Or(Or(Or(And(And((IAAv1 != 0), (IAAv5 != 0)), (IAAv6 == 0)), Or(Or(And(And((IAAv1 != 0), (IAAv5 != 0)), (IAAv6 != 0)), And(And((IAAv1 != 0), (IAAv5 != 0)), (IAAv6 == 0))), And(And((IAAv1 != 0), (IAAv5 != 0)), (IAAv6 == 0)))), And((IAAv1 != 0), (IAAv5 != 0))), And((IAAv1 != 0), (IAAv5 != 0)))), And(And(And((IAAv7 != 0), (IAAv6 != 0)), (IAAv8 != IAAv9)), (IAAv10 == 0))))

