# Entrypoint: com.facebook.LoginActivity.onCreate(Landroid/os/Bundle;)V
# Target: PC@30

IAAv6 = Int('IAAv6')    # Pointer<-1509641091>.d()
IAAv5 = Int('IAAv5')    # Pointer<-1509641091>.b.b()
IAAv7 = Real('IAAv7')    # <Input1>
IAAv4 = Int('IAAv4')    # Pointer<-1509641091>.b.a()
IAAv2 = Real('IAAv2')    # Pointer<-1509641091>.h
IAAv1 = Int('IAAv1')    # Pointer<-1509641091>.b()
IAAv3 = Real('IAAv3')    # Pointer<-1509641091>.b
IAAv0 = Int('IAAv0')    # Pointer<-1509647320>

s.add(And(And(And(And(And((IAAv0 != 0), (IAAv1 != 0)), And(And((IAAv2 != 0), (IAAv3 != 0)), (IAAv4 != 0))), Or((IAAv5 == 0), And((IAAv5 != 0), (IAAv6 != 0)))), (IAAv7 != 0)), (IAAv0 == IAAv7)))

