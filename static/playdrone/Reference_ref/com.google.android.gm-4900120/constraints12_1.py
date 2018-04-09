# Entrypoint: com.android.mail.ui.u.onLoadFinished(Landroid/content/Loader;Ljava/lang/Object;)V
# Target: invokevirtual < Application, Lcom/android/mail/ui/co, startActivityForResult(Landroid/content/Intent;I)V >@189

IAAv1 = Real('IAAv1')    # <ChainedInput2>
IAAv2 = BitVec('IAAv2',32)    # <ChainedInput2>.getCount()
IAAv4 = Real('IAAv4')    # Pointer<313732425>.mContext.q()
IAAv0 = Int('IAAv0')    # <ChainedInput1>.getId()
IAAv3 = Int('IAAv3')    # <ChainedInput2>.getExtras().getInt()

s.add(And(Or(And(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 == 0)), (IAAv3 == 0)), And(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 == 0)), (IAAv3 != 0))), (IAAv4 != 0)))

