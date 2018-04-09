# Entrypoint: com.google.android.apps.books.app.BooksActivity.onCreate(Landroid/os/Bundle;)V
# Target: PC@124

IAAv5 = Real('IAAv5')    # <Input1>
IAAv4 = Int('IAAv4')    # Pointer<356907009>
IAAv3 = Int('IAAv3')    # Pointer<-746481421>
IAAv1 = Real('IAAv1')    # <ChainedInput1>.findAccount(Pointer<1999623615>)
IAAv2 = Int('IAAv2')    # Pointer<-695848582>.isInProgress()
IAAv0 = Int('IAAv0')    # Pointer<1999623615>
IAAv6 = Real('IAAv6')    # <Input1>.getParcelable()

s.add(And(And(And(And((IAAv0 != 0), (IAAv1 == 0)), And(Or(And((IAAv2 == 0), (IAAv3 == 0)), And((IAAv2 == 0), (IAAv3 != 0))), (IAAv4 == 0))), (IAAv5 != 0)), (IAAv0 == IAAv6)))

