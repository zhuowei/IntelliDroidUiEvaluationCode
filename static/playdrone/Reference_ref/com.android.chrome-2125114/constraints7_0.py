# Entrypoint: com.google.android.apps.chrome.firstrun.FirstRunActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivity(Landroid/content/Intent;)V >@110

IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv5 = Int('IAAv5')    # Pointer<805177838>.this$0.access$100()
IAAv8 = Int('IAAv8')    # Pointer<805177838>.this$0.access$400().getFirstRunFlowComplete()
IAAv1 = Int('IAAv1')    # Pointer<582524242>.getBoolean()
IAAv7 = Int('IAAv7')    # Pointer<805177838>.this$0.access$500().checkAnyUserHasSeenToS()
IAAv4 = Real('IAAv4')    # Pointer<805177838>.mHasChildAccount
IAAv2 = Int('IAAv2')    # Pointer<-1202501681>.getInstance().checkHasChildAccount().SDK_INT
IAAv6 = Int('IAAv6')    # Pointer<805177838>.this$0.access$000()
IAAv3 = Real('IAAv3')    # Pointer<805177838>.mIsAndroidEduDevice
IAAv9 = Real('IAAv9')    # Pointer<805177838>.this$0.mObserver

s.add(And(And(And(And(And(Or((IAAv0 == 0), (IAAv0 != 0)), (IAAv1 != 0)), (IAAv2 < 18)), And((IAAv3 != 0), (IAAv4 != 0))), And(And(Or(Or(And((IAAv5 == 0), (IAAv6 != 0)), And((IAAv5 == 0), (IAAv6 == 0))), (IAAv5 != 0)), (IAAv7 == 0)), (IAAv8 == 0))), Or((IAAv9 == 0), (IAAv9 != 0))))

