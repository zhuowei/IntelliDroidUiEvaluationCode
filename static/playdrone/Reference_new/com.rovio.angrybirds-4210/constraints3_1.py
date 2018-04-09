# Entrypoint: com.rovio.skynest.socialnetwork.SocialSharingViewWrapper.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@9

IAAv3 = Real('IAAv3')    # Pointer<-1067817496>.setLogLevel().a
IAAv4 = Int('IAAv4')    # Pointer<-778432234>
IAAv0 = Real('IAAv0')    # Pointer<-1848624051>.get()
IAAv1 = Int('IAAv1')    # Pointer<1994903687>
IAAv2 = Real('IAAv2')    # Pointer<935185220>.get()

s.add(And(Or((IAAv0 == IAAv1), And((IAAv0 != IAAv1), (IAAv2 == 0))), Or(Or(And((IAAv3 == 3), (IAAv4 == 0)), And((IAAv3 == 3), (IAAv4 != 0))), (IAAv3 == 1))))

