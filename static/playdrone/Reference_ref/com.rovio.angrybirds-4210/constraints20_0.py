# Entrypoint: com.mopub.mobileads.cg.onTouch(Landroid/view/View;Landroid/view/MotionEvent;)Z
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@51

IAAv3 = Real('IAAv3')    # Pointer<-429976308>.a().c.onUserClick().d
IAAv0 = Int('IAAv0')    # <ChainedInput2>.getAction()
IAAv1 = Real('IAAv1')    # Pointer<-429976308>.a().c
IAAv2 = Real('IAAv2')    # Pointer<-429976308>.a().b.h

s.add(And(Or(And((IAAv0 == 1), (IAAv1 == 0)), And((IAAv0 == 1), (IAAv1 != 0))), (IAAv2 == IAAv3)))

