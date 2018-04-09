# Entrypoint: com.android.mail.ui.cr.onLoadFinished(Landroid/content/Loader;Ljava/lang/Object;)V
# Target: invokevirtual < Application, Lcom/android/mail/ui/cr, startActivityForResult(Landroid/content/Intent;I)V >@55

IAAv0 = Real('IAAv0')    # <ChainedInput2>
IAAv1 = Int('IAAv1')    # <ChainedInput2>.moveToFirst()
IAAv5 = Int('IAAv5')    # <ChainedInput2>.getCount()
IAAv4 = Int('IAAv4')    # Pointer<-1262134233>
IAAv2 = Int('IAAv2')    # <ChainedInput2>.moveToNext()
IAAv3 = Int('IAAv3')    # Pointer<972162467>

s.add(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv2 == 0)), Or(And(Or((IAAv3 != 0), And((IAAv3 == 0), (IAAv4 != 0))), (IAAv0 == 0)), And(And(Or((IAAv3 != 0), And((IAAv3 == 0), (IAAv4 != 0))), (IAAv0 != 0)), (IAAv5 == 0)))))

