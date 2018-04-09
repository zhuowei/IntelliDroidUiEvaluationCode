# Entrypoint: com.facebook.widget.ag.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@9

IAAv5 = Real('IAAv5')    # Pointer<-1892226031>.a().setSession().PUBLISH
IAAv1 = Real('IAAv1')    # Pointer<-1892226031>.a().getSession()
IAAv0 = Real('IAAv0')    # Pointer<-1892226031>.a().getOpenSession()
IAAv12 = Real('IAAv12')    # Pointer<-1892226031>.a().getSession().b().OPENING
IAAv9 = Real('IAAv9')    # Pointer<-1892226031>.a().getSession().i
IAAv11 = Real('IAAv11')    # Pointer<-1892226031>.a().getSession().addCallback().OPENING
IAAv10 = Real('IAAv10')    # Pointer<-1892226031>.a().getSession().b().OPENED
IAAv7 = Int('IAAv7')    # equals86<return>
IAAv6 = Real('IAAv6')    # Pointer<-1892226031>.g().d()
IAAv2 = Int('IAAv2')    # Pointer<-1892226031>.a().getSession().getState().isClosed()
IAAv8 = Real('IAAv8')    # Pointer<-1892226031>.a().getSession().b().a
IAAv3 = Int('IAAv3')    # Pointer<-1892226031>.a().getSession().isOpened()
IAAv13 = Int('IAAv13')    # Pointer<-1892226031>.a().getSession().a(Pointer<-1892226031>.a().getSession().d())
IAAv4 = Real('IAAv4')    # Pointer<-1892226031>.f()

s.add(And(And(And(And(Or(And(And(Or(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 == 0)), Or(And((IAAv0 == 0), (IAAv1 == 0)), And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 != 0)))), (IAAv3 == 0)), (IAAv4 == 0)), And(And(Or(And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 == 0)), Or(And((IAAv0 == 0), (IAAv1 == 0)), And(And((IAAv0 == 0), (IAAv1 != 0)), (IAAv2 != 0)))), (IAAv3 == 0)), (IAAv4 != 0))), (IAAv5 != IAAv6)), (IAAv7 == 0)), And(Or(Or(And((IAAv8 == 3), (IAAv9 == 0)), And((IAAv8 == 3), (IAAv9 != 0))), (IAAv8 == 1)), Or(Or((IAAv10 == IAAv11), (IAAv12 == IAAv11)), (IAAv12 == IAAv11)))), (IAAv13 != 0)))

