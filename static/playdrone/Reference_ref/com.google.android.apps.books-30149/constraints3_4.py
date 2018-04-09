# Entrypoint: com.google.android.apps.books.app.BaseBooksActivity.onAccountsUpdated([Landroid/accounts/Account;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivity(Landroid/content/Intent;)V >@38

IAAv6 = Int('IAAv6')    # Pointer<-2067429428>
IAAv5 = Int('IAAv5')    # Pointer<-2061306034>
IAAv4 = Int('IAAv4')    # Pointer<356907009>
IAAv3 = Int('IAAv3')    # Pointer<-746481421>
IAAv1 = Real('IAAv1')    # <ChainedInput1>.findAccount(Pointer<1999623615>)
IAAv2 = Int('IAAv2')    # Pointer<-695848582>.isInProgress()
IAAv0 = Int('IAAv0')    # Pointer<1999623615>
IAAv7 = Int('IAAv7')    # Pointer<356907009>.equal(Pointer<1999623615> | null)

s.add(And(And(And((IAAv0 != 0), (IAAv1 == 0)), Or(And(And(And(Or(And((IAAv2 == 0), (IAAv3 == 0)), And((IAAv2 == 0), (IAAv3 != 0))), (IAAv4 != 0)), (IAAv5 == 0)), (IAAv6 != 0)), And(And(And(Or(And((IAAv2 == 0), (IAAv3 == 0)), And((IAAv2 == 0), (IAAv3 != 0))), (IAAv4 != 0)), (IAAv5 == 0)), (IAAv6 == 0)))), And((IAAv7 == 0), (IAAv0 != 0))))

