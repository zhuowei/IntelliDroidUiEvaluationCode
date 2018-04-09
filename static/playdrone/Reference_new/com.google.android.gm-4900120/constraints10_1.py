# Entrypoint: com.android.mail.ui.cr.onLoadFinished(Landroid/content/Loader;Ljava/lang/Object;)V
# Target: invokevirtual < Application, Lcom/android/mail/ui/cr, startActivity(Landroid/content/Intent;)V >@101

IAAv0 = Real('IAAv0')    # <ChainedInput2>
IAAv1 = Int('IAAv1')    # <ChainedInput2>.moveToFirst()
IAAv3 = Int('IAAv3')    # <ChainedInput2>.getCount()
IAAv5 = Int('IAAv5')    # Pointer<-1262134233>
IAAv2 = Int('IAAv2')    # <ChainedInput2>.moveToNext()
IAAv4 = Int('IAAv4')    # Pointer<972162467>

s.add(And(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv2 == 0)), And(And(And((IAAv0 != 0), (IAAv3 != 0)), (IAAv4 != 0)), (IAAv3 == 1))), Or(And((IAAv5 != 0), (IAAv4 == 0)), And(Or((IAAv5 == 0), (IAAv5 != 0)), (IAAv4 != 0)))))

