# Entrypoint: com.google.android.apps.books.app.BaseBooksActivity.onAccountsUpdated([Landroid/accounts/Account;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@75

IAAv4 = Int('IAAv4')    # Pointer<356907009>
IAAv3 = Int('IAAv3')    # Pointer<-746481421>
IAAv1 = Real('IAAv1')    # <ChainedInput1>.findAccount(Pointer<1999623615>)
IAAv2 = Int('IAAv2')    # Pointer<-695848582>.isInProgress()
IAAv0 = Int('IAAv0')    # Pointer<1999623615>

s.add(And(And((IAAv0 != 0), (IAAv1 == 0)), And(Or(And((IAAv2 == 0), (IAAv3 == 0)), And((IAAv2 == 0), (IAAv3 != 0))), (IAAv4 == 0))))

